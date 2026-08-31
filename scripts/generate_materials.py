"""Generate experimental media, never the task-plot illustration.

Digital pixel adaptation of Bex et al.1999 translation stimuli. No angular or
photometric calibration is implied. Encoding/decoding is audited explicitly.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import cv2
import imageio_ffmpeg
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SIZE = 512
FPS = 60
SECONDS = 30
PERIOD = 32
SIGMA = 25.6
CENTERS = ((-128, 0), (128, 0), (0, -128), (0, 128))


def frame_at(index, direction):
    yy, xx = np.mgrid[:SIZE, :SIZE].astype(float)
    xx -= (SIZE - 1) / 2
    yy -= (SIZE - 1) / 2
    modulation = np.zeros_like(xx)
    for cx, cy in CENTERS:
        envelope = np.exp(-((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * SIGMA ** 2))
        carrier = np.cos(2 * np.pi * ((xx - cx) / PERIOD - direction * 4 * index / FPS))
        modulation += envelope * carrier
    gray = np.rint(128 * (1 + 0.4 * modulation)).clip(0, 255).astype(np.uint8)
    gray[(np.abs(xx) <= 4) & (np.abs(yy) <= 0.5)] = 20
    gray[(np.abs(yy) <= 4) & (np.abs(xx) <= 0.5)] = 20
    return np.repeat(gray[:, :, None], 3, axis=2)


def generate():
    target = ROOT / 'assets' / 'motion'
    target.mkdir(parents=True, exist_ok=True)
    audit = {'generator_version': 'pixel-translation-v1', 'size_px': SIZE,
             'fps': FPS, 'duration_s': SECONDS, 'temporal_frequency_hz': 4,
             'frames_per_cycle': 15, 'phase_step_cycles': 1/15,
             'carrier_period_px': PERIOD, 'gaussian_sigma_px': SIGMA,
             'patch_centers_px': CENTERS, 'digital_modulation': 0.4,
             'physical_calibration': False, 'files': {}}
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    for label, direction in [('left', -1), ('right', 1)]:
        path = target / f'{label}.mp4'
        cmd = [ffmpeg, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-vcodec',
               'rawvideo', '-s', f'{SIZE}x{SIZE}', '-pix_fmt', 'rgb24', '-r', str(FPS),
               '-i', '-', '-an', '-c:v', 'libx264', '-preset', 'fast', '-crf', '10',
               '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(path)]
        writer = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        expected_cycle = [frame_at(i, direction) for i in range(15)]
        cycle = [f.tobytes() for f in expected_cycle]
        for i in range(FPS * SECONDS):
            writer.stdin.write(cycle[i % 15])
        writer.stdin.close()
        if writer.wait() != 0:
            raise RuntimeError('Encoding failed')
        cap = cv2.VideoCapture(str(path))
        count = 0
        max_error = 0
        first = last = None
        cycle_decoded = []
        while True:
            ok, bgr = cap.read()
            if not ok:
                break
            rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
            max_error = max(max_error, int(np.abs(rgb.astype(np.int16) - expected_cycle[count % 15].astype(np.int16)).max()))
            if count == 0:
                first = rgb.copy()
            if count < 15:
                cycle_decoded.append(rgb.copy())
            last = rgb.copy()
            count += 1
        decoded_fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        assert count == FPS * SECONDS and decoded_fps == FPS, (count, decoded_fps)
        assert max_error <= 5, max_error
        Image.fromarray(first).save(target / f'{label}_first.png')
        Image.fromarray(last).save(target / f'{label}_static.png')
        # Signed spatial shift is established by comparing all15 decoded phases
        # with independent expected-direction versus reversed-direction models.
        mse_correct = np.mean([(f.astype(float)-frame_at(i,direction))**2 for i,f in enumerate(cycle_decoded)])
        mse_reversed = np.mean([(f.astype(float)-frame_at(i,-direction))**2 for i,f in enumerate(cycle_decoded)])
        assert mse_correct < mse_reversed / 20
        audit['files'][label] = {'movie_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'bytes': path.stat().st_size, 'decoded_frame_count': count, 'decoded_fps': decoded_fps,
            'max_rgb_encoding_error': max_error, 'direction_mse': float(mse_correct),
            'opposite_direction_mse': float(mse_reversed),
            'static_sha256': hashlib.sha256((target / f'{label}_static.png').read_bytes()).hexdigest(),
            'final_frame_index': count - 1, 'final_frame_pts_s': (count-1)/FPS}
    (ROOT/'references'/'material_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf8')
    print(json.dumps(audit,indent=2))


if __name__ == '__main__':
    generate()

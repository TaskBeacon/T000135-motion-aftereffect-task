from pathlib import Path
import json
import hashlib
import numpy as np
from PIL import Image
from scipy.optimize import least_squares

root=Path('E:/Taskbeacon/T000135-motion-aftereffect-task/validation/native_grating_canary')
report={'kind':'actual PsychoPy shader back-buffer fit; not physical photometry','fits':[]}
yy,xx=np.mgrid[-80:80,-80:80].astype(float)
xx+=.5;yy+=.5
for phase in [0,.25,.5,.75]:
    path=root/f'phase_{phase}_back.png'
    actual=np.array(Image.open(path).convert('RGB'),dtype=float)[320:480,432:592,0]
    # Independent nonlinear fit to measured image. Frequency, sigma, center,
    # mean, contrast and phase are free, rather than copied from renderer.
    def model(p):
        mean,amplitude,frequency,phase_fit,sx,sy,cx,cy=p
        envelope=np.exp(-.5*(((xx-cx)/sx)**2+((yy-cy)/sy)**2))
        return mean+amplitude*envelope*np.cos(2*np.pi*(frequency*(xx-cx)-phase_fit))
    result=least_squares(lambda p:(model(p)-actual).ravel(),
        [128,51,1/32,phase,25,25,0,0],
        bounds=([120,30,.028,phase-.4,20,20,-2,-2],[135,70,.035,phase+.4,32,32,2,2]))
    p=result.x
    error=((p[3]-phase+.5)%1)-.5
    report['fits'].append({'input_phase':phase,'measured_phase_cycles':p[3],
        'cyclic_phase_error':error,'spatial_frequency_cycles_per_px':p[2],
        'sigma_x_px':p[4],'sigma_y_px':p[5],'center_offset_px':p[6:].tolist(),
        'mean_rgb':p[0],'amplitude_rgb':p[1],'digital_contrast':p[1]/127.5,
        'rmse_rgb':float(np.sqrt(np.mean((model(p)-actual)**2))),
        'max_error_rgb':float(np.max(abs(model(p)-actual))),
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
evidence=json.loads((root/'evidence.json').read_text()) if (root/'evidence.json').exists() else {'dynamic':[]}
report['dynamic']=[]
for row in evidence['dynamic']:
    times=np.array(row['adaptation_drift_sample_times_s'])
    shifts=np.array(row['adaptation_drift_phase_shifts_cycles'])
    flips=np.array(row['adaptation_drift_flip_times_s'])
    report['dynamic'].append({'direction':row['direction'],'phase_slope_cycles_per_s':float(np.polyfit(times,shifts,1)[0]),
        'frame_count':len(times),'last_phase_sample_s':times[-1],
        'max_flip_interval_s':float(np.max(np.diff(flips))),
        'intervals_over_25ms':int(np.sum(np.diff(flips)>.025)),
        'adaptation_to_static_s':row['adaptation_to_static_s'],
        'last_drift_to_static_s':row['last_drift_to_static_s'],
        'late_close':row['adaptation_drift_late_close'],
        'static_equals_actual_final_phase':row['static_phase_actual']==row['adaptation_drift_final_phases']})
report['checks']={
    'two_directions_present':len(report['dynamic'])==2 and {d['direction'] for d in report['dynamic']}=={'left','right'},
    'four_phases_error_under_0_02cycles':all(abs(f['cyclic_phase_error'])<.02 for f in report['fits']),
    'fitted_sf_within_1percent':all(abs(f['spatial_frequency_cycles_per_px']*32-1)<.01 for f in report['fits']),
    'fitted_sigma_within_1px':all(abs(f['sigma_x_px']-25.6)<1 and abs(f['sigma_y_px']-25.6)<1 for f in report['fits']),
    'contrast_within_0_02':all(abs(f['digital_contrast']-.4)<.02 for f in report['fits']),
    'exposure_30s_within_50ms':len(report['dynamic'])==2 and all(abs(d['adaptation_to_static_s']-30)<.05 for d in report['dynamic']),
    'max_flip_gap_under_50ms':len(report['dynamic'])==2 and all(d['max_flip_interval_s']<.05 for d in report['dynamic']),
    'no_late_close':len(report['dynamic'])==2 and all(not d['late_close'] for d in report['dynamic']),
    'transition_under_50ms':len(report['dynamic'])==2 and all(0<=d['last_drift_to_static_s']<.05 for d in report['dynamic']),
    'static_phase_preserved':len(report['dynamic'])==2 and all(d['static_equals_actual_final_phase'] for d in report['dynamic'])}
report['status']='pass' if all(report['checks'].values()) else 'fail'
(root/'analysis.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps(report,indent=2))

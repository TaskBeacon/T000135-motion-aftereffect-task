from psyflow import StimUnit, next_trial_id, set_trial_context
from .utils import score, timing_quality


def run_trial(win, kb, settings, condition, stim_bank, trigger_runtime, block_id=None, block_idx=None):
    trial_id = next_trial_id()
    if condition not in ('left', 'right'):
        raise ValueError('Unknown translation direction')
    drift_hz = (-1 if condition == 'left' else 1) * settings.temporal_frequency_hz
    row = dict(trial_id=trial_id, block_id=block_id, block_idx=block_idx, condition=condition,
               drift_direction=condition, temporal_frequency_hz=drift_hz,
               spatial_frequency_cycles_per_pixel=1/32, gaussian_sigma_pixels=25.6,
               physical_calibration=False, diagnostic=settings.diagnostic,
               protocol_version='translation-static-gabor-v1')
    gratings = [stim_bank.get(f'patch_{index}') for index in range(4)]
    # Reset only at the beginning of a new trial. The shared runtime animates
    # phase and the static test retains exactly the last drawn phase.
    for grating in gratings:
        grating.phase = [0, 0]
    fixation = stim_bank.get('fixation')

    def unit(phase, *stims, keys=(), duration=None):
        u = StimUnit(phase, win, kb, runtime=trigger_runtime).add_stim(*stims)
        set_trial_context(u, trial_id=trial_id, phase=phase, deadline_s=duration,
                          valid_keys=list(keys), block_id=block_id, condition_id=condition,
                          stim_id='four_translation_gabors', task_factors={'direction': condition})
        return u

    unit('fixation', fixation, duration=settings.fixation_duration).show(
        duration=settings.fixation_duration, onset_trigger=settings.triggers['fixation_onset']).to_dict(row)
    adaptation = unit('adaptation', *gratings, fixation, duration=settings.adaptation_duration)
    adaptation.show(duration=settings.adaptation_duration, phase_drift_hz=drift_hz,
                    onset_trigger=settings.triggers['adaptation_onset'])
    report = unit('static_test', *gratings, fixation,
                  keys=settings.report_keys, duration=settings.test_duration)
    report.capture_response(keys=settings.report_keys, duration=settings.test_duration,
        terminate_on_response=True, onset_trigger=settings.triggers['static_onset'],
        response_trigger={settings.ceased_key:settings.triggers['motion_ceased'], settings.none_key:settings.triggers['no_motion']},
        timeout_trigger=settings.triggers['omission'])
    report.set_state(hit=None)
    adaptation.to_dict(row); report.to_dict(row)
    row.update(score(report.get_state('response'), report.get_state('rt'), settings.ceased_key, settings.none_key))
    row['static_phase_actual'] = [g.phase.tolist() for g in gratings]
    row['adaptation_to_static_s'] = report.get_state('flip_time') - adaptation.get_state('flip_time')
    row['last_drift_to_static_s'] = report.get_state('flip_time') - adaptation.get_state('offset_flip_time')
    nominal = adaptation.get_state('duration_scaled', settings.adaptation_duration)
    row['technical_timing_ok'] = timing_quality(row['adaptation_to_static_s'], nominal,
        adaptation.get_state('drift_max_frame_interval_s'), row['last_drift_to_static_s'], settings.max_frame_gap_s)
    row['motion_invalid_reasons'] = []
    if abs(row['adaptation_to_static_s']-nominal)>settings.max_frame_gap_s:
        row['motion_invalid_reasons'].append('adaptation_duration')
    if adaptation.get_state('drift_max_frame_interval_s')>settings.max_frame_gap_s:
        row['motion_invalid_reasons'].append('frame_gap')
    if row['last_drift_to_static_s']>settings.max_frame_gap_s:
        row['motion_invalid_reasons'].append('static_transition_gap')
    if adaptation.get_state('drift_late_close', False):
        row['motion_invalid_reasons'].append('late_close')
    if row['static_phase_actual'] != adaptation.get_state('drift_final_phases'):
        row['motion_invalid_reasons'].append('phase_discontinuity')
    row['motion_valid'] = row['technical_timing_ok'] and not row['motion_invalid_reasons']
    row['valid_duration_report'] = row['motion_valid'] and not row['missing_response']
    unit('recovery', fixation, duration=settings.recovery_duration).show(
        duration=settings.recovery_duration, onset_trigger=settings.triggers['recovery_onset']).to_dict(row)
    return row

"""Trial scheduling and report semantics; these do not infer perception."""
import math


def score(response, rt, ceased_key='space', none_key='n'):
    if response == none_key:
        return dict(report_category='no_apparent_motion', reported_duration_s=0.0,
                    report_rt_s=rt, missing_response=False, duration_censored=False)
    if response == ceased_key and rt is not None and math.isfinite(float(rt)) and rt >= 0:
        return dict(report_category='motion_ceased', reported_duration_s=float(rt),
                    report_rt_s=rt, missing_response=False, duration_censored=False)
    return dict(report_category='missing', reported_duration_s=None, report_rt_s=rt,
                missing_response=True, duration_censored=True)


def timing_quality(exposure, requested, max_gap, transition_gap, limit=.05):
    values = (exposure, requested, max_gap, transition_gap)
    return (all(isinstance(v, (float, int)) and math.isfinite(v) for v in values)
            and abs(exposure-requested) <= limit and 0 <= max_gap <= limit
            and 0 <= transition_gap <= limit)


def summarize(rows):
    by_direction={}
    for direction in ('left','right'):
        selected=[r for r in rows if r['condition']==direction]
        durations=[r['reported_duration_s'] for r in selected if r['valid_duration_report']]
        by_direction[direction]={'trials':len(selected),'valid_reports':len(durations),
            'mean_reported_duration_s':sum(durations)/len(durations) if durations else None,
            'invalid_motion':sum(not r['motion_valid'] for r in selected)}
    return {'trials': len(rows), 'motion_ceased_reports': sum(r['report_category']=='motion_ceased' for r in rows),
            'no_apparent_motion_reports': sum(r['report_category']=='no_apparent_motion' for r in rows),
            'missing_reports': sum(r['missing_response'] for r in rows),
            'invalid_motion_trials': sum(not r['motion_valid'] for r in rows), 'by_direction':by_direction,
            'interpretation': 'Self-reports only; no accuracy score, calibrated threshold, or proof of an aftereffect.'}

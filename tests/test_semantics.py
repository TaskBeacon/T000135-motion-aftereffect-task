import pytest
from src.utils import score, timing_quality


def test_no_motion_is_zero_but_actual_motor_rt_preserved():
    result=score('n',1.2)
    assert result['reported_duration_s']==0
    assert result['report_rt_s']==1.2
    assert not result['missing_response'] and not result['duration_censored']


def test_ceased_report_uses_elapsed_rt():
    result=score('space',4.25)
    assert result['reported_duration_s']==4.25
    assert result['report_category']=='motion_ceased'


@pytest.mark.parametrize('response,rt',[(None,None),('x',2),('space',None),('space',float('nan')),('space',-1)])
def test_absent_invalid_report_never_becomes_zero_or_deadline(response,rt):
    result=score(response,rt)
    assert result['reported_duration_s'] is None
    assert result['duration_censored'] and result['missing_response']


@pytest.mark.parametrize('exposure,gap,tail',[(29,.017,.017),(30,.3,.017),(30,.017,.2),(float('nan'),.017,.017)])
def test_partial_or_stalled_adaptation_is_flagged(exposure,gap,tail):
    assert not timing_quality(exposure,30,gap,tail)


def test_software_timing_tolerance_does_not_require_fixed_frame_count():
    assert timing_quality(30.01,30,.023,.016)

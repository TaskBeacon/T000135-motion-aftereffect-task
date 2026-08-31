from pathlib import Path
import json
import sys
import traceback
from PIL import ImageGrab
sys.path.insert(0,'E:/Taskbeacon/psyflow-grating135-publish')
from psychopy import visual
from psychopy.hardware.keyboard import Keyboard
from psyflow import StimUnit
out=Path('E:/Taskbeacon/T000135-motion-aftereffect-task/validation/native_grating_canary')
out.mkdir(parents=True,exist_ok=True)
win=visual.Window(size=[1280,800],units='pix',color='#808080',fullscr=False,checkTiming=True)
kb=Keyboard();report={'static':[],'dynamic':[],'physical_calibration':False};active=None
try:
    gratings=[visual.GratingStim(win,tex='sin',mask='gauss',size=[256,256],sf=1/32,
        phase=[0,0],contrast=.4,maskParams={'sd':5},texRes=1024,pos=pos,units='pix',autoLog=False)
        for pos in [(-128,0),(128,0),(0,128),(0,-128)]]
    cross=visual.TextStim(win,text='+',height=12,color='#141414',pos=[0,0],units='pix',autoLog=False)
    for phase in [0,.25,.5,.75]:
        for g in gratings:g.phase=[phase,0]
        u=StimUnit('static_reference',win,kb).add_stim(*gratings,cross).show(.1)
        # On this desktop GL_FRONT returns black. Save the actual shader-drawn
        # back buffer plus a separate OS capture; neither is photometry.
        for g in gratings:g.draw()
        cross.draw()
        win.getMovieFrame(buffer='back');win.saveMovieFrames(str(out/f'phase_{phase}_back.png'))
        win.flip()
        x,y=win.winHandle.get_location();w,h=win.winHandle.get_size()
        os_capture={'status':'pass'}
        try:ImageGrab.grab(bbox=(x,y,x+w,y+h)).save(out/f'phase_{phase}_os.png')
        except OSError as error:os_capture={'status':'unavailable','error':repr(error)}
        report['static'].append({'phase':phase,'file':f'phase_{phase}_back.png','os_capture':os_capture})
    # Timing batch contains no screenshots or file writes between drift onset
    # and the first static-test flip, so transition evidence is unperturbed.
    for direction,hz in [('left',-4),('right',4)]:
        for g in gratings:g.phase=[0,0]
        active=StimUnit('adaptation',win,kb).add_stim(*gratings,cross)
        active.show(30,phase_drift_hz=hz)
        test=StimUnit('static_test',win,kb).add_stim(*gratings,cross).show(.1)
        for g in gratings:g.draw()
        cross.draw()
        win.getMovieFrame(buffer='back');win.saveMovieFrames(str(out/f'{direction}_final_static_back.png'))
        states={};active.to_dict(states);test.to_dict(states)
        report['dynamic'].append({'direction':direction,**states,
          'adaptation_to_static_s':test.get_state('flip_time')-active.get_state('flip_time'),
          'last_drift_to_static_s':test.get_state('flip_time')-active.get_state('offset_flip_time'),
          'static_phase_actual':[g.phase.tolist() for g in gratings]})
        (out/'evidence.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    report['status']='pass'
except BaseException as error:
    report['status']='fail';report['error']=repr(error);report['traceback']=traceback.format_exc()
    if active is not None:
        report['failing_unit']={};active.to_dict(report['failing_unit'])
    raise
finally:
    win.close();(out/'evidence.json').write_text(json.dumps(report,indent=2),encoding='utf8')

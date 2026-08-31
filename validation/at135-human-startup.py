from pathlib import Path
from types import SimpleNamespace
import json
import sys
sys.path[:0]=['E:/Taskbeacon/psyflow-grating135-publish','E:/Taskbeacon/T000135-motion-aftereffect-task']
from psychopy import gui
from psychopy.gui.qtgui import haveQt
from importlib import import_module
QtCore=import_module(f'{haveQt}.QtCore')
import main

root=Path('E:/Taskbeacon/T000135-motion-aftereffect-task')
out=root/'validation/human_startup';out.mkdir(parents=True,exist_ok=True)
report={'mode':'human','subject_dialog':'not assessed: synthetic135 injected after actual Qt automation timed out',
        'scope':'real human branch initialize_exp, StimBank preload and first instruction shader draw/flip; stopped at checkpoint',
        'dialogs':[],'status':'running'}
original_show=gui.Dlg.show
def automate_dialog(self):
    def fill_and_accept():
        for field in self.inputFields:
            if hasattr(field,'setText'):field.setText('135')
        report['dialogs'].append({'title':self.windowTitle(),'field_count':len(self.inputFields)})
        self.okBtn.click()
    QtCore.QTimer.singleShot(250,fill_and_accept)
    return original_show(self)
main.SubInfo.collect=lambda self:{'subject_id':135}

class Checkpoint(Exception):pass
original_init=main.initialize_exp
def measured_init(settings):
    win,kb=original_init(settings)
    report['window_size']=win.size.tolist();report['subject_id']=settings.subject_id
    original_flip=win.flip
    def first_instruction_flip(*args,**kwargs):
        win.getMovieFrame(buffer='back');win.saveMovieFrames(str(out/'instruction_actual_back.png'))
        t=original_flip(*args,**kwargs)
        report['instruction_actual_flip']=t
        raise Checkpoint('Stopped after actual first human instruction flip')
    win.flip=first_instruction_flip
    return win,kb
main.initialize_exp=measured_init
original_preload=main.StimBank.preload_all
def measured_preload(self):
    result=original_preload(self)
    report['actual_preloaded_types']={key:type(self.get(key)).__name__ for key in self.keys()}
    return result
main.StimBank.preload_all=measured_preload
try:
    main.run(SimpleNamespace(mode='human',config_path=root/'config/config.yaml'))
except Checkpoint:
    report['status']='pass'
except BaseException as error:
    report['status']='fail';report['error']=repr(error)
    raise
finally:
    (out/'evidence.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False))

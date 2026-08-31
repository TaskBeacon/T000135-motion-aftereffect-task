from pathlib import Path
import json
import shutil
import subprocess
import sys
import yaml
root=Path('E:/Taskbeacon/T000135-motion-aftereffect-task')
negative=Path('E:/Taskbeacon/tmp/at135-taps-negative/T000135-motion-aftereffect-task')
negative.mkdir(parents=True,exist_ok=True)
for name in ['src','config','responders','references']:
    shutil.copytree(root/name,negative/name,dirs_exist_ok=True)
for name in ['main.py','taskbeacon.yaml','README.md','CHANGELOG.md','.gitignore']:
    shutil.copy2(root/name,negative/name)
cfg=yaml.safe_load((negative/'config/config.yaml').read_text(encoding='utf8'))
cfg['stimuli']['patch_0']['type']='not_a_supported_stimulus'
(negative/'config/config.yaml').write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False),encoding='utf8')
base=[sys.executable,'-X','utf8','-c','from taps_utils.validate import main; import sys; raise SystemExit(main(sys.argv[1:]))']
tail=['--contracts-version','v0.2.0','--contracts-root','E:/Taskbeacon/taps-grating135-publish/contracts']
results=[]
for name,path in [('positive',root),('negative_unknown_type',negative)]:
    p=subprocess.run([*base,str(path),*tail],capture_output=True,text=True,encoding='utf8')
    results.append({'case':name,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
assert results[0]['exit_code']==0
assert results[1]['exit_code']!=0 and "type 'not_a_supported_stimulus' is unsupported" in results[1]['stdout']
(root/'validation/taps-grating-contract.json').write_text(json.dumps({'status':'pass','cases':results},indent=2),encoding='utf8')
print('PASS: actual full validator accepts grating and rejects unknown type;2 cases')

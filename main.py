from contextlib import nullcontext
from functools import partial
from pathlib import Path
import json
import pandas as pd
from psychopy import core
from psyflow import (BlockUnit, StimBank, StimUnit, SubInfo, TaskSettings, context_from_config,
    initialize_exp, initialize_triggers, load_config, parse_task_run_options, runtime_context)
from src.run_trial import run_trial
from src.utils import summarize

MODES = ('human', 'qa', 'sim')
DEFAULT_CONFIG_BY_MODE = {'human':'config/config.yaml', 'qa':'config/config_qa.yaml', 'sim':'config/config_scripted_sim.yaml'}


def run(options):
    root = Path(__file__).resolve().parent
    cfg = load_config(str(options.config_path))
    ctx = context_from_config(task_dir=root, config=cfg, mode=options.mode) if options.mode in ('qa','sim') else None
    with runtime_context(ctx) if ctx else nullcontext():
        subject = {'subject_id':135} if ctx else SubInfo(cfg['subform_config']).collect()
        settings = TaskSettings.from_dict(cfg['task_config']); settings.add_subinfo(subject)
        if ctx:
            ctx.output_dir.mkdir(parents=True, exist_ok=True)
            settings.res_file = str(ctx.output_dir / ('qa_trace.csv' if options.mode=='qa' else 'sim_trace.csv'))
            settings.log_file = str(ctx.output_dir / 'psychopy.log')
            settings.json_file = str(ctx.output_dir / 'settings.json')
        if settings.trial_per_block % 2 or settings.total_trials != settings.total_blocks * settings.trial_per_block:
            raise ValueError('Use even balanced blocks and consistent trial count')
        weights = settings.resolve_condition_weights()
        settings.triggers = cfg['trigger_config']
        trigger_runtime = initialize_triggers(mock=True) if ctx else initialize_triggers(cfg)
        win, kb = initialize_exp(settings)
        try:
            if min(win.size) < 600:
                raise ValueError('At least600screen pixels required; fixed-pixel gratings must not be resized')
            bank = StimBank(win, cfg['stim_config']).preload_all(); settings.save_to_json(); rows = []
            trigger_runtime.send(settings.triggers['experiment_start'])
            StimUnit('instruction', win, kb, runtime=trigger_runtime).add_stim(bank.get('instruction')).wait_and_continue(keys=[settings.continue_key])
            for block_idx in range(settings.total_blocks):
                block_id = f'block_{block_idx+1}'
                block = BlockUnit(block_id=block_id, block_idx=block_idx, settings=settings, window=win, keyboard=kb, n_trials=settings.trial_per_block)
                block.generate_conditions(condition_labels=settings.conditions, weights=weights, order='random')
                block.run_trial(partial(run_trial, stim_bank=bank, trigger_runtime=trigger_runtime, block_id=block_id, block_idx=block_idx))
                block.to_dict(rows); pd.DataFrame(rows).to_csv(settings.res_file, index=False)
                if block_idx+1 < settings.total_blocks:
                    StimUnit('block_break', win, kb, runtime=trigger_runtime).add_stim(bank.get('block_break')).wait_and_continue(keys=[settings.continue_key])
            Path(settings.res_file).with_suffix('.summary.json').write_text(json.dumps(summarize(rows),ensure_ascii=False,indent=2),encoding='utf8')
            StimUnit('good_bye', win, kb, runtime=trigger_runtime).add_stim(bank.get('good_bye')).wait_and_continue(keys=[settings.continue_key])
            trigger_runtime.send(settings.triggers['experiment_end'])
        finally:
            trigger_runtime.close(); win.close()
    core.quit()


def main():
    run(parse_task_run_options(task_root=Path(__file__).resolve().parent, description='Motion Aftereffect Task', default_config_by_mode=DEFAULT_CONFIG_BY_MODE, modes=MODES))


if __name__ == '__main__':
    main()

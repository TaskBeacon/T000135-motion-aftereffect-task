from dataclasses import dataclass
from psyflow.sim.contracts import Action


@dataclass
class TaskSamplerResponder:
    rt_s: float = .15

    def start_session(self, session, rng):
        self.index = 0

    def act(self, obs):
        keys = list(obs.valid_keys or [])
        if 'n' in keys:
            response = ['space', 'n', None][self.index % 3]
            self.index += 1
            return Action(key=response, rt_s=self.rt_s if response else None)
        return Action(key='space', rt_s=self.rt_s) if 'space' in keys else Action(key=None, rt_s=None)

    def on_feedback(self, feedback):
        pass

    def end_session(self):
        pass

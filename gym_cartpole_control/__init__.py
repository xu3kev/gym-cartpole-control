import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='CartPoleControl-v0',
    entry_point='gym_cartpole_control.envs:CartPoleControlEnv',
    timestep_limit=1000,
    reward_threshold=995,
)

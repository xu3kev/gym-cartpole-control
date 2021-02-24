import logging
import gym_cartpole_control.envs
from gym.envs.registration import register

logger = logging.getLogger(__name__)

print("register custom cartpole env")
register(
    id='CartPoleControl-v0',
    entry_point='gym_cartpole_control.envs:CartPoleControlEnv',
    max_episode_steps=500,
    reward_threshold=475,
)
register(
    id='CartPoleControl-v1',
    entry_point='gym_cartpole_control.envs:CartPoleControlEnv',
    max_episode_steps=10000,
    reward_threshold=9975,
)

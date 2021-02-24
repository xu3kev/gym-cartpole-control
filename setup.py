from setuptools import setup

setup(name='gym_cartpole_control',
      version='0.0.1',
      install_requires=['gym>=0.2.3'],
      packages=['gym_cartpole_control', 'gym_cartpole_control.envs']
)

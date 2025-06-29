import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv

env = gym.make('LunarLander-v3')
env = DummyVecEnv([lambda: env])

# Train
model = DQN('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=1000000)

# Save model
model.save('dqn_lunar_lander')

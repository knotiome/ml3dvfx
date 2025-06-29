import gymnasium as gym
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv

env = gym.make('LunarLander-v3', render_mode='human')
env = DummyVecEnv([lambda: env])

model = DQN.load("dqn_lunar_lander")

obs = env.reset()

for _ in range(1000):
    action, _ = model.predict(obs, deterministic=True)
    obs, rewards, done, info = env.step(action)
    if done:
        obs = env.reset()
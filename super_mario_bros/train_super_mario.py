import gym_super_mario_bros
from gym.wrappers import GrayScaleObservation
from nes_py.wrappers import JoypadSpace
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import os
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback

JoypadSpace.reset = lambda self, **kwargs: self.env.reset(**kwargs)
env = gym_super_mario_bros.make('SuperMarioBros-v0', apply_api_compatibility=True, render_mode='human')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
env = GrayScaleObservation(env, keep_dim=True)
env = DummyVecEnv([lambda: env])
env = VecFrameStack(env, 4, channels_order='last')

state = env.reset()

class TrainLogCallback(BaseCallback):
    def __init__(self, check_freq, save_path, verbox=1):
        super(TrainLogCallback, self).__init__(verbose=1)
        self.check_freq = check_freq
        self.save_path = save_path

    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self):
        if self.n_calls % self.check_freq == 0:
            model_path = os.path.join(self.save_path, 'best_model_{}'.format(self.n_calls))
            self.model.save(model_path)
        return True

checkpoint_path = './train'
log_dir = './logs'

callback = TrainLogCallback(check_freq=10000, save_path=checkpoint_path)

model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=log_dir, learning_rate=0.000001, n_steps=512)
model.learn(total_timesteps=1000000, callback=callback)

print("Done training")








from vizdoom import DoomGame, Mode, Button
import random

CONFIG_FILE = "deadly_corridor.cfg"

def initialize_game(config_file, render=True):
    game = DoomGame()
    game.load_config(config_file)
    game.set_mode(Mode.PLAYER)
    game.set_window_visible(render)
    game.add_available_button(Button.MOVE_LEFT)
    game.add_available_button(Button.MOVE_RIGHT)
    game.add_available_button(Button.ATTACK)
    game.init()

    return game

class RandomAgent:
    def __init__(self, action_space):
        self.action_space = action_space

    def get_action(self):
        return [random.choice([0,1]) for _ in range(len(self.action_space))]

def train_agent(game, agent, num_episodes=10, render=True):
    for episode in range(num_episodes):
        game.new_episode()
        while not game.is_episode_finished():
            state = game.get_state()
            action = agent.get_action()
            reward = game.make_action(action)
            print(f"Reward: {reward}, Action: {action}")
        print(f"Episode: {episode + 1} finished.  Total reward: {game.get_total_reward()}")
    game.close()
    
if __name__ == "__main__":
    render_game = True
    game = initialize_game(config_file=CONFIG_FILE, render=render_game)
    action_space = game.get_available_buttons()
    agent = RandomAgent(action_space)
    train_agent(game, agent, num_episodes=500, render=render_game)




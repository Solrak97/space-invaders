from random import random
import torch.nn as nn
from PIL import Image
from actions import Actions
import numpy as np
import torch

class Agent():
    def __init__(self):

        # Agent Settings
        self.EMPTY_REWARD = -1
        self.KILL_REWARD = 1000
        self.DISCOUNT_FACTOR = 1e-3
        self.eps_greedy = 1
        self.decay = 1e-4

        # Agent networks
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.action_map = [Actions.MOVE_LEFT,Actions.MOVE_RIGHT, Actions.SHOOT]

        self.prediction_network = DQAgent().to(self.device)
        self.target_network = DQAgent().to(self.device)

        self.optimizer = torch.optim.Adam(self.prediction_network.parameters)



    def play(self, env):
        while (not env.is_terminal_state()):
            self.step(env, learn=False)



    def simulation(self, env):
        while (not env.is_terminal_state()):
            self.step(env, learn=True)

        if self.eps_greedy >= self.decay:
            self.eps_greedy -= self.decay



    def step(self, env, learn=True):
        state = env.get_state()
        q_index = self.state_to_index(state)

        if learn:
            action_index = self.select_action(q_index)
            reward, state = env.perform_action(self.actions[action_index])
            

            # Update
            q_index_prime = self.state_to_index(state)
            self.qtable[q_index][action_index] = (self.qtable[q_index][action_index] + self.learning_rate * (
                reward + self.discount_factor * np.max(self.qtable[q_index_prime]) - self.qtable[q_index][action_index]))

        else:
            action_index = np.argmax(self.qtable[q_index])
            env.perform_action(self.actions[action_index])
        

    # Transforms str into torch tensor
    def to_tensor(self, str_img):
        img = Image.frombytes('RGB', (640, 480), str_img, 'raw')
        img_array = np.array(img).reshape((3, 640, 480))
        state = torch.tensor(img_array).to(self.device).type(torch.float32).unsqueeze(dim=0)
        return state



    # Recibe el estado
    def get_Q(self, state):
        img = self.to_tensor(state)
        Q_val = self.prediction_network(img)
        
        return Q_val



    def act(self, state):
        q_vals = self.get_Q(state)

        if self.training and random.random() < self.EPS_GREEDY:
            action = random.sample(self.action_map)

        else:
            action = torch.argmax(q_vals, dim=1)[0].cpu()
            action = self.action_map[action]

        return action
        

    # Recibe el reward y ejecuta la corrección de error
    def update(self, reward):
        error = reward + self.DISCOUNT_FACTOR * self.future_Q - self.Q_val
        self.optimizer
        pass




# Red neuronal del agente
class DQAgent(nn.Module):
    def __init__(self):
        super(DQAgent, self).__init__()

        self.cl1 = nn.Conv2d(in_channels=3, out_channels=12, kernel_size=5)
        self.cl2 = nn.Conv2d(in_channels=12, out_channels=24, kernel_size=5)
        self.cl3 = nn.Conv2d(in_channels=24, out_channels=48, kernel_size=5)
        self.cl4 = nn.Conv2d(in_channels=48, out_channels=96, kernel_size=5)
        self.cl5 = nn.Conv2d(in_channels=96, out_channels=194, kernel_size=5)


        self.feature_activator = nn.LeakyReLU()
        self.feature_pool = nn.MaxPool2d(2, 2)

        self.classification = nn.Linear(in_features=194*16*11, out_features=3)
        

    def forward(self, x):
        x = self.feature_pool(self.feature_activator(self.cl1(x)))
        x = self.feature_pool(self.feature_activator(self.cl2(x)))
        x = self.feature_pool(self.feature_activator(self.cl3(x)))
        x = self.feature_pool(self.feature_activator(self.cl4(x)))
        x = self.feature_pool(self.feature_activator(self.cl5(x)))

        x = x.view(-1, 194 * 16 * 11)

        action = self.classification(x)
        
        return action

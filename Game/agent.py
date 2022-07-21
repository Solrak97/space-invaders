import torch.nn as nn
from PIL import Image
from actions import Actions
import numpy as np
import torch


class Agent():
    def __init__(self):

        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')

        self.action_map = [Actions.MOVE_LEFT,
                           Actions.MOVE_RIGHT, Actions.SHOOT]
        self.last_state = None

        self.prediction_network = DQAgent().to(self.device)
        self.target_network = DQAgent().to(self.device)

        '''
        self.PATH = './agent.pth'
        torch.save(model.state_dict(), PATH)
        '''

    # Actualiza el agente cuando se obtiene un fitting aceptable
    def update_agent():
        pass

    # Recibe el estado

    def capture_state(self, state):
        img = Image.frombytes('RGB', (640, 480), state, 'raw')
        img_array = np.array(img).reshape((3, 640, 480))
        self.last_state = torch.tensor(img_array).to(
            self.device).type(torch.float32).unsqueeze(dim=0)
        pass

    # torch.cuda.IntTensor

    # Recibe el reward y ejecuta la corrección de error
    def reward(self, reward):
        pass

    # PRedice el estado y ejecuta una acción

    def get_action(self):
        self.prediction_network(self.last_state)

        return Actions.SHOOT


# Red neuronal del agente
class DQAgent(nn.Module):
    def __init__(self):
        super(DQAgent, self).__init__()

        filters = [3, 12, 24, 48, 96, 194]

        self.feature_extraction = []

        for idx in range(1, len(filters)):
            self.feature_extraction.append(nn.Conv2d(
                in_channels=filters[idx - 1], out_channels=filters[idx], kernel_size=5))

        self.feature_activator = nn.LeakyReLU()
        self.feature_pool = nn.MaxPool2d(2, 2)

        #self.activation_final = nn.Linear(17 * 5 * 5, 144)

    def forward(self, x):

        for layer in self.feature_extraction:
            x = layer(x)
            x = self.feature_activator(x)
            x = self.feature_pool(x)

        x = x.view(-1, 194 * 16 * 11)
        return x

    pass

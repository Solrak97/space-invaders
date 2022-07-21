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
        prediction = self.prediction_network(self.last_state)
        action = torch.argmax(prediction, dim=1)[0].cpu()
        return self.action_map[action]


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
        self.classification_activation = nn.Sigmoid()


    def forward(self, x):
        x = self.feature_pool(self.feature_activator(self.cl1(x)))
        x = self.feature_pool(self.feature_activator(self.cl2(x)))
        x = self.feature_pool(self.feature_activator(self.cl3(x)))
        x = self.feature_pool(self.feature_activator(self.cl4(x)))
        x = self.feature_pool(self.feature_activator(self.cl5(x)))

        x = x.view(-1, 194 * 16 * 11)

        x = self.classification(x)
        action = self.classification_activation(x)
        
        return action

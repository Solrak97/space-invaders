import torch.nn as nn
from PIL import Image
from actions import Actions
import numpy as np
import torch


class Agent():
    def __init__(self):
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.action_map = [Actions.MOVE_LEFT, Actions.MOVE_RIGHT, Actions.SHOOT]
        self.last_state = None

        self.prediction_network = DQAgent().to(self.device)
        self.target_network = DQAgent().to(self.device)
        
        '''
        self.PATH = './agent.pth'
        torch.save(model.state_dict(), PATH)
        pass
        '''


    def update_agent():
        pass
    

    def capture_state(self, state):
        img = Image.frombytes('RGB', (640, 480), state, 'raw')
        self.last_state = np.array(img)
        
        pass

    
    def reward():
        pass


    def get_action(self):
        self.prediction_network(self.last_state)

        return Actions.SHOOT
        



class DQAgent(nn.Module):
    def __init__(self):
        super(DQAgent, self).__init__()
        self.feature_extractor = []
        self.feature_extractor.append(nn.Conv2d(in_channels = 3, out_channels= 6, kernel_size = 5))
        self.feature_extractor.append(nn.LeakyReLU())
        self.feature_extractor.append(nn.MaxPool2d(2, 2))

        self.classificator = []
        self.classificator.append(nn.Linear(17 * 5 * 5, 144))
    
    def forward(self, x):
        for layer in self.feature_extractor:
            x = layer(x)

        x = x.view()

        for layers in self.classificator:
            x = layer(x)

        return x

    pass
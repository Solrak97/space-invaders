import torch.nn as nn
class   Agent(nn.Module):

    def __init__(self):
        super(Agent, self).__init__()
        self.conv1 = nn.Conv2d(in_channels = 3, out_channels= 6, kernel_size = 5)
        self.conv2 = nn.Conv2d(in_channels = 6, out_channels= 17, kernel_size = 5)
        self.activation = nn.LeakyReLU()
        self.activation_final = nn.LogSoftmax() 
        self.pooling = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(17 * 5 * 5, 144)
        self.fc2 = nn.Linear(144, 89)
        self.fc3 = nn.Linear(89, 10)

    
    def forward(self, x):
        x = self.conv1(x)
        x = self.activation(x)
        x = self.pooling(x)
        x = self.conv2(x)
        x = self.activation(x)
        x = self.pooling(x)
        x = x.view(-1, 17 * 5 * 5)
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        x = self.activation(x)
        x = self.fc3(x)
        x = self.activation_final(x)
        return x

    def train_classifier(optimizer, model, x_true, x_false, accuracy=None, max_iters=100, batch_size=1000):
        pass

    pass

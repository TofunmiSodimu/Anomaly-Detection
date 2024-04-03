import torch.nn as nn

class AnomalyModel(nn.Module):
    def __init__(self,input_size):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(in_features=input_size,out_features=4),
            nn.BatchNorm1d(num_features=4),
            nn.ReLU(),
            nn.Linear(in_features=4,out_features=4),
            nn.BatchNorm1d(num_features=4),
            nn.ReLU(),

            # Final Fully Connected Layer
            nn.Linear(in_features=4,out_features=2)
        )

    def forward(self, x):
        x = self.layers(x)
        return x

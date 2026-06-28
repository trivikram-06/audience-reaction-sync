import torch
import torch.nn as nn
import numpy as np


class EngagementModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(7, 32),
            nn.ReLU(),

            nn.Linear(32, 16),
            nn.ReLU(),

            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.network(x)


class Predictor:

    def __init__(self):

        self.model = EngagementModel()

        self.model.load_state_dict(
            torch.load(
                "models/checkpoints/engagement_model.pth",
                map_location="cpu"
            )
        )

        self.model.eval()

    def predict(
        self,
        ear,
        mar,
        blink,
        yaw,
        pitch,
        roll,
        attention
    ):

        features = np.array([
            ear,
            mar,
            blink,
            yaw,
            pitch,
            roll,
            attention
        ], dtype=np.float32)

        features = torch.tensor(
            features
        ).unsqueeze(0)

        with torch.no_grad():

            prediction = self.model(features)

        score = float(prediction.item())

        score = max(0, min(100, score))

        return score
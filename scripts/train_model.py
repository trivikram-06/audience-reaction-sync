import pandas as pd
import torch
import torch.nn as nn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ------------------------
# Load Dataset
# ------------------------

df = pd.read_csv("outputs/logs/training_dataset.csv")

# Features
X = df[
    [
        "ear",
        "mar",
        "blink_count",
        "yaw",
        "pitch",
        "roll",
        "attention"
    ]
]

# Target
y = df["engagement"]

# ------------------------
# Normalize
# ------------------------

scaler = StandardScaler()
X = scaler.fit_transform(X)

# ------------------------
# Train Test Split
# ------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)

y_train = torch.tensor(
    y_train.values,
    dtype=torch.float32
).view(-1,1)

y_test = torch.tensor(
    y_test.values,
    dtype=torch.float32
).view(-1,1)

# ------------------------
# Model
# ------------------------

class EngagementModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(7,32),
            nn.ReLU(),

            nn.Linear(32,16),
            nn.ReLU(),

            nn.Linear(16,1)

        )

    def forward(self,x):

        return self.network(x)

model = EngagementModel()

criterion = nn.MSELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

# ------------------------
# Training
# ------------------------

epochs = 100

for epoch in range(epochs):

    prediction = model(X_train)

    loss = criterion(
        prediction,
        y_train
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if epoch % 10 == 0:

        print(
            f"Epoch {epoch} | Loss {loss.item():.4f}"
        )

# ------------------------
# Save
# ------------------------

torch.save(
    model.state_dict(),
    "models/checkpoints/engagement_model.pth"
)

print("\nTraining Complete!")

print("Model Saved!")
import pandas as pd

# Load your latest CSV
df = pd.read_csv("outputs/logs/session.csv")   # <-- Change filename if needed

def calculate_engagement(attention):

    if attention >= 80:
        return 95

    elif attention >= 60:
        return 75

    elif attention >= 40:
        return 50

    elif attention >= 20:
        return 25

    else:
        return 10

df["engagement"] = df["attention"].apply(calculate_engagement)

df.to_csv(
    "outputs/logs/training_dataset.csv",
    index=False
)

print("Training dataset generated successfully!")
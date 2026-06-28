import glob
import os

import pandas as pd


class SessionAnalytics:

    def __init__(self, log_folder="outputs/logs"):

        files = glob.glob(os.path.join(log_folder, "*.csv"))

        if not files:
            raise FileNotFoundError("No session CSV files found.")

        self.latest_file = max(files, key=os.path.getctime)

        self.df = pd.read_csv(self.latest_file)

    def session_file(self):
        return os.path.basename(self.latest_file)

    def people_count(self):
        return self.df["person_id"].nunique()

    def average_attention(self):
        return round(self.df["attention"].mean(), 2)

    def average_engagement(self):
        return round(self.df["engagement"].mean(), 2)

    def highest_engagement(self):
        return round(self.df["engagement"].max(), 2)

    def lowest_engagement(self):
        return round(self.df["engagement"].min(), 2)

    def average_blinks(self):
        return round(self.df["blink_count"].mean(), 2)

    def most_attentive_person(self):

        person = (
            self.df.groupby("person_id")["attention"]
            .mean()
            .idxmax()
        )

        return int(person)

    def least_attentive_person(self):

        person = (
            self.df.groupby("person_id")["attention"]
            .mean()
            .idxmin()
        )

        return int(person)

    def session_duration(self):

        timestamps = pd.to_datetime(
            self.df["timestamp"],
            format="%H:%M:%S.%f"
        )

        duration = timestamps.max() - timestamps.min()

        return str(duration)
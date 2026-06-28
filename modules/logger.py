import csv
import os
from datetime import datetime


class FeatureLogger:

    def __init__(self):

        os.makedirs("outputs/logs", exist_ok=True)

        self.filename = (
            f"outputs/logs/session_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        self.file = open(self.filename, "w", newline="")

        self.writer = csv.writer(self.file)

        self.writer.writerow([
            "timestamp",
            "person_id",
            "ear",
            "mar",
            "eye_status",
            "blink_count",
            "yaw",
            "pitch",
            "roll",
            "attention",
            "engagement"
        ])

    def log(
        self,
        person_id,
        ear,
        mar,
        eye_status,
        blink_count,
        yaw,
        pitch,
        roll,
        attention,
        engagement
    ):

        self.writer.writerow([
            datetime.now().strftime("%H:%M:%S.%f"),
            person_id,
            round(ear, 4),
            round(mar, 4),
            eye_status,
            blink_count,
            round(yaw, 2),
            round(pitch, 2),
            round(roll, 2),
            attention,
            round(engagement, 2)
        ])

        self.file.flush()

    def close(self):
        self.file.close()
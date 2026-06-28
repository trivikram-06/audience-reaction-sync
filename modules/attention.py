class AttentionEngine:

    def __init__(self):
        pass

    def calculate(
        self,
        ear,
        eye_status,
        blink_count
    ):

        score = 100

        # Eyes closed
        if eye_status == "CLOSED":
            score -= 40

        # Low EAR
        if ear < 0.22:
            score -= 20

        # Too many blinks
        if blink_count > 20:
            score -= 15

        score = max(0, min(100, score))

        return score
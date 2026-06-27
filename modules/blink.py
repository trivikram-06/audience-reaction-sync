class BlinkDetector:

    def __init__(self):

        self.counter = 0
        self.blinks = 0
        self.threshold = 0.22

    def update(self, ear):

        status = "OPEN"

        if ear < self.threshold:

            self.counter += 1
            status = "CLOSED"

        else:

            if self.counter >= 2:
                self.blinks += 1

            self.counter = 0

        return status, self.blinks
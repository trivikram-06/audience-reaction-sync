import math

# MediaPipe landmark indices
NOSE = 1
LEFT_EYE = 33
RIGHT_EYE = 263
CHIN = 152


def estimate_head_pose(landmarks):

    nose = landmarks[NOSE]
    left_eye = landmarks[LEFT_EYE]
    right_eye = landmarks[RIGHT_EYE]
    chin = landmarks[CHIN]

    # Approximate yaw
    yaw = (nose.x - (left_eye.x + right_eye.x) / 2) * 180

    # Approximate pitch
    pitch = (chin.y - nose.y) * 180 - 55

    # Approximate roll
    roll = math.degrees(
        math.atan2(
            right_eye.y - left_eye.y,
            right_eye.x - left_eye.x
        )
    )

    return yaw, pitch, roll
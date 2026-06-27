import math


def distance(p1, p2):
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )


def eye_aspect_ratio(landmarks):

    # Left eye landmark indices
    top = landmarks[159]
    bottom = landmarks[145]

    left = landmarks[33]
    right = landmarks[133]

    vertical = distance(top, bottom)
    horizontal = distance(left, right)

    if horizontal == 0:
        return 0

    return vertical / horizontal


def mouth_aspect_ratio(landmarks):

    top = landmarks[13]
    bottom = landmarks[14]

    left = landmarks[78]
    right = landmarks[308]

    vertical = distance(top, bottom)
    horizontal = distance(left, right)

    if horizontal == 0:
        return 0

    return vertical / horizontal
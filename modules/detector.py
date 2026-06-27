from ultralytics import YOLO

# Load model once
model = YOLO("yolo11n.pt")


def detect_people(frame):
    """
    Detect and track people.
    Returns YOLO tracking results.
    """
    results = model.track(
        frame,
        persist=True,
        classes=[0],   # person only
        verbose=False
    )

    return results
import cv2

from modules.detector import detect_people
from modules.landmark import process_face
from modules.features import eye_aspect_ratio, mouth_aspect_ratio
from modules.blink import BlinkDetector
from modules.logger import FeatureLogger

# Initialize modules
blink_detector = BlinkDetector()
logger = FeatureLogger()

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # Detect + Track people
    results = detect_people(frame)

    if (
        len(results) > 0
        and results[0].boxes is not None
        and results[0].boxes.xyxy is not None
    ):

        boxes = results[0].boxes.xyxy.cpu().numpy()

        # Get tracking IDs (if available)
        if results[0].boxes.id is not None:
            ids = results[0].boxes.id.int().cpu().tolist()
        else:
            ids = [1] * len(boxes)

        for box, person_id in zip(boxes, ids):

            x1, y1, x2, y2 = map(int, box)

            # Keep coordinates inside frame
            h, w = frame.shape[:2]

            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(w, x2)
            y2 = min(h, y2)

            crop = frame[y1:y2, x1:x2]

            if crop.size == 0:
                continue

            # Face Mesh
            crop, landmarks = process_face(crop)

            if landmarks:

                # Features
                ear = eye_aspect_ratio(landmarks)
                mar = mouth_aspect_ratio(landmarks)

                # Blink Detection
                eye_status, blink_count = blink_detector.update(ear)

                # Save features to CSV
                logger.log(
                    person_id,
                    ear,
                    mar,
                    eye_status,
                    blink_count
                )

                # Display Tracking ID
                cv2.putText(
                    frame,
                    f"ID: {person_id}",
                    (x1, y1 - 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

                # EAR
                cv2.putText(
                    frame,
                    f"EAR: {ear:.2f}",
                    (x1, y1 - 85),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )

                # MAR
                cv2.putText(
                    frame,
                    f"MAR: {mar:.2f}",
                    (x1, y1 - 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )

                # Eye Status
                cv2.putText(
                    frame,
                    f"Eyes: {eye_status}",
                    (x1, y1 - 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 0),
                    2
                )

                # Blink Count
                cv2.putText(
                    frame,
                    f"Blinks: {blink_count}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 0),
                    2
                )

            # Put processed crop back
            frame[y1:y2, x1:x2] = crop

            # Draw Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

    cv2.imshow("Audience Reaction Sync", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
logger.close()
cap.release()
cv2.destroyAllWindows()
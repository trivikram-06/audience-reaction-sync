import cv2

from modules.detector import detect_people
from modules.landmark import process_face
from modules.features import eye_aspect_ratio, mouth_aspect_ratio
from modules.blink import BlinkDetector
from modules.logger import FeatureLogger
from modules.head_pose import estimate_head_pose
from modules.attention import AttentionEngine
from modules.predictor import Predictor

# ---------------------------------------
# Initialize Modules
# ---------------------------------------
blink_detector = BlinkDetector()
attention_engine = AttentionEngine()
logger = FeatureLogger()
predictor = Predictor()

# ---------------------------------------
# Webcam
# ---------------------------------------
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # ---------------------------------------
    # Detect People
    # ---------------------------------------
    results = detect_people(frame)

    if (
        len(results) > 0
        and results[0].boxes is not None
        and results[0].boxes.xyxy is not None
    ):

        boxes = results[0].boxes.xyxy.cpu().numpy()

        # Tracking IDs
        if results[0].boxes.id is not None:
            ids = results[0].boxes.id.int().cpu().tolist()
        else:
            ids = list(range(1, len(boxes) + 1))

        for box, person_id in zip(boxes, ids):

            x1, y1, x2, y2 = map(int, box)

            h, w = frame.shape[:2]

            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(w, x2)
            y2 = min(h, y2)

            crop = frame[y1:y2, x1:x2]

            if crop.size == 0:
                continue

            # ---------------------------------------
            # Face Mesh
            # ---------------------------------------
            crop, landmarks = process_face(crop)

            if landmarks:

                # ---------------------------------------
                # Feature Extraction
                # ---------------------------------------
                ear = eye_aspect_ratio(landmarks)
                mar = mouth_aspect_ratio(landmarks)

                # Blink Detection
                eye_status, blink_count = blink_detector.update(ear)

                # Head Pose
                yaw, pitch, roll = estimate_head_pose(landmarks)

                # Attention Score
                attention = attention_engine.calculate(
                    ear,
                    eye_status,
                    blink_count
                )

                # AI Engagement Prediction
                engagement = predictor.predict(
                    ear,
                    mar,
                    blink_count,
                    yaw,
                    pitch,
                    roll,
                    attention
                )

                # ---------------------------------------
                # CSV Logging
                # ---------------------------------------
                logger.log(
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
                )

                # ---------------------------------------
                # Draw Bounding Box
                # ---------------------------------------
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # ---------------------------------------
                # Information Panel
                # ---------------------------------------
                info_x = x1
                info_y = max(25, y1 - 220)

                lines = [
                    f"ID : {person_id}",
                    f"EAR : {ear:.2f}",
                    f"MAR : {mar:.2f}",
                    f"Eyes : {eye_status}",
                    f"Blinks : {blink_count}",
                    f"Yaw : {yaw:.1f}",
                    f"Pitch : {pitch:.1f}",
                    f"Roll : {roll:.1f}",
                    f"Attention : {attention}%",
                    f"Engagement : {engagement:.1f}%"
                ]

                colors = [
                    (0, 255, 0),
                    (0, 255, 255),
                    (0, 255, 255),
                    (255, 255, 0),
                    (255, 255, 0),
                    (255, 255, 255),
                    (255, 255, 255),
                    (255, 255, 255),
                    (0, 255, 255),
                    (0, 255, 0)
                ]

                for i, (text, color) in enumerate(zip(lines, colors)):
                    cv2.putText(
                        frame,
                        text,
                        (info_x, info_y + i * 22),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2
                    )

            # Put processed face back
            frame[y1:y2, x1:x2] = crop

    cv2.imshow("Audience Reaction Sync", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ---------------------------------------
# Cleanup
# ---------------------------------------
logger.close()
cap.release()
cv2.destroyAllWindows()
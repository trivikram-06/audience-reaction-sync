import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils


def process_face(face_crop):

    rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    landmarks = None

    if results.multi_face_landmarks:

        for face in results.multi_face_landmarks:

            landmarks = face.landmark

            mp_draw.draw_landmarks(
                face_crop,
                face,
                mp_face_mesh.FACEMESH_TESSELATION
            )

    return face_crop, landmarks
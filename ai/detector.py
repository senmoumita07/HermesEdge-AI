from ultralytics import YOLO
from collections import Counter
import cv2
import os

model = YOLO("yolov8n.pt")


def detect_objects(video_path, callback=None):

    cap = cv2.VideoCapture(video_path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    os.makedirs("runs/detect/predict", exist_ok=True)

    output_path = "runs/detect/predict/output.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    counter = Counter()

    current = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame, verbose=False)

        annotated = results[0].plot()

        out.write(annotated)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                name = model.names[cls]
                counter[name] += 1

        current += 1

        if callback:
            callback(
                current,
                frame_count,
                dict(counter)
            )

    cap.release()
    out.release()

    return dict(counter)
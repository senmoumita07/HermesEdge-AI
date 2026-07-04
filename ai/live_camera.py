from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from ultralytics import YOLO
import av

model = YOLO("yolov8n.pt")

class VideoProcessor(VideoTransformerBase):

    def transform(self, frame):

        img = frame.to_ndarray(format="bgr24")

        results = model(img, verbose=False)

        annotated = results[0].plot()

        return av.VideoFrame.from_ndarray(
            annotated,
            format="bgr24"
        )

def start_camera():
    webrtc_streamer(
        key="hermesedge",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )
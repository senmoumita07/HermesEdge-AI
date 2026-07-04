import os
import glob
import tempfile

import plotly.graph_objects as go
import streamlit as st

from ai.detector import detect_objects
from ai.utils.session import init_session
from ai.live_camera import start_camera
from ai.history import save_history
from ai.style import load_css


st.set_page_config(
    page_title="Live Drive AI",
    page_icon="🚗",
    layout="wide"
)

init_session()
load_css()

progress = st.progress(0)
status = st.empty()
live_metrics = st.container()


c1, c2, c3, c4 = st.columns(4)

c1.success("🟢 AI Online")
c2.info("📡 GPS Connected")
c3.warning("🚗 Vehicle Active")
c4.success("⚡ Edge AI Ready")

st.title("🚗 Live Drive AI")
st.markdown("---")


st.subheader("📹 Live Camera")
start_camera()


uploaded_video = st.file_uploader(
    "Upload Road Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video:

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_file.write(uploaded_video.read())
    temp_file.close()

    st.success("Video Uploaded")
    st.video(temp_file.name)


    if st.button("🚀 Run AI Detection"):

        def update(frame, total, counts):

            progress.progress(frame / total)
            status.info(f"Processing Frame {frame}/{total}")

            with live_metrics:
                c1, c2, c3, c4 = st.columns(4)

                c1.markdown(f"""
                <div style="background:#0f172a;padding:12px;border-radius:10px;text-align:center;color:white;">
                🚗 Cars<br><h2>{counts.get('car',0)}</h2>
                </div>
                """, unsafe_allow_html=True)

                c2.markdown(f"""
                <div style="background:#0f172a;padding:12px;border-radius:10px;text-align:center;color:white;">
                🚶 People<br><h2>{counts.get('person',0)}</h2>
                </div>
                """, unsafe_allow_html=True)

                c3.markdown(f"""
                <div style="background:#0f172a;padding:12px;border-radius:10px;text-align:center;color:white;">
                🏍 Bikes<br><h2>{counts.get('motorcycle',0)}</h2>
                </div>
                """, unsafe_allow_html=True)

                c4.markdown(f"""
                <div style="background:#0f172a;padding:12px;border-radius:10px;text-align:center;color:white;">
                🚛 Trucks<br><h2>{counts.get('truck',0)}</h2>
                </div>
                """, unsafe_allow_html=True)

        result = detect_objects(temp_file.name, callback=update)
        st.success("Detection Finished!")
        st.write(result)

    
        folders = glob.glob("runs/detect/predict*")

        if folders:
            latest = max(folders, key=os.path.getmtime)

            videos = glob.glob(os.path.join(latest, "*.mp4"))

            if videos:
                st.subheader("🎥 AI Processed Video")
                st.video(videos[0])
                st.success("Detection Completed")

     
        car = result.get("car", 0)
        person = result.get("person", 0)
        bike = result.get("motorcycle", 0)
        truck = result.get("truck", 0)
        bus = result.get("bus", 0)
        traffic = result.get("traffic light", 0)

      
        risk_score = (
            person * 15 +
            truck * 20 +
            bike * 10 +
            bus * 12
        )

        if traffic > 10:
            risk_score += 5

        risk_score = min(risk_score, 100)

        if risk_score >= 70:
            risk = "HIGH"
            recommendation = "Brake Immediately"
        elif risk_score >= 35:
            risk = "MEDIUM"
            recommendation = "Reduce Speed"
        else:
            risk = "LOW"
            recommendation = "Safe to Continue"

        safety = 100 - risk_score

        
        st.session_state.cars = car
        st.session_state.persons = person
        st.session_state.bikes = bike
        st.session_state.trucks = truck
        st.session_state.traffic = traffic
        st.session_state.risk = risk
        st.session_state.recommendation = recommendation
        st.session_state.safety = safety

        save_history(car, person, bike, truck, traffic, safety, risk)

        st.markdown("---")

      
        st.subheader("📊 Detection Summary")

        a, b, c, d = st.columns(4)

        a.markdown(f"""<div style="background:#111827;padding:12px;border-radius:10px;color:white;text-align:center;">
        🚗 Cars<br><h2>{car}</h2></div>""", unsafe_allow_html=True)

        b.markdown(f"""<div style="background:#111827;padding:12px;border-radius:10px;color:white;text-align:center;">
        🚶 People<br><h2>{person}</h2></div>""", unsafe_allow_html=True)

        c.markdown(f"""<div style="background:#111827;padding:12px;border-radius:10px;color:white;text-align:center;">
        🏍 Bikes<br><h2>{bike}</h2></div>""", unsafe_allow_html=True)

        d.markdown(f"""<div style="background:#111827;padding:12px;border-radius:10px;color:white;text-align:center;">
        🚛 Trucks<br><h2>{truck}</h2></div>""", unsafe_allow_html=True)

       
        st.subheader("🛡 Safety Score")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=safety,
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#00C8FF"},
                "steps": [
                    {"range": [0, 40], "color": "#ef4444"},
                    {"range": [40, 70], "color": "#f59e0b"},
                    {"range": [70, 100], "color": "#22c55e"}
                ]
            }
        ))

        st.plotly_chart(fig,width="stretch")

       
        st.subheader("🧠 AI Decision")

        if risk == "LOW":
            st.success(recommendation)
        elif risk == "MEDIUM":
            st.warning(recommendation)
        else:
            st.error(recommendation)

        confidence = max(
            80,
            100 - (person * 3 + truck * 2 + bike)
        )

        st.metric("AI Confidence", f"{confidence}%")


st.markdown("---")

st.caption(
"""
HermesEdge AI v1.0

Explainable Predictive Edge Intelligence

Built for Tata Hackathon
"""
)
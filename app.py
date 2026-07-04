import streamlit as st
from ai.utils.session import init_session
from ai.style import load_css

st.set_page_config(
    page_title="HermesEdge AI",
    page_icon="🚗",
    layout="wide"
)

init_session()
load_css()

st.title("🚗 HermesEdge AI")

st.subheader("Explainable Predictive Edge Intelligence for Autonomous Vehicles")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

c1.success("🟢 AI Engine Online")
c2.info("📡 GPS Connected")
c3.warning("🚗 Vehicle Ready")
c4.success("⚡ YOLOv8 Loaded")

st.markdown("---")

st.subheader("🚀 Project Features")

a, b, c = st.columns(3)

with a:
    st.info("""
### 🚗 Live Drive

- Live Camera
- Video Upload
- YOLO Detection
- Real-Time Tracking
""")

with b:
    st.info("""
### 🧠 AI Prediction

- Collision Prediction
- Safety Score
- Risk Analysis
- AI Recommendation
""")

with c:
    st.info("""
### 🌍 Digital Twin

- Virtual Road View
- Live Objects
- Smart Monitoring
- AI Visualization
""")

d, e, f = st.columns(3)

with d:
    st.info("""
### 📊 Analytics

- Charts
- Detection History
- Safety Trend
- Risk Distribution
""")

with e:
    st.info("""
### 🌦 Scenario Simulator

- Rain
- Fog
- Night
- School Zone
""")

with f:
    st.info("""
### 🤖 AI Assistant

- Explain AI
- Driving Tips
- Risk Guidance
- Smart Suggestions
""")

st.markdown("---")


st.subheader("📈 Current AI Status")

m1, m2, m3, m4 = st.columns(4)

m1.metric("🛡 Safety", f"{st.session_state.safety}%")
m2.metric("⚠ Risk", st.session_state.risk)
m3.metric("🚗 Cars", st.session_state.cars)
m4.metric("🚶 People", st.session_state.persons)

m5, m6, m7 = st.columns(3)

m5.metric("🏍 Bikes", st.session_state.bikes)
m6.metric("🚛 Trucks", st.session_state.trucks)
m7.metric("🚦 Traffic", st.session_state.traffic)

st.markdown("---")

st.subheader("⚙ AI Workflow")

st.success("1️⃣ Upload Road Video")
st.success("2️⃣ YOLOv8 Object Detection")
st.success("3️⃣ Object Counting")
st.success("4️⃣ Collision Risk Prediction")
st.success("5️⃣ Digital Twin Visualization")
st.success("6️⃣ Analytics Dashboard")
st.success("7️⃣ AI Recommendation")

st.markdown("---")


st.subheader("🚀 Open Modules")

c1, c2, c3 = st.columns(3)

with c1:
    st.page_link(
        "pages/2_🚗_Live_Drive.py",
        label="🚗 Live Drive"
    )

    st.page_link(
        "pages/3_🧠_AI_Prediction.py",
        label="🧠 AI Prediction"
    )

with c2:
    st.page_link(
        "pages/4_🌍_Digital_Twin.py",
        label="🌍 Digital Twin"
    )

    st.page_link(
        "pages/5_📊_Analytics.py",
        label="📊 Analytics"
    )

with c3:
    st.page_link(
        "pages/6_🌦_Scenario_Simulator.py",
        label="🌦 Scenario Simulator"
    )

    st.page_link(
        "pages/7_🤖_AI_Assistant.py",
        label="🤖 AI Assistant"
    )

st.markdown("---")


st.subheader("🛠 Technology Stack")

t1, t2, t3, t4 = st.columns(4)

t1.success("YOLOv8")
t2.success("OpenCV")
t3.success("Streamlit")
t4.success("Plotly")

st.markdown("---")

st.info(
"""
### 💡 About HermesEdge AI

HermesEdge AI is an Explainable AI platform for autonomous driving.

It performs real-time vehicle detection using YOLOv8,
predicts collision risk, visualizes a Digital Twin,
generates analytics dashboards,
simulates different road scenarios,
and provides AI-powered driving recommendations.
"""
)

st.markdown("---")

st.caption("""
HermesEdge AI v1.0

🚗 Built for Tata Hackathon 2026

Explainable Predictive Edge Intelligence
""")
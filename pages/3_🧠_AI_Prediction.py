import streamlit as st
import plotly.graph_objects as go
from ai.utils.session import init_session

c1,c2,c3,c4 = st.columns(4)

c1.success("🟢 AI Online")
c2.info("📡 GPS Connected")
c3.warning("🚗 Vehicle Active")
c4.success("⚡ Edge AI Ready")
st.set_page_config(
    page_title="AI Prediction",
    page_icon="🧠",
    layout="wide"
)

from ai.style import load_css

init_session()

load_css()

st.title("🧠 AI Prediction Engine")

st.caption("Predictive Intelligence for Autonomous Driving")

st.markdown("---")



collision_probability = max(
    5,
    min(
        95,
        100 - st.session_state.safety
    )
)

left, right = st.columns([1,1])

with left:

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=collision_probability,
        title={"text":"Collision Probability (%)"},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"#38BDF8"},
            "steps":[
                {"range":[0,30],"color":"green"},
                {"range":[30,70],"color":"orange"},
                {"range":[70,100],"color":"red"}
            ]
        }
    ))

    st.plotly_chart(fig,width="stretch")

with right:

    st.subheader("🤖 AI Decision")

    if st.session_state.risk == "HIGH":

        st.error("🛑 Brake Immediately")

    elif st.session_state.risk == "MEDIUM":

        st.warning("⚠ Reduce Speed")

    else:

        st.success("✅ Continue Driving")

st.markdown("---")


st.subheader("⏳ Next 10 Seconds")

timeline=[]

if st.session_state.cars>0:
    timeline.append("1 sec → Vehicle ahead detected")

if st.session_state.persons>0:
    timeline.append("3 sec → Pedestrian may cross")

if st.session_state.trucks>0:
    timeline.append("5 sec → Truck entering lane")

if st.session_state.risk=="HIGH":
    timeline.append("7 sec → Collision probability increases")
    timeline.append("10 sec → Emergency braking advised")

elif st.session_state.risk=="MEDIUM":
    timeline.append("7 sec → Maintain safe distance")
    timeline.append("10 sec → Slow vehicle movement")

else:
    timeline.append("10 sec → Safe route predicted")

for item in timeline:
    st.success(item)

st.markdown("---")


st.subheader("🧠 Explainable AI")

reasons=[]

if st.session_state.persons>0:
    reasons.append(f"🚶 {st.session_state.persons} pedestrian(s) detected")

if st.session_state.cars>0:
    reasons.append(f"🚗 {st.session_state.cars} vehicle(s) nearby")

if st.session_state.bikes>0:
    reasons.append(f"🏍 {st.session_state.bikes} motorcycle(s) nearby")

if st.session_state.trucks>0:
    reasons.append(f"🚛 {st.session_state.trucks} truck(s) nearby")

if st.session_state.traffic>0:
    reasons.append(f"🚦 {st.session_state.traffic} traffic signal(s) detected")

if len(reasons)==0:

    st.success("Road appears clear.")

else:

    for r in reasons:
        st.write(r)

st.info(f"### Final Recommendation\n\n{st.session_state.recommendation}")

st.markdown("---")



confidence=max(
    80,
    100-(
        st.session_state.persons*3+
        st.session_state.trucks*2+
        st.session_state.bikes
    )
)

st.metric("🎯 AI Confidence",f"{confidence}%")

st.markdown("---")

st.caption(
"""
HermesEdge AI v1.0

Explainable Predictive Edge Intelligence

Built for Tata Hackathon
"""
)
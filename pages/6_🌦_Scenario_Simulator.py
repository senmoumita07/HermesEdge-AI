import streamlit as st
import plotly.graph_objects as go
from ai.utils.session import init_session

st.set_page_config(layout="wide")

from ai.style import load_css

init_session()

load_css()

st.title("🌦 Scenario Simulator")

st.markdown("### Simulate different road conditions")

scenario = st.selectbox(
    "Choose Scenario",
    [
        "☀ Sunny",
        "🌧 Rain",
        "🌫 Fog",
        "🌙 Night",
        "🚸 School Zone"
    ]
)

safety = st.session_state.safety
risk = st.session_state.risk
recommendation = st.session_state.recommendation

if scenario == "☀ Sunny":
    safety += 5

elif scenario == "🌧 Rain":
    safety -= 10

elif scenario == "🌫 Fog":
    safety -= 20

elif scenario == "🌙 Night":
    safety -= 15

elif scenario == "🚸 School Zone":
    safety -= 25


safety = max(0, min(100, safety))

if safety >= 70:
    risk = "LOW"
    recommendation = "Continue Driving"

elif safety >= 40:
    risk = "MEDIUM"
    recommendation = "Reduce Speed"

else:
    risk = "HIGH"
    recommendation = "Brake Immediately"

st.markdown("---")

c1,c2,c3=st.columns(3)

c1.metric("Safety Score",f"{safety}%")
c2.metric("Collision Risk",risk)
c3.metric("AI Recommendation",recommendation)

st.markdown("---")

st.subheader("🚗 Live Detection")

c1, c2, c3, c4 = st.columns(4)

c1.metric("🚗 Cars", st.session_state.cars)
c2.metric("🚶 Pedestrians", st.session_state.persons)
c3.metric("🏍 Bikes", st.session_state.bikes)
c4.metric("🚛 Trucks", st.session_state.trucks)

st.markdown("---")

fig=go.Figure(go.Indicator(
    mode="gauge+number",
    value=safety,
    title={"text":"Safety Meter"},
    gauge={
        "axis":{"range":[0,100]},
        "bar":{"color":"cyan"},
        "steps":[
            {"range":[0,40],"color":"red"},
            {"range":[40,70],"color":"orange"},
            {"range":[70,100],"color":"green"}
        ]
    }
))

st.plotly_chart(fig,width="stretch")

st.markdown("---")

st.subheader("🧠 Explainable AI")

if scenario=="☀ Sunny":

    st.success("Excellent visibility")
    st.success("Dry road surface")
    st.success("Low accident probability")

elif scenario=="🌧 Rain":

    st.warning("Road friction reduced")
    st.warning("Stopping distance increased")
    st.warning("Visibility reduced")

elif scenario=="🌫 Fog":

    st.error("Poor visibility")
    st.error("Sensor confidence reduced")
    st.error("High collision probability")

elif scenario=="🌙 Night":

    st.warning("Pedestrian visibility reduced")
    st.warning("Headlight dependency increased")

else:

    st.error("Pedestrian crossing expected")
    st.error("Children movement predicted")
    st.error("Automatic braking recommended")

st.markdown("---")

st.subheader("🤖 AI Decision")

st.write(f"Risk Level : **{risk}**")
st.write(f"Safety Score : **{safety}%**")
st.write(f"Recommendation : **{recommendation}**")

st.write("### Why?")

if st.session_state.persons > 0:
    st.write(f"🚶 {st.session_state.persons} pedestrian(s) detected")

if st.session_state.cars > 0:
    st.write(f"🚗 {st.session_state.cars} vehicle(s) detected")

if st.session_state.trucks > 0:
    st.write(f"🚛 {st.session_state.trucks} truck(s) nearby")

if st.session_state.traffic > 0:
    st.write(f"🚦 {st.session_state.traffic} traffic signal(s) detected")

st.markdown("---")

st.caption("""
HermesEdge AI v1.0

Explainable Predictive Edge Intelligence

Built for Tata Hackathon
""")
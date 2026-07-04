import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

from ai.utils.session import init_session
from ai.history import load_history
from ai.style import load_css

init_session()
load_css()
history = load_history()
c1,c2,c3,c4 = st.columns(4)

c1.success("🟢 AI Online")
c2.info("📡 GPS Connected")
c3.warning("🚗 Vehicle Active")
c4.success("⚡ Edge AI Ready")

st.title("📊 HermesEdge AI Analytics")

st.caption("Real-Time Autonomous Vehicle Statistics")

st.markdown("---")


m1, m2, m3, m4 = st.columns(4)

m1.metric("🚗 Cars", st.session_state.cars)
m2.metric("🚶 Pedestrians", st.session_state.persons)
m3.metric("🏍 Bikes", st.session_state.bikes)
m4.metric("🚛 Trucks", st.session_state.trucks)

st.markdown("---")


left, right = st.columns(2)

with left:

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Cars","People","Bikes","Trucks","Traffic"],
        y=[
            st.session_state.cars,
            st.session_state.persons,
            st.session_state.bikes,
            st.session_state.trucks,
            st.session_state.traffic
        ]
    ))

    fig.update_layout(
        title="Detected Objects",
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white")
    )

    fig.update_layout(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font=dict(color="white")
)

st.plotly_chart(fig,width="stretch")


with right:

    values = [
        st.session_state.cars,
        st.session_state.persons,
        st.session_state.bikes,
        st.session_state.trucks
    ]

    labels = [
        "Cars",
        "Pedestrians",
        "Bikes",
        "Trucks"
    ]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=.55
            )
        ]
    )

    fig.update_layout(
        title="Object Distribution",
        paper_bgcolor="#111827",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


left, right = st.columns([1,1])

with left:

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=st.session_state.safety,

        title={"text":"Safety Score"},

        gauge={
            "axis":{"range":[0,100]},

            "bar":{"color":"#00C8FF"},

            "steps":[
                {"range":[0,40],"color":"red"},
                {"range":[40,70],"color":"orange"},
                {"range":[70,100],"color":"green"}
            ]
        }

    ))

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("🧠 AI Summary")

    st.write(f"🚗 Cars : {st.session_state.cars}")
    st.write(f"🚶 Pedestrians : {st.session_state.persons}")
    st.write(f"🏍 Bikes : {st.session_state.bikes}")
    st.write(f"🚛 Trucks : {st.session_state.trucks}")
    st.write(f"🚦 Traffic Lights : {st.session_state.traffic}")

    st.markdown("---")

    if st.session_state.risk == "HIGH":
        st.error("🔴 High Collision Risk")

    elif st.session_state.risk == "MEDIUM":
        st.warning("🟠 Medium Collision Risk")

    else:
        st.success("🟢 Low Collision Risk")

    st.info(
        f"Recommendation: {st.session_state.recommendation}"
    )

st.markdown("---")


st.subheader("📈 AI Performance")

c1, c2, c3 = st.columns(3)

confidence = max(
    80,
    100 - (
        st.session_state.persons * 3 +
        st.session_state.trucks * 2 +
        st.session_state.bikes
    )
)

c1.metric("🎯 AI Confidence", f"{confidence}%")
c2.metric("🛡 Safety", f"{st.session_state.safety}%")
c3.metric("⚠ Risk", st.session_state.risk)

st.markdown("---")

st.subheader("📋 Detection History")

if not history.empty:

    st.dataframe(
        history,
        use_container_width=True
    )

else:

    st.info("No history available.")

st.markdown("---")

st.subheader("📈 Safety Trend")


if len(history) > 0:

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=history["Time"],
            y=history["Safety"],
            mode="lines+markers",
            name="Safety"
        )
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.subheader("⚠ Risk Distribution")

if len(history) > 0:

    risk_counts = history["Risk"].value_counts()

    fig = go.Figure(
        data=[
            go.Pie(
                labels=risk_counts.index,
                values=risk_counts.values,
                hole=.45
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        font=dict(color="white")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.success("✅ Analytics Updated Successfully")

st.markdown("---")

st.caption(
"""
HermesEdge AI v1.0

Explainable Predictive Edge Intelligence

Built for Tata Hackathon
"""
)
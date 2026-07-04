import streamlit as st
import plotly.graph_objects as go
from ai.utils.session import init_session


c1,c2,c3,c4 = st.columns(4)

c1.success("🟢 AI Online")
c2.info("📡 GPS Connected")
c3.warning("🚗 Vehicle Active")
c4.success("⚡ Edge AI Ready")
st.set_page_config(
    page_title="Digital Twin",
    page_icon="🌍",
    layout="wide"
)

from ai.style import load_css

init_session()

load_css()

st.title("🌍 Digital Twin")

st.caption("Real-Time Autonomous Vehicle Environment")

st.markdown("---")


c1, c2, c3, c4 = st.columns(4)

c1.metric("🚗 Cars", st.session_state.cars)
c2.metric("🚶 Pedestrians", st.session_state.persons)
c3.metric("🏍 Bikes", st.session_state.bikes)
c4.metric("🛡 Safety", f"{st.session_state.safety}%")

st.markdown("---")

left, right = st.columns([2,1])


with left:

    st.subheader("🛣 Road Digital Twin")

    fig = go.Figure()


    fig.add_shape(
        type="rect",
        x0=4,
        y0=0,
        x1=6,
        y1=20,
        fillcolor="#2E2E2E",
        line=dict(color="white")
    )


fig.add_shape(
    type="rect",
    x0=3,
    y0=0,
    x1=7,
    y1=22,
    fillcolor="#202124",
    line=dict(color="white", width=2)
)


for y in range(0,22,2):

    fig.add_shape(
        type="line",
        x0=5,
        y0=y,
        x1=5,
        y1=y+1,
        line=dict(
            color="white",
            width=2,
            dash="dash"
        )
    )

    fig.add_trace(go.Scatter(
        x=[5],
        y=[2],
        mode="markers+text",
        marker=dict(

    size=28,

    color="#00C8FF",

    line=dict(

        color="white",

        width=2
    )
),
        text=["🚗"],
        textposition="top center",
        name="Your Vehicle"
    ))

fig.add_trace(

    go.Scatter(

        x=[5,5,5,5],

        y=[2,5,8,11],

        mode="lines",

        line=dict(

            color="#00C8FF",

            width=4,

            dash="dot"

        ),

        name="Prediction"
    )
)

fig.add_shape(

    type="circle",

    x0=4.3,
    y0=1.2,

    x1=5.7,
    y1=2.8,

    fillcolor="rgba(255,0,0,.15)",

    line=dict(color="red")
)


for i in range(st.session_state.cars):
        fig.add_trace(go.Scatter(
            x=[5],
            y=[5+i*2],
            mode="markers",
            marker=dict(size=16, color="green"),
            name="Car"
        ))

for i in range(st.session_state.persons):

    y=6+i*2

    fig.add_trace(
        go.Scatter(
            x=[3],
            y=[y],
            mode="markers",
            marker=dict(
                size=18,
                color="orange"
            )
        )
    )

    fig.add_shape(
        type="circle",
        x0=2.5,
        y0=y-.5,
        x1=3.5,
        y1=y+.5,
        fillcolor="rgba(255,165,0,.25)",
        line=dict(color="orange")
    )

for i in range(st.session_state.bikes):
        fig.add_trace(go.Scatter(
            x=[7],
            y=[6+i*2],
            mode="markers",
            marker=dict(size=14, color="purple"),
            name="Bike"
        ))

  
for i in range(st.session_state.trucks):
        fig.add_trace(go.Scatter(
            x=[5],
            y=[12+i*2],
            mode="markers",
            marker=dict(size=22, color="red"),
            name="Truck"
        ))

fig.update_layout(
        height=600,
        showlegend=False,
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="white"),
        xaxis=dict(range=[0,10], visible=False),
        yaxis=dict(range=[0,20], visible=False)
    )

st.plotly_chart(fig,width="stretch")

st.markdown("---")

st.subheader("🧠 Explainable AI Decision")

reason=[]

if st.session_state.persons>0:
    reason.append("Pedestrian detected")

if st.session_state.trucks>0:
    reason.append("Heavy vehicle nearby")

if st.session_state.cars>3:
    reason.append("Dense traffic")

if st.session_state.risk=="HIGH":
    reason.append("Collision probability increased")

for r in reason:
    st.write("✔",r)

st.success(
    st.session_state.recommendation
)


with right:

    st.subheader("🤖 AI Status")

    if st.session_state.risk == "HIGH":
        st.error("🔴 HIGH RISK")

    elif st.session_state.risk == "MEDIUM":
        st.warning("🟠 MEDIUM RISK")

    else:
        st.success("🟢 LOW RISK")

    st.metric(
        "Safety Score",
        f"{st.session_state.safety}%"
    )

    st.metric(
        "Recommendation",
        st.session_state.recommendation
    )

st.markdown("---")


st.subheader("🧠 AI Environment Summary")

if st.session_state.cars > 0:
    st.write(f"🚗 {st.session_state.cars} vehicle(s) detected nearby.")

if st.session_state.persons > 0:
    st.write(f"🚶 {st.session_state.persons} pedestrian(s) detected.")

if st.session_state.bikes > 0:
    st.write(f"🏍 {st.session_state.bikes} bike(s) detected.")

if st.session_state.trucks > 0:
    st.write(f"🚛 {st.session_state.trucks} truck(s) detected.")

if st.session_state.traffic > 0:
    st.write(f"🚦 {st.session_state.traffic} traffic signal(s) detected.")

st.success("Digital Twin updated from latest AI detection.")

st.markdown("---")

st.caption(
"""
HermesEdge AI v1.0

Explainable Predictive Edge Intelligence

Built for Tata Hackathon
"""
)
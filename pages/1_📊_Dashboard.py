import streamlit as st
import plotly.graph_objects as go
from ai.utils.session import init_session

c1,c2,c3,c4 = st.columns(4)

c1.success("🟢 AI Online")
c2.info("📡 GPS Connected")
c3.warning("🚗 Vehicle Active")
c4.success("⚡ Edge AI Ready")

st.set_page_config(
    page_title="HermesEdge AI Dashboard",
    page_icon="🚗",
    layout="wide"
)

from ai.style import load_css

init_session()

load_css()

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#050816,#0F172A,#1E293B);
    color:#F8FAFC;
}

/* Main Container */
.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Metric Cards */
div[data-testid="stMetric"]{
    background:#111827;
    border:1px solid #334155;
    border-radius:18px;
    padding:18px;
    box-shadow:0 8px 25px rgba(0,0,0,.35);
    transition:0.3s;
}

div[data-testid="stMetric"]:hover{
    border:1px solid #38BDF8;
    transform:translateY(-4px);
}

/* Buttons */
.stButton>button{
    background:linear-gradient(90deg,#0EA5E9,#38BDF8);
    color:white;
    border:none;
    border-radius:12px;
    font-size:16px;
    font-weight:bold;
    padding:12px;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#0284C7,#0EA5E9);
}

/* Progress */
div[data-testid="stProgressBar"] > div{
    background:#22C55E;
}

/* Headings */
h1{
    color:#FFFFFF;
    font-size:42px;
    font-weight:700;
}

h2{
    color:#38BDF8;
}

h3{
    color:#F8FAFC;
}

/* Success */
div[data-baseweb="notification"]{
    border-radius:12px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0F172A;
}

</style>
""", unsafe_allow_html=True)

st.title("🚗 HermesEdge AI Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.markdown("""
<div style="padding:15px;background:#1E293B;border-radius:12px;color:white;text-align:center;">
🟢 <b>AI Engine Online</b>
</div>
""", unsafe_allow_html=True)
col1.markdown("""
<div style="padding:15px;background:#1E293B;border-radius:12px;color:white;text-align:center;">
📡 <b>GPS Connected</b>
</div>
""", unsafe_allow_html=True)
col1.markdown("""
<div style="padding:15px;background:#1E293B;border-radius:12px;color:white;text-align:center;">
🚗 <b>Vehicle Active</b>
</div>
""", unsafe_allow_html=True)
col1.markdown("""
<div style="padding:15px;background:#1E293B;border-radius:12px;color:white;text-align:center;">
⚡<b>Edge AI Running</b>
</div>
""", unsafe_allow_html=True)

st.caption(
    "Explainable Predictive Edge Intelligence for Autonomous Vehicles"
)

st.progress(st.session_state.safety)

st.caption(
    f"Autonomous Driving Confidence : {st.session_state.safety}%"
)

st.markdown("---")

a,b,c,d = st.columns(4)

a.markdown(f"""
<div style="
background:#0F172A;
padding:18px;
border-radius:12px;
border:1px solid #38BDF8;
text-align:center;
">
<h4 style="color:#94A3B8;">🛡 Safety Score</h4>
<h2 style="color:white;">{st.session_state.safety}%</h2>
</div>
""", unsafe_allow_html=True)

b.markdown(f"""
<div style="
background:#0F172A;
padding:18px;
border-radius:12px;
border:1px solid #38BDF8;
text-align:center;
">
<h4 style="color:#94A3B8;">⚠ Risk</h4>
<h2 style="color:white;">{st.session_state.risk}%</h2>
</div>
""", unsafe_allow_html=True)

c.markdown(f"""
<div style="
background:#0F172A;
padding:18px;
border-radius:12px;
border:1px solid #38BDF8;
text-align:center;
">
<h4 style="color:#94A3B8;">🚗 Cars</h4>
<h2 style="color:white;">{st.session_state.cars}%</h2>
</div>
""", unsafe_allow_html=True)

d.markdown(f"""
<div style="
background:#0F172A;
padding:18px;
border-radius:12px;
border:1px solid #38BDF8;
text-align:center;
">
<h4 style="color:#94A3B8;">🚶 Pedestrians</h4>
<h2 style="color:white;">{st.session_state.safety}%</h2>
</div>
""", unsafe_allow_html=True)

e,f,g = st.columns(3)

e.markdown(f"""
<div style="
background:#0F172A;
padding:18px;
border-radius:12px;
border:1px solid #38BDF8;
text-align:center;
">
<h4 style="color:#94A3B8;">🛵Bikes</h4>
<h2 style="color:white;">{st.session_state.bikes}%</h2>
</div>
""", unsafe_allow_html=True)
f.markdown(f"""
<div style="
background:#0F172A;
padding:18px;
border-radius:12px;
border:1px solid #38BDF8;
text-align:center;
">
<h4 style="color:#94A3B8;">🚚Trucks</h4>
<h2 style="color:white;">{st.session_state.trucks}%</h2>
</div>
""", unsafe_allow_html=True)

g.markdown(f"""
<div style="
background:#0F172A;
padding:18px;
border-radius:12px;
border:1px solid #38BDF8;
text-align:center;
">
<h4 style="color:#94A3B8;">🚦Traffic Lights</h4>
<h2 style="color:white;">{st.session_state.traffic}%</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

left,right = st.columns([2,1])

with left:

    st.subheader("🛡 Safety Gauge")

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=st.session_state.safety,

        title={"text":"Safety Score"},

        gauge={
            "axis":{"range":[0,100]},

            "bar":{"color":"#00C8FF"},

            "steps":[
                {"range":[0,40],"color":"#EF4444"},
                {"range":[40,70],"color":"#F59E0B"},
                {"range":[70,100],"color":"#22C55E"}
            ]
        }

    ))

    fig.update_layout(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font=dict(color="white")
)

st.plotly_chart(fig,width="stretch")

with right:

    st.subheader("🧠 AI Recommendation")

    if st.session_state.risk=="LOW":

        st.success(
            "✅ "+st.session_state.recommendation
        )

    elif st.session_state.risk=="MEDIUM":

        st.warning(
            "⚠ "+st.session_state.recommendation
        )

    else:

        st.error(
            "🛑 "+st.session_state.recommendation
        )

    confidence=max(

        80,

        100-(

            st.session_state.persons*3+

            st.session_state.trucks*2+

            st.session_state.bikes

        )

    )

    st.metric(
        "AI Confidence",
        f"{confidence}%"
    )

st.markdown("---")

left, right = st.columns(2)


with left:

    st.subheader("📅 AI Prediction Timeline")

    timeline = []

    if st.session_state.cars > 0:
        timeline.append("🚗 Vehicle detected ahead")

    if st.session_state.persons > 0:
        timeline.append("🚶 Pedestrian approaching crossing")

    if st.session_state.trucks > 0:
        timeline.append("🚛 Heavy vehicle in adjacent lane")

    if st.session_state.traffic > 0:
        timeline.append("🚦 Traffic signal detected")

    if st.session_state.risk == "HIGH":
        timeline.append("🛑 Collision probability increasing")
        timeline.append("⚠ Emergency braking recommended")

    elif st.session_state.risk == "MEDIUM":
        timeline.append("⚠ Reduce speed")
        timeline.append("➡ Maintain safe distance")

    else:
        timeline.append("✅ Safe driving conditions")

    for item in timeline:
        st.success(item)


with right:

    st.subheader("🧠 Explainable AI")

    reasons = []

    if st.session_state.persons > 0:
        reasons.append(f"🚶 {st.session_state.persons} pedestrian(s) detected")

    if st.session_state.cars > 0:
        reasons.append(f"🚗 {st.session_state.cars} vehicle(s) nearby")

    if st.session_state.trucks > 0:
        reasons.append(f"🚛 {st.session_state.trucks} truck(s) nearby")

    if st.session_state.traffic > 0:
        reasons.append(f"🚦 {st.session_state.traffic} traffic signal(s) detected")

    if len(reasons) == 0:
        st.success("Road looks clear.")
    else:
        for r in reasons:
            st.write(r)

    st.markdown("---")

    st.info(f"### Recommendation\n\n{st.session_state.recommendation}")

st.markdown("---")

st.subheader("⚙ AI System Health")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.progress(100)
    st.caption("YOLO Engine")

with c2:
    st.progress(97)
    st.caption("Prediction Engine")

with c3:
    st.progress(95)
    st.caption("Edge AI")

with c4:
    st.progress(99)
    st.caption("Navigation System")

st.markdown("---")

st.subheader("🚀 Modules")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.page_link(
        "pages/2_🚗_Live_Drive.py",
        label="🚗 Live Drive"
    )

with c2:
    st.page_link(
        "pages/3_🧠_AI_Prediction.py",
        label="🧠 AI Prediction"
    )

with c3:
    st.page_link(
        "pages/4_🌍_Digital_Twin.py",
        label="🌍 Digital Twin"
    )

with c4:
    st.page_link(
        "pages/5_📊_Analytics.py",
        label="📊 Analytics"
    )

st.markdown("---")

st.caption(
"""
HermesEdge AI v1.0

Explainable Predictive Edge Intelligence

Built for Tata Hackathon
"""
)
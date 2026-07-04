import streamlit as st
from ai.utils.session import init_session
from ai.style import load_css

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

init_session()
load_css()

st.title("🤖 HermesEdge AI Assistant")
st.caption("Ask questions about the latest AI detection.")

st.markdown("---")

question = st.text_input(
    "Ask something...",
    placeholder="Example: Why is the risk high?"
)

if question:

    q = question.lower()

    if "risk" in q:

        st.subheader("⚠ Risk Analysis")
        st.write(f"Risk Level : **{st.session_state.risk}**")
        st.write(f"Safety Score : **{st.session_state.safety}%**")
        st.write(f"Recommendation : **{st.session_state.recommendation}**")

    elif "car" in q or "vehicle" in q:

        st.success(f"🚗 Cars detected : {st.session_state.cars}")

    elif "people" in q or "pedestrian" in q:

        st.success(f"🚶 Pedestrians detected : {st.session_state.persons}")

    elif "bike" in q:

        st.success(f"🏍 Bikes detected : {st.session_state.bikes}")

    elif "truck" in q:

        st.success(f"🚛 Trucks detected : {st.session_state.trucks}")

    elif "traffic" in q:

        st.success(f"🚦 Traffic Lights detected : {st.session_state.traffic}")

    elif "safe" in q:

        if st.session_state.risk == "LOW":
            st.success("✅ Road looks safe.")

        elif st.session_state.risk == "MEDIUM":
            st.warning("⚠ Drive carefully and reduce speed.")

        else:
            st.error("🛑 High collision risk detected.")

    elif "summary" in q:

        st.subheader("📋 Detection Summary")

        st.write(f"🚗 Cars : {st.session_state.cars}")
        st.write(f"🚶 Pedestrians : {st.session_state.persons}")
        st.write(f"🏍 Bikes : {st.session_state.bikes}")
        st.write(f"🚛 Trucks : {st.session_state.trucks}")
        st.write(f"🚦 Traffic Lights : {st.session_state.traffic}")
        st.write(f"🛡 Safety : {st.session_state.safety}%")
        st.write(f"⚠ Risk : {st.session_state.risk}")

    else:

        st.info("I can answer questions about:")
        st.write("• Risk")
        st.write("• Safety")
        st.write("• Cars")
        st.write("• Pedestrians")
        st.write("• Bikes")
        st.write("• Trucks")
        st.write("• Traffic")
        st.write("• Summary")

st.markdown("---")

st.caption("""
HermesEdge AI v1.0

Explainable Predictive Edge Intelligence

Built for Tata Hackathon
""")
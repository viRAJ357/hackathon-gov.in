import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AadhaarPulse | UIDAI Analytics",
    layout="wide"
)

st.title("📊 AadhaarPulse – UIDAI Decision Support Dashboard")
st.markdown("""
**Purpose:**  
Unlock societal trends in Aadhaar enrolment, biometric updates, and demographics  
using anonymised UIDAI datasets.
""")

# Sidebar
st.sidebar.header("Upload UIDAI Datasets")

enrol_file = st.sidebar.file_uploader("Aadhaar Enrolment Data", type="csv")
bio_file = st.sidebar.file_uploader("Biometric Update Data", type="csv")
demo_file = st.sidebar.file_uploader("Demographic Data", type="csv")

if enrol_file and bio_file and demo_file:
    enrol = pd.read_csv(enrol_file)
    bio = pd.read_csv(bio_file)
    demo = pd.read_csv(demo_file)

    st.success("✅ All datasets loaded successfully")

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Enrolments", f"{len(enrol):,}")
    col2.metric("Biometric Updates", f"{len(bio):,}")
    col3.metric("Demographic Records", f"{len(demo):,}")

    # Aadhaar Stress Index (ASI)
    asi = round((len(bio) / len(enrol)) * 100, 2)

    st.subheader("⚠️ Aadhaar Stress Index (ASI)")
    st.metric("ASI Score", asi)

    if asi > 50:
        st.error("High operational stress detected – Immediate UIDAI intervention recommended")
    elif asi > 30:
        st.warning("Moderate stress detected – Monitoring required")
    else:
        st.success("System stable")

    # Visualization
    st.subheader("📈 Enrolment Distribution (Top Categories)")
    fig, ax = plt.subplots()
    enrol.iloc[:, 0].value_counts().head(10).plot(kind="bar", ax=ax)
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Policy insights
    st.subheader("🧠 Policy Insights for UIDAI")
    st.markdown("""
- Regions with high biometric updates may require assisted authentication
- Elderly-heavy demographics correlate with higher biometric instability
- Predictive staffing can reduce enrolment-update mismatch
""")

else:
    st.info("⬅ Upload all three datasets to activate the dashboard")

st.markdown("""
---
🔐 **Data Privacy Notice:**  
This application uses only anonymised datasets and does not store, process, or infer any Aadhaar number or personal identity.
""")

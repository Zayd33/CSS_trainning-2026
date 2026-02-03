# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 22:37:02 2026

@author: ATMOSPHERIC SERVICE
"""
import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Professor Naven Chetty - Research Group",
    layout="wide"
)

# --- DATA PREPARATION ---

# Research Group Data (updated with attached info)
group_members_data = pd.DataFrame([
    {"Name": "Richard I. Akomolafe", "Field": "Biomedical and Radiation Physics", "Designation": "PhD"},
    {"Name": "Adeleye A", "Field": "Biomedical and Radiation Physics", "Designation": "PhD"},
    {"Name": "Ilori A", "Field": "Biomedical and Radiation Physics", "Designation": "PhD"},
    {"Name": "Segun O", "Field": "Biomedical and Radiation Physics", "Designation": "PhD"},
    {"Name": "Abdulazeez Y", "Field": "Atmospheric & Computational Physics", "Designation": "PhD"},
    {"Name": "Saheed T", "Field": "Atmospheric & Computational Physics", "Designation": "PhD in View"},
    {"Name": "Abubakar M", "Field": "Biomedical and Radiation Physics", "Designation": "PhD in View"},
    {"Name": "Teliat R", "Field": "Atmospheric & Computational Physics", "Designation": "PhD in View"},
])

# Summary Statistics for Metrics
metrics_data = {
    "Publications": 30,
    "MSc Graduates": 15,
    "PhD Graduates": 7
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Biography", "Research Interests", "Research Group", "Publications & Metrics"]
)

# -------------------- BIOGRAPHY --------------------
if menu == "Biography":
    st.title("Professor Naven Chetty")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Note: Ensure "Prof_Chetty_PICS.png" is in the same folder
        st.image("Prof_Chetty_PICS.png", caption="Professor Naven Chetty")
    
    with col2:
        st.subheader("Professional Summary")
        st.write("PhD: Experimental Physics, University of KwaZulu-Natal")
        st.write("Current Role: College Dean of Teaching and Learning at UKZN")
        st.write("Award: UKZN Distinguished Teacher Award (2017)")
        
        st.info("""
        Professor Chetty is driven by a passion for teaching and enthusiastically enlightens 
        students about the wonders of Physics. He strives to transform teaching and learning 
        within the College of Agriculture, Engineering and Science.
        
        His scientific contributions extend to atmospheric physics and environmental modeling, 
        including applications of wind speed analysis and renewable energy resource assessment. 
        These areas align with ongoing research in mixture Weibull distributions, Monte Carlo 
        simulations, and uncertainty quantification for energy planning in South Africa.
        """)

# -------------------- RESEARCH INTERESTS --------------------
elif menu == "Research Interests":
    st.title("Research Specializations")
    st.write("Professor Chetty's research spans several critical areas of Applied Physics:")
    
    interests = [
        "Applied Physics and Biomedical Optics",
        "Atmospheric Physics and Wind Resource Assessment",
        "Physics Education and Pedagogy",
        "Environmental Physics and Renewable Energy Modeling"
    ]
    
    for item in interests:
        st.markdown(f"- {item}")

# -------------------- RESEARCH GROUP --------------------
elif menu == "Research Group":
    st.title("Research Profiles & Group Members")
    st.write("Below is the current composition of the research group and their respective fields:")
    
    st.table(group_members_data)

# -------------------- PUBLICATIONS & METRICS --------------------
elif menu == "Publications & Metrics":
    st.title("Research Impact")
    
    # Key Metrics Highlights
    m1, m2, m3 = st.columns(3)
    m1.metric("ISI Publications", f"{metrics_data['Publications']}+")
    m2.metric("MSc Graduates", metrics_data['MSc Graduates'])
    m3.metric("PhD Graduates", metrics_data['PhD Graduates'])
    
    st.divider()
    
    st.subheader("Publication Trends")
    st.write("Professor Chetty has published more than 30 papers in ISI rated journals, with strong emphasis on applied physics and atmospheric modeling.")
    
    # Visualizing the graduation impact
    grad_data = pd.DataFrame({
        "Level": ["MSc", "PhD"],
        "Count": [15, 7]
    })
    st.bar_chart(grad_data.set_index("Level"))

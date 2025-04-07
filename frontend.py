import streamlit as st
import requests

st.title("SHL Assessment Recommendation Engine")

query = st.text_input("Enter job role or skill:")

if st.button("Get Recommendations"):
    try:
        res = requests.post("http://127.0.0.1:8000/recommend", json={"query": query})

        if res.status_code == 200:
            data = res.json()
            st.subheader("Recommended Assessments:")
            for rec in data["recommendations"]:
                st.write(f"- {rec}")
        else:
            st.error(f"Server Error: {res.status_code}")
    except Exception as e:
        st.error(f"Failed to connect to backend: {e}")
import streamlit as st
from resume_gpt import improve_resume

st.set_page_config(page_title="ResumeGPT", layout="centered")

st.title("📄 ResumeGPT – Upgrade Your Resume with AI")

resume_text = st.text_area("📝 Paste your resume below:", height=300)

if st.button("🚀 Improve Resume"):
    if resume_text.strip() == "":
        st.warning("Please paste your resume text before clicking improve.")
    else:
        with st.spinner("Improving your resume..."):
            improved = improve_resume(resume_text)
            st.success("✅ Done!")
            st.text_area("✨ Improved Resume:", improved, height=400)

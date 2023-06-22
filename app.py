from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
certificate_file = current_dir / "assets" / "python.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Anish"
PAGE_ICON = ":file_folder:"
NAME = "ANISH NARAYAN"
DESCRIPTION = """
Student at SRMIST || Python Freelancer
"""
EMAIL = "anishnarayan0007@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/anixh23/"
}
PROJECTS = {
    "🏆 DIGITAL ONLINE RESUME USING STREAMLIT - PYTHON"

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
with open(certificate_file, "rb") as pdf_file:
    PDFbyte2 = pdf_file.read()



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Pursuing Computer Science Engineering With Specialisation In Artificial Intelligence and Machine Learning
- ✔️ Completed Python 3.0 Course from CodeAcademy


"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Streamlit, Tkinter),
- ⚜️ Extra Utilities: Canva,Github
- 👾 Designing Expert Using Adobe Illustrator
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
st.download_button(
        label=" 📄 Certficicate Of Completion - Python",
        data=PDFbyte2,
        file_name=certificate_file.name,
        mime="application/octet-stream",
    )

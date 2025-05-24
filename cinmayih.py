import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer
import pandas as pd
from st_social_media_links import SocialMediaIcons
#from st_gsheets_connection import connect
from streamlit_clickable_images import clickable_images
import base64
import os
from PIL import Image, ImageOps, ImageDraw
from io import BytesIO

st.set_page_config(page_title="ChinmayiHiremath", layout="wide", page_icon="👩🏻‍💼")

page_bg_image = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://guelphmarket.com/cdn/shop/files/A_black_image.jpg?v=1683422282&width=3840");
background-size: cover;
background-color: #ffffff10;
backdrop-filter: blur(50px); 
}          

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>"""

st.markdown(page_bg_image, unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
  def make_circle(img_path):
    img = Image.open(img_path).convert("RGBA")
    np_img = Image.new("L", img.size, 0)

    draw = ImageDraw.Draw(np_img)
    draw.ellipse((0, 0) + img.size, fill=255)

    result = ImageOps.fit(img, img.size, centering=(0.5, 0.5))
    result.putalpha(np_img)
    result = result.resize((200, 200))  # Resize for sidebar

    return result

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()
    return img_b64

# Prepare circular image
circular_img = make_circle("Chinmayi_photo-.png")
img_b64 = image_to_base64(circular_img)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_rfmdENT2xohZM6ppko7MWTSgX3HAF9bpyGq--M979WOjBWjEa2DKisQZNMw6anVDpNg&usqp=CAU");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display centered image in sidebar
st.sidebar.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_b64}" width="200" style="border-radius: 50%;">
    </div>
    """,
    unsafe_allow_html=True
    )
st.sidebar.markdown(
"""
<h2 style='text-align: center;'>Chinmayi Hiremath</h2>
<h3 style='text-align: center;'>Devops Engineer</h3>
""",
unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <div style="text-align: center;">
     <a href="mailto:chinmayigh08@gmail.com" target="blank">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width="30" style="margin: 0 10px;">
        </a>
      <a href="https://www.linkedin.com/in/chinmayi-hiremath-8090a6279/?trk=public-profile-join-page" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" style="filter: grayscale(100%) brightness(0); margin: 0 10px;">
        </a>
        <a href="https://github.com/gitcgh" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30" style="margin: 0 10px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
    .option-menu-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 0px;
        padding-top: 10px;
    }
    .nav-link {
        font-size: 14px !important;
        padding: 0.4rem 0.75rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Center the menu using a custom HTML container
st.markdown('<div class="option-menu-container">', unsafe_allow_html=True)

choice = option_menu(
    menu_title=None,
    options=["Home", "Experience", "Projects", "Contact"],
    icons=["house-door", "file-person", "bi bi-file-earmark-code-fill", "telephone-outbound-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)
if choice == "Home":
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("### About Me")
    st.markdown("""DevOps Engineer with expertise in AWS, Docker, Git, and Kubernetes.
    Skilled in building scalable, fault-tolerant systems and automating deployments.
    Focused on streamlining operations through robust CI/CD pipelines and infrastructure as code.
    Passionate about cloud-native technologies and delivering secure, high-performing solutions.""")
    with open("CHINMAYI HIREMATH.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="CHINMAYI HIREMATH.pdf",
            mime="text/pdf"
        )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Education")
        st.markdown("###### 🎓 Bachelor of Science in Computer Science \n– R T E S College, Ranebennuru")
        st.markdown("###### 🎓 Devops Engineer Cource \n– Excelr Solutions, Bangalore")

    with col2:
        st.markdown("#### Certifications") 
        st.markdown("######  📜 Devops Engineer Certification")
        st.markdown("######  📜 Internship Certification from AI Variant")


if choice == "Experience":
   st.markdown("#### Internships")
   st.markdown("##### **Company Name:** AI Variant")
   st.write("""AI Variant is a leading analytics firm that delivers best-in-class products and solutions through a strong foundation in data-driven technologies and cloud-native architecture. 
            With deep expertise in analytics and industry domains, the company enables scalable, secure, and high-performing systems. As a DevOps-focused organization, AI Variant emphasizes continuous integration, automated deployment, and infrastructure as code to streamline delivery pipelines. 
            Its team is highly passionate about solving mission-critical challenges, optimizing development workflows, and ensuring reliability and efficiency across client environments.""")
   st.markdown("###### Click here to know more about [AI Variant](https://aivariant.com/)")
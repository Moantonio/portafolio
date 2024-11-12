import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Config
st.set_page_config(page_title="Moisés Cornetero", page_icon="🤖", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_file = "https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

# Main Introduction Section
with st.container():
    st.subheader("Hello, I'm Moisés Cornetero 👋")
    st.title("Machine Learning Engineer at Marvik")
    st.write(
        """
        A passionate engineer focused on computer vision, natural language processing, and classical machine learning. 
        Currently working as an MLE at Marvik, a fast-growing company leading the implementation of AI solutions with business impact.
        """
    )
    st.write("[Learn more >](https://github.com/jhonatancamasca)")

# About Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write(
            """
            With over 4 years of experience in eCommerce, healthcare, and banking, I specialize in Data Science, ML Engineering, and Data Engineering. My work focuses on computer vision, NLP, and advanced data analytics to solve industry-specific challenges.

            I'm passionate about AI, participating in hackathons, and have won international awards, including an Honorable Mention from NASA.
            """
        )
        st.write("📫 Reach me at: jccamascah@gmail.com")
    with right_column:
        st_lottie(load_lottieurl(lottie_file), height=400)

# Services / Expertise Section
with st.container():
    st.write("---")
    st.header("Expertise and Skills")
    st.write("##")

    # Left Column
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image = Image.open("images/automation.png")  # Adjust image path as needed
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Skills and Tools")
        st.write(
            """
            - Languages & Tools: CSS3, Docker, Git, HTML5, Linux, MySQL, OpenCV, Pandas, PostgreSQL, Python, PyTorch, Scikit-learn, Seaborn, TensorFlow.
            - Hackathons & Competitions:
              - 🏆 1st place - BBVA Hackathon 2020 (BBVA)
              - 🏆 2nd place - Hackathon Creamos Juntos Banco BCP
              - 🏆 3rd place - Hackathon Belcorp 2.0 (Belcorp)
              - 🏆 2nd place - NASA Space Apps Lima Hackathon (NASA)
              - 🏆 NASA Honorable Mention (NASA)
              - 🏆 IBM Champion 2022 & 2023 (IBM)
            """
        )

# Publications Section
with st.container():
    st.write("---")
    st.header("Publications")
    st.write(
        """
        📋 Detection of Pathologies in X-Rays Based on a Deep Learning Framework - CIIS Ulima Congreso Internacional de Ingeniería de Sistemas

        📋 Multi-class Vehicle Detection and Automatic License Plate Recognition based on YOLO in Latin American Context - SIMBig 2020.
        """
    )

# Education Section
with st.container():
    st.write("---")
    st.header("Education")
    st.write(
        """
        🎓 Systems Engineer from Universidad ESAN.

        🎓 Postgraduate in Artificial Intelligence from Pontificia Universidad Católica de Chile.

        🎓 Postgraduate in Computer Vision from Universidad Católica San Pablo.

        🎓 Micromaster in Statistics & Data Science from MIT.
        """
    )

# Contact Section
# Contact Section
with st.container():
    st.write("---")
    st.header("Get in Touch!")
    st.write("##")

    contact_form = f"""
    <form id="contact-form">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="button" onclick="sendEmail()">Send</button>
    </form>
    
    <script src="https://cdn.jsdelivr.net/npm/emailjs-com@2.6.4/dist/email.min.js"></script>
    <script>
        (function(){{
            emailjs.init("YOUR_PUBLIC_KEY"); // Replace with your EmailJS public key
        }})();
        
        function sendEmail() {{
            emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", {{
                name: document.querySelector('input[name="name"]').value,
                email: document.querySelector('input[name="email"]').value,
                message: document.querySelector('textarea[name="message"]').value
            }})
            .then(function(response) {{
                alert("Thank you! Your message has been sent.");
                document.getElementById('contact-form').reset();
            }}, function(error) {{
                alert("Oops! There was an error sending your message.");
            }});
        }}
    </script>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

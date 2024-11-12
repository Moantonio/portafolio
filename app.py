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
    st.title("Systems and computing engineer")
    st.write(
        """
        I am a Systems and Computing Engineer, with a tendency towards New Information Technologies, capable of working in a team.
        With a lot of creativity and initiative, supportive and optimistic, eager to learn, capable of directing and making decisions to generate effectiveness, prepared to work under pressure.
        Experienced in implementing systems and computing projects, and very easy to adapt to jobs.
        """
    )
    st.write("[Learn more >](https://github.com/Moantonio)")

# About Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write(
            """
            With more than 4 years of experience in the public and private sector.
            
            I specialize in the development and implementation of information systems. 
            
            My work focuses on optimizing processes through information systems, analysis and providing solutions that solve specific business challenges.
            """
        )
        st.write("📫 Reach me at: moises.cornetero@gmail.com")
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
            - Languages & Tools: CSS3, Docker, Git, HTML5, Linux, MySQL, PostgreSQL, SQL Server, Python.
            - Software Development
            - IT Service Management
            - IT Project Management
            - Business Process Management.
            - Marketing and E-Commerce
            - Business Management Systems
            """
        )

# Publications Section
with st.container():
    st.write("---")
    st.header("Publications")
    st.write(
        """
        📋   - 2024
        """
    )

# Education Section
with st.container():
    st.write("---")
    st.header("Education")
    st.write(
        """
        🎓 Systems and computing Engineer from USAT - Lambayeque.

        🎓 Diplomado en Gestión Publica - USMP.

        🎓 Certifiación  en ITIL Foundation – IT Service Management - People Cert
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

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_w51pcehl.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# --Header Section--
with st.container():
    st.subheader("Hi, I am Yogesh Kumar:wave:")
    st.title("An Engineer from India")
    st.write("I am passionate about python")
    st.write("[Learn more >](https://www.linkedin.com/in/yogism/)")
    
# --WHAT I DO--
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            - Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            - Sed at tellus at arcu aliquet pretium.
            - Aenean dapibus turpis a eros convallis, at vehicula odio scelerisque.
            - Praesent a sem venenatis, elementum neque quis, iaculis risus.
            - Nunc eu lectus nec turpis porta auctor ac id elit.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
 
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
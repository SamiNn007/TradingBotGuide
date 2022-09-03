import streamlit as st
import requests
from PIL import Image
import time
#from

st.set_page_config(page_title="sam cody fran", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()    

#def local_css(file, w):
    #with open('file', 'w') as f:
       # file.write("C:\Users\Acer\OneDrive\Desktop\Streamlit\style")
        #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#local_css("style\css")

    # load assets
#lottie_coding = load_lottieurl("https://lottiefiles.com/72654-human-group-cycling")
img = Image.open("pictures for web\Croatia.jpg")
img1 = Image.open("pictures for web\England.jpg")
img2 = Image.open("pictures for web\Germany.jpg")
img3 = Image.open("perfectvacay.jpg")

     # HEADER
with st.container():
    st.title("DREAM VACAY :bicyclist: :surfer: :evergreen_tree:" )
    st.subheader("Welcome, to where dreams come true :wave:")
    st.write("")
    st.write("")

    # Benefits
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Offer")
        st.write("##")
        st.write(
            """
            - Fast and easy bookings 
            - Great spots
            - Cheap rooms
            - Available discounts
            - Sporting events 

            """
        )
    with right_column:
        st.image(img3)

with st.container():
    st.write("---")
    st.header("Top Places To Visit")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img)

    with text_column:
        st.subheader("CROATIA") 

    image_column, text_column = st.columns((1, 2))
    

    with image_column:
        st.image(img1)

    with text_column:
        st.subheader("ENGLAND")  

    image_column, text_column = st.columns((1, 2))
      
    
    with image_column:
        st.image(img2)

    with text_column:
        st.subheader("GERMANY")  

with st.container():
    st.write("---")
    st.header("For More Information")
    st.write("##")  

    contact_form ="""
    <form action="https://formsubmit.co/samibolt11@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false"
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
        with st.empty():
            for seconds in range(60):
                st.write(f"⏳ {seconds} seconds have passed") 
                time.sleep(1)
            st.write("✔️ 1 minute over!")   


        
          
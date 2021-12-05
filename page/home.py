import streamlit as st
from PIL import Image

def app():
    logo = Image.open('Avatar.png')
    st.image(logo, width = 200)
    st.markdown('''🏄‍♂️
    "I thrive on creative challenges and enjoy learning new skills. Life is about living with experiences."
        **CC.Chayanin**  ''')



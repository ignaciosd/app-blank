import streamlit as st

st.title("It works !!!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

x = st.text_input('How old are you?')
#print(f'## {x} ... I am that old')
st.write(f'## {x} ... I am that old, you think?')

# How to use the webcam?
#import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.camera_input("Take a picture")
st.write(img_file_buffer.shape)

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)


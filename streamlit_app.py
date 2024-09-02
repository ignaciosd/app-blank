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
import time

img_file_buffer = st.camera_input("Take a picture")
#st.write(img_file_buffer.shape)

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
    st.balloons()

    import streamlit as st
    progress_text = "Calculating Awesomeness..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.progress(percent_complete + 1, text="## AWESOMENESS level -> 100%")
    #my_bar.empty()
    st.snow()
    #st.button("Rerun")

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    #st.write(type(img_array))
    

# LATEX
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# CODE
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")    

# SOUND
st.audio("thp-reagan-bomb-russia.mp3", format="audio/mpeg", loop=True, autoplay=True)



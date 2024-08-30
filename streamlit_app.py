import streamlit as st

st.title("It works !!!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

x = st.text_input('How old are you?')
print(f'## {x} ... I am that old')


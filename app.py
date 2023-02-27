import streamlit as st

st.title(':red[Innomatics] Data App :sunglasses:')

st.header(':blue[Data Science Internship] Feb 2023')

st.subheader('Data Science Intern')


primaryColor="#F63366"
backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

btn_click = st.button('Click Me!')
if btn_click == True:
    st.subheader('Learning Data Science and Python :smile:')

CODE = '''print("Hello World! It's Fun to Learn Programming")'''

st.code(CODE, language = 'python')
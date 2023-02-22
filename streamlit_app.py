#version 1
# st.echo
# Streamlit Version v1.18.0
# Use in a `with` block to draw some code on the app, then execute it.
# Function signature
# st.echo(code_location="above" or "below")
# Whether to show the echoed code before or after the results of the executed code block.

 #import streamlit as st

#with st.echo():
   # st.write('This code will be printed')
    
    
   
import streamlit as st

def get_user_name():
    return 'Vaibhav'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')

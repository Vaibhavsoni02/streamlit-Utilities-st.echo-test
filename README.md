# streamlit-Utilities-st.echo-test
I am learning to use streamlit one step at a time.

st.echo
Streamlit Version
v1.18.0
Use in a `with` block to draw some code on the app, then execute it.
Function signature
st.echo(code_location="above")

Parameters
code_location ("above" or "below")

Whether to show the echoed code before or after the results of the executed code block.

Example
import streamlit as st

with st.echo():
    st.write('This code will be printed')
    
 ![image (1)](https://user-images.githubusercontent.com/93029661/220639631-d5e13580-9417-4c44-907c-0b0cb04b3273.png)
   
Example main 1

import streamlit as st

def get_user_name():
    return 'John'

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

![image (2)](https://user-images.githubusercontent.com/93029661/220643693-9334a037-1f2a-481c-9830-4f737f8b7efc.png)


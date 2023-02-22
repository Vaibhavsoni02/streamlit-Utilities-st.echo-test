#version 1
# st.echo
# Streamlit Version v1.18.0
# Use in a `with` block to draw some code on the app, then execute it.
# Function signature
# st.echo(code_location="above" or "below")
# Whether to show the echoed code before or after the results of the executed code block.

import streamlit as st

def get_user_name():
    return 'Vaibhav'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

    st.write(value, punctuation)
st.write(value, punctuation)
# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

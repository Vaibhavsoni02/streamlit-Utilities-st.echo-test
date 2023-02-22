#version 1
# st.echo
# Streamlit Version v1.18.0
# Use in a `with` block to draw some code on the app, then execute it.
# Function signature
# st.echo(code_location="above" or "below")
# Whether to show the echoed code before or after the results of the executed code block.

import streamlit as st

with st.echo():
    st.write('This code will be printed')

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("Hello2")
st.write("day 3")
st.write("My first stream")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number 50}")

st.title("Title heading")

st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")
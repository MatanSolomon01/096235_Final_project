import streamlit as st

import utils
from utils import helps
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="My kitchen companion", page_icon=":cookie:", layout="wide")

# Sidebar
sdb_header = st.sidebar.header("Menu")
sdb_myzone_btn = st.sidebar.button("My zone", help=helps["sdb_myzone_btn"])
sdb_tut_btn = st.sidebar.button("Tutorial", help=helps["sdb_tut_btn"])
sdb_about_btn = st.sidebar.button("About us", help=helps["sdb_about_btn"])

# Header
st.header(":cookie: My Kitchen Companion")
st.write("---")

# Panels
left_panel, right_panel = st.columns(2)

with right_panel:
    st.write("Choose your flavours!")
    columns = st.columns(4)
    with columns[0]:
        sweet = st.checkbox("Sweet")
    with columns[1]:
        sour = st.checkbox("Sour")
    with columns[2]:
        salty = st.checkbox("Salty")
    with columns[3]:
        bitter = st.checkbox("Bitter")

    st.write('<style>div.row-widget.stRadio div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write('<style>.st-cx{margin-right: auto;}</style>', unsafe_allow_html=True)
    temperature = st.radio("Choose your temperature!", ['Cold', 'Natural', 'Hot'], help=helps["temperature"])

    columns = st.columns(2)
    with columns[0]:
        include = st.multiselect("Ingredients to include", options=("a",), help=helps["include"])
    with columns[1]:
        st.write()
        exclude = st.multiselect("Ingredients to exclude", options=("a",), help=helps["exclude"])

    preparation_time = st.slider("Preparation time", min_value=0, max_value=100, value=50, step=10, format="",
                                 help=helps["preparation_time"])
    healthiness = st.slider("Healthiness", min_value=0, max_value=100, value=50, step=10, format="",
                            help=helps["healthiness"])

with left_panel:
    with st.spinner("Loading a recipe...:cookie:"):
        time.sleep(5)
        if sweet:
            name, ingredients, instructions = utils.get_recipe()
            st.write(f"**{name}**")
            st.write('')
            ingredients = ingredients.split('\n')
            for i in ingredients:
                st.markdown("- " + i)
            st.write('')
            instructions = instructions.split('\n')
            for i, ins in enumerate(instructions):
                st.markdown(f"{i+1}. " + ins)

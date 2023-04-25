import random
import streamlit as st
import numpy as np
import pandas as pd

st.header("Laptop Price Prediction")

st.markdown("""
This app performs the following function;
- Takes laptop feaures like RAM, SIZE, MEMORY
- Perform EDA on the targetted models
- Process and predict the price estimate of the model

            """)

ram_specs = ["4GB", "8GB", '16GB', '64GB']

st.sidebar.header("User Input Features")
selected_ram = st.sidebar.selectbox("RAM: ", ram_specs)

if st.button("Predict Now"):
    st.write("This is a dummy presentation")

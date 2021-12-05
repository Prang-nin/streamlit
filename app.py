
import os
import streamlit as st
import numpy as np

# custom modules
from multipage import multipage
from page import home, dataProfiling, stockApp

# create an instance for multipage class
app = multipage()

# create main page title
st.title("MulTi-APPs PRoJeCT")

# add all page
app.addPage("About me", home.app)
app.addPage("Data Profilling", dataProfiling.app)
app.addPage("Observe stock market", stockApp.app)

# main
app.run()

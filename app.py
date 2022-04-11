import os
import streamlit as st
import numpy as np

# custom modules
from multipage import multipage
from page import home, dataProfiling, stockApp, classification

# create an instance for multipage class
app = multipage()

# create main page title
st.title("Multi-APPs Project")

# add all page
app.addPage("Home page", home.app)
app.addPage("Data Profilling", dataProfiling.app)
app.addPage("Observe stock market", stockApp.app)
app.addPage("Classification Experiments", classification.app)
# main
app.run()

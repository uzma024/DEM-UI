from asyncore import file_dispatcher
import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image
import numpy as np

st.title('Image Super Resolution')

uploaded_file = st.sidebar.file_uploader(label="", type=".tif")

st.subheader("")
st.subheader("Input LR DEM")

st.write(type(uploaded_file))
st.write(uploaded_file)

if uploaded_file is not None:
    

    st.write("filename:", uploaded_file.name)
    image = Image.open(uploaded_file)
    image = np.array(image)
    print(image.shape)
    st.image(image=image)


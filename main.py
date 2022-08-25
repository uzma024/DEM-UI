from asyncore import file_dispatcher
import streamlit as st
import pandas as pd
from io import StringIO
from PIL import Image
import numpy as np
import extra_streamlit_components as stx
import os
import rasterio as rio
# import torch
# import torch.nn as nn
# import torch.functional as F
# import os

# os.environ['KMP_DUPLICATE_LIB_OK']='True'
# def model(im):
#     tensor = torch.tensor(im)
#     upsampled = F.interpolate(im, scale_factor=3, mode='bilinear')
#     return upsampled.numpy()

def normalize(im):
    MIN_H = -500.0
    MAX_H = 10000.0
    return (im - MIN_H)/(MAX_H-MIN_H)

def main_page():
    st.title('Image Super Resolution')

    uploaded_file = st.sidebar.file_uploader(label="", type=".tif")

    st.subheader("")

    # st.write(type(uploaded_file))
    # st.write(uploaded_file)

    if uploaded_file is not None:
        # st.write("filename:", uploaded_file.name)
        st.subheader("Input LR DEM")
        image = normalize(rio.open(uploaded_file).read(1).astype('float'))
        image = np.array(image)
        # out=model(image)
        
        print(image.shape)
        st.image(image=image)
        st.subheader("Output HR DEM")
        # --------------DO SOME COMPUTATION --------------
        print(image.shape)
        st.image(image=image)
        # c1,c2=st.columns(2)
        # with c1:
        #     st.image(image=image)
        # with c2:
        #     st.image(image=image)


def page2():
    # Page 2
    c1,c2,c3,c4=st.columns(4)
    with c1:
        image = os.path.join(os.getcwd(),'images','LR_IMAGE.png')
        # image = Image.open(directory+"")
        if image is not None:
            st.image(image, use_column_width=True)
            st.text("LR IMAGE")
        else:
            st.text("No file uploaded.")
    with c2:
        image = os.path.join(os.getcwd(),'images','Bi_Linear.png')
        if image is not None:
            st.image(image, use_column_width=True)
            st.text("Bi Linear")
        else:
            st.text("No file uploaded.")
    with c3:
        image = os.path.join(os.getcwd(),'images','Our_Result.png')
        if image is not None:
            st.image(image, use_column_width=True)
            st.text("Our Result")
        else:
            st.text("No file uploaded.")
    with c4:
        image = os.path.join(os.getcwd(),'images','SOTA_Model.png')
        if image is not None:
            st.image(image, use_column_width=True)
            st.text("SOTA Model")
        else:
            st.text("No file uploaded.")

    c1,c2,c3=st.columns(3)

    with c2:
        st.markdown("Stats: ")
        st.markdown("* BL vs Our PSNR, BL vs SOTA PSNR") 
        st.markdown("* BL vs Our SSIM, Bl vs SOTA SSIM") 
        st.button("View the generated map in 3d surface model")
        st.button("Get elevation b/w two points")

def page3():
    c1,c2 = st.columns([7,3])

    with c1:
        # geometry_list = st.geom_canvas(img, box = True, polygon = True, point = True, radius = True)
        image = os.path.join(os.getcwd(),'images','Our_Result.png')
        # obj_list = st.canvas_select(image, box = True, polygon = True)

    with c2:
        st.button("Generated image")
        st.button("save this view")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

# @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
# def init_router():
#     return stx.Router({"/home": home, "/landing": landing})

# def home():
#     return st.write("This is a home page")

# def landing():
#     return st.write("This is the landing page")

# router = init_router()
# router.show_route_view()




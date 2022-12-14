import streamlit as st
import numpy as np
import cv2
from  PIL import Image, ImageEnhance
import os
import pathlib
# from streamlit_drawable_canvas import st_canvas




st.title("Super Resolution Digital Elevation Models from low-resolution DEMs")

# directory = pathlib.Path(__file__).parent.resolve()
# print(directory)

col1, col2 = st.columns(2)

# File uploader to allow users to upload photos
with col1: 
    # st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)

    # img_arr = np.array(Image.open(f'Images/{filename}'))
    
    # im = Image.fromarray(img_arr)
    # im = im.convert("L")
    # im.save("Images/gen.jpeg")

    uploaded_file = st.file_uploader(label="", type=[".png",".tif", ".asc"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
        st.text("You uploaded a file!")
        st.button("Generate")
    else:
        st.text("No file uploaded.")

with col2:
    # st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)
    # if st.button("Choose an existing dem to compare results",on_click=lambda: st.text("You clicked the button!")) :
    if st.button("Choose an existing dem to compare results"):
        st.text("Following your request...")
    # else:
    #     st.text("You didn't upload a file.")

# st.file_uploader('Upload a CSV')

# st.markdown("</br>")


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

# Page 3
c1,c2 = st.columns([7,3])

with c1:
    # geometry_list = st.geom_canvas(img, box = True, polygon = True, point = True, radius = True)
    image = os.path.join(os.getcwd(),'images','Our_Result.png')
    # obj_list = st.canvas_select(image, box = True, polygon = True)

with c2:
    st.button("Generated image")
    st.button("save this view")





# streamlit run app.py
# env - cv
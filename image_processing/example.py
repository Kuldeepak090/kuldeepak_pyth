
import streamlit as st
from PIL import Image,ImageFont,ImageDraw


st.title("Image Editor")
upload = st.file_uploader("Upload an image ", type = ["jpg","png"])
if upload is not None:
    image = st.image(upload.read(), use_column_width=True)
    img = Image.open(upload)


    content = st.text_input("add text on image")
    col = st.columns(4)
    fs =    col[0].slider("font size", 1,100,50)
    px =     col[1].slider("position x", 1, 100,50)
    py = col[2].slider("position y ", 1,100,50)

    color = col[3].color_picker("text color")

    btn = st.button("confim to create ")
    if btn and content:
        
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("font.ttf",fs)
        draw.text((px,py), content, color , font = font)
        img.save("edit_image.png")
        st.image("edit_image.png" , use_column_width = True)

        #streamlit run image_processing/example.py
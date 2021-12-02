import streamlit as st
import numpy as np
import cv2
from PIL import Image

#Setting Title of App
st.title("Image Watermarking")
st.markdown("Upload two image")

#Uploading the dog image
Back_image = st.file_uploader("Choose an image to be in background")
Logo_image = st.file_uploader("Choose an image to put on the top of first")
title = st.text_input('Text to put on the image', '')
submit = st.button('create Image')
#On predict button click
if submit:


    if Back_image is not None:

        # Convert the file to an opencv image.
        file_bytes1 = np.asarray(bytearray(Back_image.read()), dtype=np.uint8)
        opencv_back = cv2.imdecode(file_bytes1, 1)
        back = cv2.resize(opencv_back, (500,300))
        h_image = 500
        w_image = 300
        if Logo_image is not None:
            # Convert the file to an opencv image.
            file_bytes2 = np.asarray(bytearray(Logo_image.read()), dtype=np.uint8)
            opencv_logo = cv2.imdecode(file_bytes2, 1)
            logo = cv2.resize(opencv_logo, (100,100))
            h_logo = 100
            w_logo = 100
            # Get the center of the orihinal. It's the location where we will place the watermark
            center_y = int(h_image / 2)
            center_x = int(w_image / 2)
            top_y = center_y - int(h_logo / 2)
            left_x = center_x - int(w_logo / 2)
            bottom_y = top_y + h_logo
            right_x = left_x + w_logo

            # Get ROI
            roi = back[top_y: bottom_y, left_x: right_x]
            # Add the logo to the ROI
            result = cv2.addWeighted(roi, 0.5, logo, 1.5, 0)
            #Drawing
            cv2.line(back, (0, center_y), (left_x, center_y), (0,0,255), 1)
            cv2.line(back, (right_x, center_y), (w_image,center_y),(0,0,255), 1)
            # Replace the ROI on the image
            back[top_y: bottom_y, left_x: right_x] = result
            # Display image
            #st.image(back, channels="BGR")

        if title is not None:
            back = cv2.putText(back, text=' title', org=(w_image - 200, h_image - 10), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,255), thickness=2, lineType= cv2.LINE_4)
        st.image(back, channels="BGR")
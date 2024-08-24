import streamlit as st
import base64
# Function to set Image as Background
def add_local_backgound_image_(image):
with open(image, "rb") as image:
encoded_string = base64.b64encode(image.read())
st.write("Image Courtesy: unplash")
st.markdown(
f"""
<style>
.stApp {{
background-image: url(data:fav
{"png"};base64,{encoded_string.decode()});
background-size: cover
}}
</style>
""",
unsafe_allow_html=True
)
st.write("Background Image")
# Calling Image in function
add_local_backgound_image_('fav.png')

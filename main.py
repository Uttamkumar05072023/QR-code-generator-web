import streamlit as st
import qrcode

st.set_page_config(page_title="QR code generator", layout="wide")
st.balloons()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.title("Generate your QR Code 👩‍💻")
with middle_column:
    st.title("[For more click here](https://uttamkumar05072023.github.io/form-using-html-and-css/)")
with right_column:
    st.title("Code with UK")
st.write("---")

data = st.text_input("Paste/Write here for which you want to generate QR",placeholder="Enter any message any link")
color = st.text_input("Enter color (optional)", placeholder="Enter a color name")
if color == "":
    color = "black"
bg_color = st.text_input("Enter background color (optional)", placeholder="Enter a color name for background")
if bg_color == "":
    bg_color = "white"
button = st.button("Submit")

def QR_code(data, color, bg_color):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=3)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=bg_color)
    img.save("sample.png")

QR_code(data, color, bg_color)

# st.image("sample.png")
left_column, middle_column, right_column = st.columns(3)
with middle_column:
    st.image("sample.png")
    st.download_button(label="Download", data="sample.png", file_name="sample.png")

# st.write("---")
st.divider()

# st.snow()
st.subheader("Feedback form")
st.radio("Give the rating", [1, 2, 3, 4, 5])
st.text_area("Share your experience", placeholder="Tell me how was your experience")
st.button("Share")
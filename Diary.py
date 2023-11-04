from tkinter import Image
import streamlit as st
import pandas as pd
import random
from streamlit_drawable_canvas import st_canvas
import datetime

diary_df = pd.DataFrame(columns=["Date", "Entry"])

if "diary_df" not in st.session_state:
    st.session_state.diary_df = pd.DataFrame(columns=["Date", "Entry"])

st.title("Welcome to your diary 🥳")
st.header("Dear Diary is here to help you journal your day")
#st.balloons()
st.text("Before you begin, tell me, How was your day?")
col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    b1 = st.button('😃')
    msg =''
with col2:
    b2 = st.button('😎')
    msg =''
with col3:
    b3 = st.button('😍')
    msg =''
with col4:
    b4 = st.button('😡')
    msg =''
with col5:
    b5 = st.button('😭')
    msg =''

if b1:
    msg = st.text("Ohh that's great!")
    st.subheader("Let's write it down")
if b2:
    msg = st.text("Party scenes huh!!")
    st.subheader("Give me all the details")
if b3:
    msg = st.text("That's lovelyy")
    st.subheader("Just look at that smile")
if b4:
    msg = st.text("Chill dude, here, have some ice -🧊")
    st.subheader("Let it all out.")
if b5:
    msg = st.text("Everything will be alright, don't give up")
    st.subheader("Writing helps you calm down")

# Initialize entries list if it doesn't exist in the session state
if "entries" not in st.session_state:
    st.session_state.entries = []

# Text input for the user to describe and jot down their day
user_entry = st.text_area("Describe and jot down your day:")

# Button to add the user's entry to the diary
if st.button("Add Entry"):
    # Get the current date and time
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a new entry as a dictionary
    new_entry = {"Date": current_date, "Entry": user_entry}

    # Append the new entry to the list of entries in session state
    st.session_state.entries.append(new_entry)

# Display previous diary entries
st.subheader("Previous Diary Entries:")

# Create a new DataFrame from the list of entries
diary_df = pd.DataFrame(st.session_state.entries)

# Show the updated diary DataFrame
st.write(diary_df)



st.text("Would you like to doodle or draw?: Y/N ")
drawans = st.text_input("Your answer")
if drawans == 'N':
    st.text("OHH that's fine")
elif drawans == 'Y':
    # Specify canvas parameters in application
    drawing_mode = st.sidebar.selectbox("Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform"))

    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
    if drawing_mode == 'point':
        point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
    stroke_color = st.sidebar.color_picker("Stroke color hex: ")
    bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
    bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

    realtime_update = st.sidebar.checkbox("Update in realtime", True)

    

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=Image.open(bg_image) if bg_image else None,
        update_streamlit=realtime_update,
        height=150,
        drawing_mode=drawing_mode,
        point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
        key="canvas",
        )

# Do something interesting with the image data and paths
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data)
    if canvas_result.json_data is not None:
        objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
        for col in objects.select_dtypes(include=['object']).columns:
            objects[col] = objects[col].astype("str")
        st.dataframe(objects)





# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from scipy.spatial.distance import jaccard
from sklearn.preprocessing import Binarizer
from sklearn.metrics import jaccard_score

import random
import string

st.set_page_config(layout="wide")

#dfOriginal = pd.read_csv("dfCleaned.csv")
dfOriginal = pd.read_csv("funda.csv")
pd.set_option("display.max_columns", None)
# print(dfOriginal)


html_str = f"""
        
            <style>
                /* Import fonts from my personal Adobe account and add styling  */
                @import url("https://use.typekit.net/krz0vvn.css");

                #header {{
                    font-family: poppins;
                    font-weight: 500;
                    font-size: 60px;
                    margin-bottom: -2rem;

                    background: rgb(45,225,252);
                    background: linear-gradient(90deg, rgba(45,225,252,1) 0%, rgba(248,9,140,1) 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }}

                #title {{
                    font-family: poppins;
                    font-weight: 500;
                    font-size: 30px;
                    margin-bottom: 0px;
                }}

                #textSmall {{
                    font-family: poppins;
                    font-weight: 500;
                    font-size: 15px;
                    margin: 0px;
                }}

            </style>

            <p id="header">The story of John 🌊🏠</p>
            
            <br />
            <br />

        """ 
st.markdown(html_str, unsafe_allow_html=True)




image_filenames = [
    "13.png",
    "14.png",
    "15.png"
]

# Define the final paragraphs
paragraphs = [
    "John and his parents chose one of the recommended temporary houses. After moving in, they discovered that this house does not fully suit their needs. It is still too small and it hasn't got an elevator for Johns dad.",
    "Over time, you and your parents are quite stressed about this situation. And there is no option to stay in another temporary house. John and his parents start to feel guilty about this situation. They realised that a lot of hassle could be prevented if they took the right preparation measurements.",
    "John starts making a list of everything they need to keep on hand in case of future disasters. Meanwhile, his family does their best to make the small apartment feel like home, but they can't help feeling frustrated and uncomfortable. The experience serves as a harsh lesson for John and his parents and they vow to never be caught unprepared again."
]



# Initialize current_paragraph_index with 0 if it doesn't exist in session state
if "current_index3" not in st.session_state:
    st.session_state.current_index3 = 0

# Define a function to show the next paragraph
def next_paragraph(current_paragraph_index3):
    if current_paragraph_index3 >= len(paragraphs):
        st.write("John starts making a list of everything they need to keep on hand in case of future disasters. Meanwhile, his family does their best to make the small apartment feel like home, but they can't help feeling frustrated and uncomfortable. The experience serves as a harsh lesson for John and his parents and they vow to never be caught unprepared again.")
    else:
        st.write(paragraphs[current_paragraph_index3])


# Define a function to show the next image
def next_image(current_image_index3):
    if current_image_index3 >= len(image_filenames):
        st.write("")
        st.image("15.png", width=400)
    else:
        st.image(image_filenames[current_image_index3], width=400)


# Display the first paragraph and image
# next_paragraph(st.session_state.current_index)
# next_image(st.session_state.current_index)

# Add a button to show the next paragraph and image
if st.button("Next"):
    next_paragraph(st.session_state.current_index3)
    next_image(st.session_state.current_index3)
    st.session_state.current_index3 += 1
    











# # Define the final paragraphs
# paragraphs = [
#     "",
#     "Continue the last part of the story: ➡️",
#     "John and his parents chose one of the recommended temporary houses. After moving in, they discovered that this house does not fully suit their needs. It is still too small and it hasn't got an elevator for Johns dad.",
#     "Over time, you and your parents are quite stressed about this situation. And there is no option to stay in another temporary house. John and his parents start to feel guilty about this situation. They realised that a lot of hassle could be prevented if they took the right preparation measurements.",
#     "John starts making a list of everything they need to keep on hand in case of future disasters. Meanwhile, his family does their best to make the small apartment feel like home, but they can't help feeling frustrated and uncomfortable. The experience serves as a harsh lesson for John and his parents and they vow to never be caught unprepared again."
# ]

# # Initialize current_paragraph_index with 0 if it doesn't exist in session state
# if "current_paragraph_index3" not in st.session_state:
#     st.session_state.current_paragraph_index3 = 0

# # Display the current paragraph
# # st.write(paragraphs[st.session_state.current_paragraph_index2])

# # Add a button to show the next paragraph
# if st.button("Show the last steps of the story"):
#     st.session_state.current_paragraph_index3 += 1
#     if st.session_state.current_paragraph_index3 >= len(paragraphs):
#         st.write("John starts making a list of everything they need to keep on hand in case of future disasters. Meanwhile, his family does their best to make the small apartment feel like home, but they can't help feeling frustrated and uncomfortable. The experience serves as a harsh lesson for John and his parents and they vow to never be caught unprepared again.")
#     else:
#         st.write(paragraphs[st.session_state.current_paragraph_index3])


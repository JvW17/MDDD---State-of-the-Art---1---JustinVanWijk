# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


st.header('Continue with the last part of the story by clicking on the button below:')



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


# Add a button to show the next paragraph and image
if st.button("Next"):
    next_paragraph(st.session_state.current_index3)
    next_image(st.session_state.current_index3)
    st.session_state.current_index3 += 1


# Create empty space underneath the button
with st.container():
   st.write("")
   st.write("")
   st.write("")
   st.write("")


# Add extra checklist questions
st.header('You are almost finished. Take a look at the checklist below and find out what measures you need to take to reduce your risks in the event of flooding:')

with st.expander("Let's take some action for yourself!"):
    question1 = st.radio(
        "1. As you read, floods can rise up to three metres. Are you able to stay dry if this will happen?",
        ('Yes', 'No'))

    if question1 == "Yes":
        st.write("- ✅ Great! Still, take account with the following:")
        st.write("- Don't hide in your attic if you don't have a window. You risk getting stuck if the water keeps rising.")
        st.write("- Hang a (white) sheet out of the window. This way you make it clear where you are.")
        st.write("- Use a whistle to let people know where you are when help is nearby.")
    if question1 == "No":
        st.write("- ⚠️ Take account with the following:")
        st.write("- Check if you can get out via a skylight or ladder.")
        st.write("- Leave your house and go to a dry place nearby.")
    
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")


    question2 = st.radio(
        "2. Are you able to use their toilet in a dry spot?",
        ('Yes', 'No'))

    if question2 == "Yes":
        st.write("- ✅ Great! Still, take account with the following:")
        st.write("- Toilets can overflow due to overloaded pipes. Prevent this by shielding your toilet with a sandbag.")
    if question2 == "No":
        st.write("- ⚠️ Take account with the following:")
        st.write("- Prepare a portable toilet in advance, so that you can always use that one.")
    
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    

    question3 = st.radio(
        "3. Are you able to have enough drinks left to survive for three days?",
        ('Yes', 'No'))

    if question3 == "Yes":
        st.write("- ✅ Great! Still, take account with the following:")
        st.write("- No more water is likely to come out of the tap. Therefore, quickly fill a bucket or your bath with water when water is still flowing.")
        st.write("- Remember to use your available water sparingly.")
    if question3 == "No":
        st.write("- ⚠️ Take account with the following:")
        st.write("- Buy bottles of water for three days, at least three litres per person per day, and store them in a dry, preferably high spot.")
    
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    

    question4 = st.radio(
        "4. Are you able to have enough food left to survive for three days?",
        ('Yes', 'No'))

    if question4 == "Yes":
        st.write("- ✅ Great! Still, take account with the following:")
        st.write("- You can't buy groceries or order food. Your cooker, oven and microwave probably won't work either.")
    if question4 == "No":
        st.write("- ⚠️ Take account with the following:")
        st.write("- Prepare long-lasting food and store them in a dry, preferably high spot.")
        st.write("- Prepare food where reheating is not necessary. For example: peanut butter, canned vegetables and fruit, nuts, beef jerky.")
    
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")



    question5 = st.radio(
        "5. Do you have a sufficient amount of clothing and blankets to stay warm?",
        ('Yes', 'No'))

    if question5 == "Yes":
        st.write("- ✅ Great! Still, take account with the following:")
        st.write("- If you get wet, like your clothing, you get cold really fast.")
        st.write("- If there is no electricity, you also get cold really fast.")
        st.write("- Dry yourself up really well in case you get wet.")
    if question5 == "No":
        st.write("- ⚠️ Take account with the following:")
        st.write("- Prepare blankets, towels, warm cloathing, and rain cloathing. Make sure they are stored in a high and dry place, like a closed and purged up.")
    
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")



    question6 = st.radio(
        "6. Are able to stay in touch with the outside world? Think of friends/family/relatives/neighbours?",
        ('Yes', 'No'))

    if question6 == "Yes":
        st.write("- ✅ Great! Still, take account with the following:")
        st.write("- Use a torch or whisle to communicate in case you cannot use a mobile phone to communicate.")
        st.write("- If you are able to, help others.")
    if question6 == "No":
        st.write("- ⚠️ Take account with the following:")
        st.write("- Prepare a battery-powered radio.")
        st.write("- Prepare a powerbank to charge your (mobile) devices. Store the powerbank in a dry place.")
    
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")



    question7 = st.radio(
        "7. Do you have a sufficient amount of medicine at home for three days?",
        ('Yes', 'No'))

    if question7 == "Yes":
        st.write("- ✅ Great! Still, take account with the following:")
        st.write("- During a flood, you are unlikely to be able to go to a doctor, pharmacy or hospital.")
    if question7 == "No":
        st.write("- ⚠️ Take account with the following:")
        st.write("- Prepare an adequate supply of medicine and hygiene products for your personal use for at least three days.")
        st.write("- Prepare a first-aid kit and make sure that it is within your reach.")
    
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    

    html_str = f"""

        <style>
        .mapInformation {{
            font-family: poppins;
            font-weight: 300;
            font-size: 20px;
            margin-bottom: 0px;
        }}

        #firstLine {{
            margin-top: 30px;
        }}

        .move {{
            font-size: 80px;
            margin: 0;
            line-height: 1;
            margin-bottom: -100px;
        }}

        </style>

        <p class="mapInformation" id="firstLine">❗MAKE A SCREENSHOT OF THE ABOVE AND STICK IT ABOVE YOUR BED❗You will never know when you need it!</p>
        <p class="mapInformation" id="firstLine">This was the story of John. John and his parents hope this story has contributed to a better understanding of how your relationship with your environment affects your risk during a flood.</p>
        <br></br>

    """
    st.markdown(html_str, unsafe_allow_html=True)


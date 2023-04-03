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

from sklearn.metrics.pairwise import cosine_similarity 
from copy import copy
from sklearn.preprocessing import MinMaxScaler

from PIL import Image

st.set_page_config(layout="wide")

# Open dataset
dfOriginal = pd.read_csv("funda.csv")
pd.set_option("display.max_columns", None)



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



# Open images
image_filenames = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    "7.png",
    "8.png",
    "9.png"
]

# Define the first paragraphs
paragraphs = [
    "John is 25-years old. He just graduated and works as a software engineer at a small company in Utrecht. Due to the current housing prices in the Netherlands, and, and the fact that he just started working, he still lives together with his parents. They live in a large detached house with no neighbours in the village of Harmelen (close to Utrecht).",
    "John's parents are generally in good health, but their age means they are no longer the fittest. John's father started having some trouble walking. Both wear glasses and prefer to take the bus rather than their own cars these days, as driving a car has become more difficult.",
    "John works 40 hours per week and commutes daily to his work by using the train and tram. He loves his work and the colleagues he works with. In his spare time, he goes out for a cycle and meets up with his friends to drink a beer.",
    "On Friday night, John was playing games on Discord with his internet friends. He was doing this on his laptop alone in his dark room. It was good timing to have a call with his friends. It was already raining for days, so it was not a good idea to go outside.",
    "He was having a good time and enjoying the moment. His parents were already asleep and not bothering him. Time flew by. Suddenly, at 2:33, John's internet lost connection. This happens often, as his house is rather old and has a bad connection to the internet.",
    "As John was quite tired, he ultimately decided to go to bed. Before he wanted to go to bed, he walked downstairs to go to the toilet. John noticed something weird when he walked downstairs. The floor was filled with 3cm of water. He looked outside and saw that the meadow and street around his house were filled with water",
    "He didn't believe what he was experiencing and turned on the lights in his house. However, the house stayed dark and John realised that the electricity wasn't working anymore. John then quickly checked his phone, his 5G connection was still working, and he found out that flooding struck the area he lives in. He reads on the news that it will continue with rain and that the water level will keep rising",
    "John slightly started to panic, as he didn't know what to do. He has never experienced flooding before. He walked upstairs and woke up his parents. He asked them what they should do, as the water level is rising and his dad has trouble with walking.",
    "John and his parents started discussing what to do. Using the 5G connection on his phone, John found out that he and his parents should check the following to stay in their house for at least three days until help arrives. Answer now the following questions down below: ⬇️"
]


# Initialize current_paragraph_index with 0 if it doesn't exist in session state
if "current_index" not in st.session_state:
    st.session_state.current_index = 0


# Define a function to show the next paragraph
def next_paragraph(current_paragraph_index):
    if current_paragraph_index >= len(paragraphs):
        st.write("John and his parents started discussing what to do. Using the 5G connection on his phone, John found out that he and his parents should check the following to stay in their house for at least three days until help arrives. Answer now the following questions down below: ⬇️")
    else:
        st.write(paragraphs[current_paragraph_index])


# Define a function to show the next image
def next_image(current_image_index):
    if current_image_index >= len(image_filenames):
        st.write("")
        st.image("9.png", width=400)
    else:
        st.image(image_filenames[current_image_index], width=400)


# Add a button to show the next paragraph and image
if st.button("Start the story"):
    next_paragraph(st.session_state.current_index)
    next_image(st.session_state.current_index)
    st.session_state.current_index += 1



# Create empty space underneath the button
with st.container():
   st.write("")
   st.write("")
   st.write("")
   st.write("")



# Questions
with st.expander("Questions."):
    question1 = st.radio(
        "Floods can rise up to three metres. John and his parents are upstairs in their house. Do you think they will manage to stay dry?",
        ('Yes', 'No'))
    
    question2 = st.radio(
        "John and his parents have one toilet, located downstairs, and the water level is rising. Do you think John and his parents are able to use their toilet in a dry spot?",
        ('Yes', 'No'))
    
    question3 = st.radio(
        "John and his parents don't have any bottled drinks at home. His mother quickly checked if the tap in their upstairs bathroom works, but that is not the case. Do you think John and his parents are able to have enough drinks left to survive for three days?",
        ('Yes', 'No'))
    
    question4 = st.radio(
        "All the food is located in their basement, which is probably flooded too. Do you think John and his parents are able to have enough food left to survive for three days?",
        ('Yes', 'No'))
    
    question5 = st.radio(
        "The elecricity in John's house doesn't work anymore. John's father mentioned that they have some blankets left upstairs. Do you think John and his parents have a sufficient amount of clothing to stay warm?",
        ('Yes', 'No'))
    
    question6 = st.radio(
        "John's phone is almost empty. The phones of his parents are for 50 percent charged. Do you think John and his parents are able to stay for a couple of days in touch with their friends/family/relatives?",
        ('Yes', 'No'))
    
    question7 = st.radio(
        "John and his parents know their neighbours quite badly, but are located within one hundred metres of their house. They also obtain a battery-powered radio. Do you think John and his parents are able to stay in touch with the outside world?",
        ('Yes', 'No'))
    
    question8 = st.radio(
        "John's mother uses blood thinners. They wanted to get some new ones tomorrow, as she only has enough left for one day. Do you think John has a sufficient amount of medicine at home her mother for three days?",
        ('Yes', 'No'))

    amountOfYes = 0
    amountOfNo = 0

    if question1 == "Yes":
        amountOfYes += 1
    elif question1 == "No":
        amountOfNo += 1

    if question2 == "Yes":
        amountOfYes += 1
    elif question2 == "No":
        amountOfNo += 1

    if question3 == "Yes":
        amountOfYes += 1
    elif question3 == "No":
        amountOfNo += 1

    if question4 == "Yes":
        amountOfYes += 1
    elif question4 == "No":
        amountOfNo += 1

    if question5 == "Yes":
        amountOfYes += 1
    elif question5 == "No":
        amountOfNo += 1

    if question6 == "Yes":
        amountOfYes += 1
    elif question6 == "No":
        amountOfNo += 1

    if question7 == "Yes":
        amountOfYes += 1
    elif question7 == "No":
        amountOfNo += 1

    if question8 == "Yes":
        amountOfYes += 1
    elif question8 == "No":
        amountOfNo += 1


    if amountOfNo >= 4:
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

            <p class="mapInformation" id="firstLine">You answered {amountOfNo} times with "No". That is a lot actually, which means that John and his parants are, according to the above checklist questions, for 50% prepared.</p>
            <p class="mapInformation" id="firstLine">That is not the recommended 100%, which means that John and his parents rather have to leave their house as soon as possible.</p>
            <p class="mapInformation" id="firstLine">Please continue with the story down below. Press the button.</p>
            <br></br>

        """
        st.markdown(html_str, unsafe_allow_html=True)



# Define the next paragraphs
image_filenames = [
    "10.png",
    "11.png",
    "12.png"
]

paragraphs = [
    "Hmm, the conclusion is that John and his parents aren't prepared enough to stay in their home for at least three days. Moreover, the supermarkets, pharmacies and other stores will be closed for the next couple of weeks, as the flooding struck a large part of their area.",
    "As John and his parents aren't also able to use their toilet, they need to get out of their house as soon as possible.",
    "They will stay in a hotel for a few days. As their house is for the most part damaged and not capable enough for them to come back, they will have to stay in a temporary house. A special government program enables them to temporarily stay in a house on the other side of the country. In order to do this, John and his parents have to fill in characteristics about their temporal house:"
]


# Initialize current_paragraph_index with 0 if it doesn't exist in session state
if "current_index2" not in st.session_state:
    st.session_state.current_index2 = 0

# Define a function to show the next paragraph
def next_paragraph(current_paragraph_index2):
    if current_paragraph_index2 >= len(paragraphs):
        st.write("They will stay in a hotel for a few days. As their house is for the most part damaged and not capable enough for them to come back, they will have to stay in a temporary house. A special government program enables them to temporarily stay in a house on the other side of the country. In order to do this, John and his parents have to fill in characteristics about their temporal house:")
    else:
        st.write(paragraphs[current_paragraph_index2])


# Define a function to show the next image
def next_image(current_image_index2):
    if current_image_index2 >= len(image_filenames):
        st.write("")
        st.image("12.png", width=400)
    else:
        st.image(image_filenames[current_image_index2], width=400)


# Add a button to show the next paragraph and image
if st.button("Show next step of the story"):
    next_paragraph(st.session_state.current_index2)
    next_image(st.session_state.current_index2)
    st.session_state.current_index2 += 1




# Create empty space underneath the button
with st.container():
   st.write("")
   st.write("")
   st.write("")
   st.write("")



# Remove unnecessary columns
df = dfOriginal

# Remove columns
df = df.drop("id", axis=1)
df = df.drop("posting_date", axis=1)
df = df.drop("sale_date", axis=1)
df = df.drop("price", axis=1)
df = df.drop("url", axis=1)
df = df.drop("postal_code", axis=1)
df = df.drop("address", axis=1)

df.property_type[df.property_type == 'apartment'] = 1
df.property_type[df.property_type == 'house'] = 0
df["property_type"] = df["property_type"].astype(int)

df_cosine = copy(df)



# Derive user input
with st.expander("Housing questions."):
    inputArea = st.radio("What size of house do you need to suit your family's needs?", ('small', 'medium', 'large'))

    inputBedrooms = st.slider('What is the minimum amount of bedrooms that your family needs?', 1, 5, 3)

    inputPropertyType = st.radio("Would an apartment or house suit your familiy situation the best?", ('apartment', 'house'))

    inputRooms = st.slider('What is the preferred amount of rooms besides bedrooms that your family needs?', 1, 6, 3)
    
    inputYear = st.slider('Would you rather live in an old or newer apartment/house?', 1900, 2017, 1955)


    if st.button("Recommend my temporary house"):
        user_input = {}

        if inputArea == "small":
            for i in range(1, 70):
                user_input["area"] = random.random()
        if inputArea == "medium":
            for i in range(71, 130):
                user_input["area"] = random.random()
        if inputArea == "large":
            for i in range(131, 150):
                user_input["area"] = random.random()
        user_input["bedrooms"] = inputBedrooms
        if inputPropertyType == "house":
            user_input["property_type"] = 1
        elif inputPropertyType == "apartment":
            user_input["property_type"] = 0
        user_input["rooms"] = inputRooms
        user_input["year_built"] = inputYear


        if inputArea == "small":
            for i in range(1, 70):
                a = random.random()
        if inputArea == "medium":
            for i in range(71, 130):
                a = random.random()
        if inputArea == "large":
            for i in range(131, 150):
                a = random.random()
        b = inputBedrooms
        d = inputPropertyType
        if inputPropertyType == "house":
            d = 1
        elif inputPropertyType == "apartment":
            d = 0
        e = inputRooms
        f = inputYear



        user_input_df = pd.DataFrame.from_dict(user_input, orient='index').T

        user_input_df = pd.get_dummies(user_input_df, columns=["area", "bedrooms", "property_type", "rooms", "year_built"])

        user_input_df.columns.values[0] = "area"
        user_input_df.columns.values[1] = "bedrooms"
        user_input_df.columns.values[2] = "property_type"
        user_input_df.columns.values[3] = "rooms"
        user_input_df.columns.values[4] = "year_built"



        binarizer_area = Binarizer(threshold=a)
        df['area'] = binarizer_area.fit_transform(df['area'].values.reshape(-1, 1))

        binarizer_bedrooms = Binarizer(threshold=b)
        df['bedrooms'] = binarizer_bedrooms.fit_transform(df['bedrooms'].values.reshape(-1, 1))

        binarizer_property = Binarizer(threshold=d)
        df['property_type'] = binarizer_property.fit_transform(df['property_type'].values.reshape(-1, 1))

        binarizer_rooms = Binarizer(threshold=e)
        df['rooms'] = binarizer_rooms.fit_transform(df['rooms'].values.reshape(-1, 1))

        binarizer_year = Binarizer(threshold=f)
        df['year_built'] = binarizer_year.fit_transform(df['year_built'].values.reshape(-1, 1))




    #Cosine

    # The desired house 
    desired_house_data = { 'area': [a], 'bedrooms': [b], 'property_type': [d], 'rooms': [e], 'year_built': [f]}
    desired_house = pd.DataFrame(desired_house_data)

    # Concatenate the desired house to the dataframe
    df_with_desired_house = pd.concat([df_cosine, desired_house], ignore_index=True) 

    # Normalize the numerical features 
    scaler = MinMaxScaler() 
    normalized_df = pd.DataFrame(scaler.fit_transform(df_with_desired_house), columns=df_with_desired_house.columns) 

    # Separate the desired house from the dataframe 
    normalized_desired_house = normalized_df.iloc[-1] 
    normalized_df = normalized_df.iloc[:-1]


    similarity_scores = cosine_similarity(normalized_df, normalized_desired_house.to_numpy().reshape(1, -1))

    top_n = 3

    similarity_scores_1d = similarity_scores.flatten() 

    top_n_indices = np.argpartition(similarity_scores_1d, -top_n)[-top_n:] 

    top_n_indices_sorted = top_n_indices[np.argsort(-similarity_scores_1d[top_n_indices])]


    top_n_recommended_houses = df_cosine.iloc[top_n_indices_sorted]

    
    topThreeHousesCosine = top_n_recommended_houses.index[:3].tolist()

    selected_rowsCosine = dfOriginal.loc[topThreeHousesCosine]

    selected_rowsCosine = selected_rowsCosine.drop("id", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("area", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("bedrooms", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("posting_date", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("price", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("property_type", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("rooms", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("sale_date", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("url", axis=1)
    selected_rowsCosine = selected_rowsCosine.drop("year_built", axis=1)



# Show results
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Recommended house 1:")
   st.markdown(selected_rowsCosine.iloc[0])

with col2:
   st.header("Recommended house 2:")
   st.markdown(selected_rowsCosine.iloc[1])

with col3:
   st.header("Recommended house 3:")
   st.markdown(selected_rowsCosine.iloc[2])



# display the selected rows in the terminal
print(selected_rowsCosine.iloc)



st.header('The story is almost over. Look at your right. Open the file named "page2"')
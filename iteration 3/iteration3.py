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
            <p id="title">You will be following the story of John. John experiences the results of a flood in his hometown. You will see the consequences of insufficient preparation and what consequences that can have.</p>
            
            <br />
            <br />

        """ 
st.markdown(html_str, unsafe_allow_html=True)


st.header('Look at your left. Open the file named "page2"')

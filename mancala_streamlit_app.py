import streamlit as st
import pandas as pd
import numpy as np

from .mancala import *

## Define the game board instance
game = Mancala()


## Create the app title
st.title('Mancala')


## Show the game board
game

## Get the next move
move = st.text_input("Enter your move ('Q' to quit): ")

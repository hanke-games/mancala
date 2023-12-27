import streamlit as st
import pandas as pd
import numpy as np

from mancala import *


## Configure the streamlit page
st.set_page_config(layout="wide")





def attempt_new_move():
    ## Get the next move
    move_num = st.session_state['move_input']

    st.session_state['move_input'] = None

    ## Clear the move text
#    st.session_state['move_input'].value = None
#    st.session_state['move_input'] = st.number_input("Enter your move ('Q' to quit): ", 
#                                                    value=None, 
#                                                    min_value=1, max_value = 13,
#                                                    on_change=attempt_new_move)

    ## Apply the move
    try:
        st.session_state['game_board'].perform_move(move_num)
        st.rerun()
    except:
        pass







## Define the game board instance
if 'game_board' not in st.session_state:
    st.session_state['game_board'] = Kalah(m=6, n=4)

## Define the move input box instance
if 'text_input' not in st.session_state:
    st.session_state['move_input'] = st.number_input("Enter your move ('Q' to quit): ", 
                                                    value=None, 
                                                    min_value=1, max_value = 13,
                                                    on_change=attempt_new_move)



## Create the app title
st.title('Mancala')

## Show the game board
#st.write(st.session_state['game_board'].__repr__())


## Add a cleaner board display
col_list = st.columns(8)
first_col = col_list[0]
last_col = col_list[-1]

with first_col:
    st.write('')
    st.write('')
    st.write('')
    with st.container(border=True):
        st.write('North Player Cradle')
        st.write('  ' + str(st.session_state['game_board'].game_state_list[0]))

with last_col:
    st.write('')
    st.write('')
    st.write('')
    with st.container(border=True):
        st.write('South Player Cradle')
        st.write('  ' + str(st.session_state['game_board'].game_state_list[7]))

for i, col in enumerate(col_list[1:-1]):
    with col:
        ## Define the associated index for each player
        north_index = 14-(i+1)
        south_index = (i+1)

        ## Setup the north player move buttons
        if st.button(str(north_index)):
            st.session_state['game_board'].perform_move(north_index)
#            st.session_state['move_input'] = north_index
            st.rerun()

        ## Write the north and south player stone counts
        with st.container(border=True):
            st.write('  ' + str(st.session_state['game_board'].game_state_list[north_index]))
        st.write('')
        st.write('')
        st.write('')
        with st.container(border=True):
            st.write(str(st.session_state['game_board'].game_state_list[south_index]).center(4))

        ## Set up the south player move buttons
        if st.button(str(south_index)):
            st.session_state['game_board'].perform_move(south_index)
#            st.session_state['move_input'] = south_index
            st.rerun()



## Show the game history
st.write("Game History:")
st.write(st.session_state['game_board'].history_list())




import streamlit as st
import pandas as pd
import numpy as np

from mancala import *



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
st.write(st.session_state['game_board'].__repr__())


## Add a cleaner board display
col_list = st.columns(8)
first_col = col_list[0]
last_col = col_list[-1]

with first_col:
    st.write('')
    st.write('North Player Cradle')
    st.write(str(st.session_state['game_board'].game_state_list[0]))

with last_col:
    st.write('')
    st.write('South Player Cradle')
    st.write(str(st.session_state['game_board'].game_state_list[7]))

for i, col in enumerate(col_list[1:-1]):
    with col:
        st.button(str(14-(i+1)))
        st.write(str(st.session_state['game_board'].game_state_list[14-(i+1)]))
        st.write('')
        st.write('')
        st.write('')
        st.write(str(st.session_state['game_board'].game_state_list[i+1]))
        if st.button(str(i+1)):
            st.session_state['game_board'].perform_move(i+1)
#            st.session_state['move_input'] = i+1
            st.rerun()



## Show the game history
st.write("Game History:")
st.write(st.session_state['game_board'].history_list())




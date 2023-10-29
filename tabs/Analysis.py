import random

import streamlit as st
import pandas as pd
import numpy as np
from tabs.Game import state, re_state_init


def analysis():
    st.write("Probability Graph")
    if len(state['analysis_list']) > 0:
        df = pd.DataFrame(state['analysis_list'])
        st. line_chart(df)
    else:
        st.write("No data yet 😣")
        st.markdown("# ←Please play the game first 🔥")

    st.write("Prediction Graph")
    defaultNum = 100
    if state['counter'] > 1:
        defaultNum = state['counter']
    N = st.number_input("Number of times", 1, 10000, defaultNum, on_change=re_state_init, help="Simulation times")
    guess_data_mt = []
    get_data = 0
    for i in range(1, N):
        if random.random() <= 2/3:
            get_data += 1
            guess_data_mt.append(get_data/i)
        else:
            guess_data_mt.append(get_data/i)

    guess_data_nmt = []
    get_data = 0
    for i in range(1, N):
        if random.random() <= 1/3:
            get_data += 1
            guess_data_nmt.append(get_data/i)
        else:
            guess_data_nmt.append(get_data/i)
    array = np.array([guess_data_mt, guess_data_nmt]).T
    df = pd.DataFrame(array, columns=["Monty Hall", "Not Monty Hall"])
    st.line_chart(df)

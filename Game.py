import random

import streamlit as st
from settings import *

state = st.session_state

def show_image(img_path: list):
    one, two, three = st.columns(3)
    with one:
        st.image(img_path[0], width=200)
    with two:
        st.image(img_path[1], width=200)
    with three:
        st.image(img_path[2], width=200)


def state_init():
    answer = random.randint(0, 2)
    tmp_img_list = [0] * 3
    for i in range(3):
        if i == answer:
            tmp_img_list[i] = DUCK_IMG
        else:
            tmp_img_list[i] = DOOR_OPEN_IMG
    state['disabled'] = False
    state['step'] = 0
    state['counter'] = 0
    state['answer'] = answer
    state['selected'] = None
    state['img_path_list'] = tmp_img_list
    state['win'] = 0
    state['lose'] = 0


def re_state_init():
    answer = random.randint(0, 2)
    tmp_img_list = [0] * 3
    for i in range(3):
        if i == answer:
            tmp_img_list[i] = DUCK_IMG
        else:
            tmp_img_list[i] = DOOR_OPEN_IMG
    state['step'] = -1
    state['answer'] = answer
    state['selected'] = None
    state['img_path_list'] = tmp_img_list
    state['disabled'] = False


def Game():
    if 'counter' not in state:
        state_init()

    button1, button2, button3 = st.columns(3)
    with button1:
        if st.button("Door 1", disabled=state['disabled']):
            state['selected'] = 0
    with button2:
        if st.button("Door 2", disabled=state['disabled']):
            state['selected'] = 1

    with button3:
        if st.button("Door 3", disabled=state['disabled']):
            state['selected'] = 2

    if state['step'] == 0:
        img = [DOOR_IMG] * 3
        show_image(img)
    elif state['step'] == 1:
        img = [DOOR_IMG] * 3
        if state['selected'] == state['answer']:
            a = [0, 1, 2]
            a.remove(state['selected'])
            img[random.choice(a)] = DOOR_OPEN_IMG
        else:
            change = 3 - state['answer'] - state['selected']
            img[change] = DOOR_OPEN_IMG
        show_image(img)
        state['disabled'] = True
    elif state['step'] == 2:
        show_image(state['img_path_list'])
        state['counter'] += 1
        if state['answer'] == state['selected']:
            st.success('You Win!')
            state['win'] += 1
        else:
            st.error('You Lose!')
            state['lose'] += 1
        re_state_init()
        st.button("Restart")

    state['step'] += 1

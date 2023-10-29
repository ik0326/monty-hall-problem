import random

import streamlit as st

DOOR_IMG = "assets/door.png"
DOOR_OPEN_IMG = "assets/open_door.png"
DUCK_IMG = "assets/duck.jpeg"

state = st.session_state

# step1: select a door
# step2: host opens a door
# step3: switch or not
# step4: win or lose

# initの段階でimgはセットしておく。

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
    global state
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


def show_image(img_path: list):
    one, two, three = st.columns(3)
    with one:
        st.image(img_path[0], width=200)
    with two:
        st.image(img_path[1], width=200)
    with three:
        st.image(img_path[2], width=200)
def main():
    if 'counter' not in state:
        state_init()

    game, analisis = st.tabs(["Game", "Analysis"])

    with game:
        st.title("Monty Hall Problem")
        st.write("This is a simple implementation of the Monty Hall Problem.")
        st.write("The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975. It became famous as a question from a reader's letter quoted in Marilyn vos Savant's Ask Marilyn column in Parade magazine in 1990: ")
        st.write("Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, 'Do you want to pick door No. 2?' Is it to your advantage to switch your choice?")
        st.write("The answer is yes, you should switch your choice. The first door has a 1/3 chance of winning, but the second door has a 2/3 chance of winning. Here's a simple python implementation to prove it.")

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

    with analisis:
        st.info("Coming soon")

if __name__ == "__main__":
    main()
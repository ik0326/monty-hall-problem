import streamlit as st

from tabs.Analysis import analysis
from tabs.Game import Game, state
from Description import description, title


# step1: select a door
# step2: host opens a door
# step3: switch or not
# step4: win or lose

def main():
    game_tab, analysis_tab = st.tabs(["Game", "Analysis"])
    with game_tab:
        title()
        description()
        Game()
    with analysis_tab:
        analysis()


if __name__ == "__main__":
    main()

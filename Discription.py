import streamlit as st


def title():
    st.title("Monty Hall Problem")


def description():
    st.write("This is a simple implementation of the Monty Hall Problem.")
    st.write(
        "The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975. It became famous as a question from a reader's letter quoted in Marilyn vos Savant's Ask Marilyn column in Parade magazine in 1990: ")
    st.write(
        "Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, 'Do you want to pick door No. 2?' Is it to your advantage to switch your choice?")
    st.write(
        "The answer is yes, you should switch your choice. The first door has a 1/3 chance of winning, but the second door has a 2/3 chance of winning. Here's a simple python implementation to prove it.")

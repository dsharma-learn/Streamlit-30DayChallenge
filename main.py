import streamlit as st
## print("hello world")
import numpy as np
import altair as alt
import pandas as pd


#########################################
# Day - 01
#########################################
def day_01():
    st.title("Streamlit App - 30 Day Challenge")


#########################################
# Day - 02
#########################################
def day_02():
    st.write('Hello world!')


#########################################
# Day - 03
#########################################
def day_03():
    st.header('st.button')

    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')


#########################################
# Day - 04 - long video from Ken Jee
#########################################


#########################################
# Day - 03
#########################################
def day_05():
    st.header('st.write: Day 05')

    # Example 1

    st.write('Hello, *World!* :sunglasses:')

    # Example 2

    st.write(1234)

    # Example 3

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    st.write(df)

    # Example 4

    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

    # Example 5

    df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
    c = alt.Chart(df2).mark_circle().encode(x='a',
                                            y='b',
                                            size='c',
                                            color='c',
                                            tooltip=['a', 'b', 'c'])
    st.write(c)


######################################################
# MAIN
######################################################

day_05()

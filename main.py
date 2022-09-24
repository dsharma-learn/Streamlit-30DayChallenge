import streamlit as st
## print("hello world")
import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime


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
    st.header('Day 03 - st.button')

    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')


#########################################
# Day - 04 - long video from Ken Jee
#########################################


#########################################
# Day - 05
#########################################
def day_05():
    st.header('Day 05  - st.write ')

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


#########################################
# Day - 08
#########################################
def day_08():

    st.header('Day 08 - st.slider')

    # Example 1:
    st.subheader("Slider")

    age = st.slider("How old are you?", 0, 130, 25)
    st.write("I am ", age, " years old")

    # Example 2:
    st.subheader("Range Slider")
    values = st.slider("Select Range of values: ", 0.0, 100.0, (25.0, 75.0))

    st.write('Values:', values)

    # Example 3

    st.subheader('Range time slider')

    appointment = st.slider("Schedule your appointment:",
                            value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)

    # Example 4

    st.subheader('Datetime slider')

    start_time = st.slider("When do you start?",
                           value=datetime(2020, 1, 1, 9, 30),
                           format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)


#########################################
# Day - 09
#########################################
def day_09():
    st.header('Day 09 - Line chart')

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


######################################################
# MAIN
######################################################
day_09()

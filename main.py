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
    st.title("Day 01 - Streamlit App - 30 Day Challenge - using st.title")


#########################################
# Day - 02
#########################################
def day_02():
    st.write('Day 02 - Hello world! - Using st.write')


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
def day_04():
    st.header("Day 05 - Ken Jee's long video")


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
# Day - 06
#########################################
def day_06():
    st.header("Day 06 - Uploading App to Github")


#########################################
# Day - 07
#########################################
def day_07():
    st.header("Day 07 - Deploying app to Streamlit Cloud")


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


#########################################
# Day - 10
#########################################
def day_10():
    st.header('Day 10 - st.selectbox')

    option = st.selectbox('What is your favorite color?',
                          ('Blue', 'Red', 'Green'))

    st.write('Your favorite color is ', option)


#########################################
# Day - 11
#########################################
def day_11():
    st.header('Day 11 - st.multiselect')

    options = st.multiselect('What are your favorite colors',
                             ['Green', 'Yellow', 'Red', 'Blue'],
                             ['Yellow', 'Red'])

    st.write('You selected:', options)


#########################################
# Day - 12
#########################################
def day_12():
    st.header('Day 12 - TBD')


#########################################
# Day - 13
#########################################
def day_13():
    st.header('Day 13 - TBD')


#########################################
# Day - 14
#########################################
def day_14():
    st.header('Day 14 - TBD')


#########################################
# Day - 15
#########################################
def day_15():
    st.header('Day 15 - TBD')


#########################################
# Day - 16
#########################################
def day_16():
    st.header('Day 16 - TBD')


#########################################
# Day - 17
#########################################
def day_17():
    st.header('Day 17 - TBD')


#########################################
# Day - 18
#########################################
def day_18():
    st.header('Day 18 - TBD')


#########################################
# Day - 19
#########################################
def day_19():
    st.header('Day 19 - TBD')


#########################################
# Day - 20
#########################################
def day_20():
    st.header('Day 20 - TBD')


#########################################
# Day - 21
#########################################
def day_21():
    st.header('Day 21 - TBD')


#########################################
# Day - 22
#########################################
def day_22():
    st.header('Day 22 - TBD')


#########################################
# Day - 23
#########################################
def day_23():
    st.header('Day 23 - TBD')


#########################################
# Day - 24
#########################################
def day_24():
    st.header('Day 24 - TBD')


#########################################
# Day - 25
#########################################
def day_25():
    st.header('Day 25 - TBD')


#########################################
# Day - 26
#########################################
def day_26():
    st.header('Day 26 - TBD')


#########################################
# Day - 27
#########################################
def day_27():
    st.header('Day 27 - TBD')


#########################################
# Day - 28
#########################################
def day_28():
    st.header('Day 28 - TBD')


#########################################
# Day - 29
#########################################
def day_29():
    st.header('Day 29 - TBD')


#########################################
# Day - 30
#########################################
def day_30():
    st.header('Day 30 - TBD')


######################################################
# MAIN
######################################################
num = st.slider("How old are you?", 1, 30, 10)

myfunction = '{}_{:02}'.format("day", num)

st.write("Calling " + myfunction)

locals()[myfunction]()

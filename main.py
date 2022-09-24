import streamlit as st
## print("hello world")
import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime
from streamlit_pandas_profiling import st_profile_report


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
    st.subheader("REMINDER: NESTED BUTTONS WITH CHECKBOXES")

    st.subheader("Example 01 ")

    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

    st.subheader("Example 02 ")
    smile = st.button("Smile")
    cry = st.button("Cry")

    if smile:
        cry = False
        st.write(":smile:")

    if cry:
        smile = False
        st.write(":cry:")


#########################################
# Day - 04 - long video from Ken Jee
#########################################
def day_04():
    st.header("Day 05 - Ken Jee's long video")
    st.subheader("REMINDER: Complete this looong video")


#########################################
# Day - 05
#########################################
def day_05():
    st.header('Day 05  - st.write ')
    st.subheader(
        "REMINDER: Video from KEn Jee - https://docs.streamlit.io/library/api-reference/write-magic/st.write"
    )

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

    # Example 5
    st.subheader('Example 05 - Select slider')
    st.title("Streamlit Select Slider")
    temp_options = ['low', 'medium', 'high']
    temp = st.select_slider("Choose the temperature", options=temp_options)
    st.write("The temperature of this :fire: is ", temp)

    # Example 6
    st.subheader('Example 06 - Double slider')
    slider_range = st.slider("Double ended Slider", value=[100, 400])
    st.info("Our Slider range has type %s " % type(slider_range))
    st.write("Slider Range ", slider_range, slider_range[0], slider_range[1])

    # Example 7
    st.subheader('Example 07 - Non Numeric Double slider')
    rainbow = ['Voilet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
    start_color, end_color = st.select_slider(
        "Select a range of colors from rainbow: ",
        options=rainbow,
        value=('Indigo', 'Orange'))
    st.info("Our Colors have type %s" % type(start_color))

    st.write("you chose: ", start_color, " to ", end_color)


#########################################
# Day - 09
#########################################
def day_09():
    st.header('Day 09 - Line chart')
    st.subheader(
        "REMINDER: https://docs.streamlit.io/library/api-reference/charts/st.altair_chart"
    )

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
    st.header('Day 12 - st.checkbox')

    st.write('What would you like to order?')

    icecream = st.checkbox('Ice cream')
    coffee = st.checkbox('Coffee')
    cola = st.checkbox('Cola')

    if icecream:
        st.write("Great! Here's some more 🍦")

    if coffee:
        st.write("Okay, here's some coffee ☕")

    if cola:
        st.write("Here you go 🥤")


#########################################
# Day - 13
#########################################
def day_13():
    st.header('Day 13 - Gitpod - Cloud IDEs')


#########################################
# Day - 14
#########################################
def day_14():
    st.header('Day 14 - `streamlit_pandas_profiling`')
    st.subheader(
        'REMINDER: CREATING CUSTOM COMPONENTS: https://docs.streamlit.io/library/components/create'
    )

    st.subheader(
        'REMINDER: Component List: https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634'
    )

    df = pd.read_csv(
        'https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv'
    )

    pr = df.profile_report()
    st_profile_report(pr)


#########################################
# Day - 15
#########################################
def day_15():
    st.header('Day 15 - st.latex')

    st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)
         ''')


#########################################
# Day - 16
#########################################
def day_16():
    st.header('Day 16 - Theme Customization ')
    st.title('Customizing the theme of Streamlit apps')

    st.write('Contents of the `.streamlit/config.toml` file of this app')

    st.code("""
    [theme]
    primaryColor="#F39C12"
    backgroundColor="#2E86C1"
    secondaryBackgroundColor="#AED6F1"
    textColor="#FFFFFF"
    font="monospace"
    """)

    number = st.sidebar.slider('Select a number:', 0, 10, 5)
    st.write('Selected number from slider widget is:', number)


#########################################
# Day - 17
#########################################
def day_17():
    st.header('Day 17 - Secrets')
    st.title('st.secrets')
    st.write(st.secrets['message'])


#########################################
# Day - 18
#########################################
def day_18():
    st.header('Day 18 - st.file_uploader')

    st.subheader('Input CSV')
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader('DataFrame')
        st.write(df)
        st.subheader('Descriptive Statistics')
        st.write(df.describe())
    else:
        st.info('☝️ Upload a CSV file')


#########################################
# Day - 19
#########################################
def day_19():
    st.header('Day 19 - App Layout')

    #st.set_page_config(layout="wide")

    st.title('How to layout your Streamlit app')

    with st.expander('About this app'):
        st.write(
            'This app shows the various ways on how you can layout your Streamlit app.'
        )
        st.image(
            'https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png',
            width=250)

    st.sidebar.header('Input')
    user_name = st.sidebar.text_input('What is your name?')
    user_emoji = st.sidebar.selectbox('Choose an emoji',
                                      ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
    user_food = st.sidebar.selectbox(
        'What is your favorite food?',
        ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

    st.header('Output')

    col1, col2, col3 = st.columns(3)

    with col1:
        if user_name != '':
            st.write(f'👋 Hello {user_name}!')
        else:
            st.write('👈  Please enter your **name**!')

    with col2:
        if user_emoji != '':
            st.write(f'{user_emoji} is your favorite **emoji**!')
        else:
            st.write('👈 Please choose an **emoji**!')

    with col3:
        if user_food != '':
            st.write(f'🍴 **{user_food}** is your favorite **food**!')
        else:
            st.write('👈 Please choose your favorite **food**!')


#########################################
# Day - 20
#########################################
def day_20():
    st.header('Day 20 - Tech Twitter Space on What is Streamlit')


#########################################
# Day - 21
#########################################
def day_21():
    st.header('Day 21 - st.progress')
    import time
    with st.expander('About this app'):
        st.write(
            'You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.'
        )

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)

    st.balloons()


#########################################
# Day - 22
#########################################
def day_22():
    st.header('Day 22 - Forms ')

    # Full example of using the with notation
    st.header('1. Example of using `with` notation')
    st.subheader('Coffee machine')

    with st.form('my_form'):
        st.subheader('**Order your coffee**')

        # Input widgets
        coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
        coffee_roast_val = st.selectbox('Coffee roast',
                                        ['Light', 'Medium', 'Dark'])
        brewing_val = st.selectbox(
            'Brewing method',
            ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
        serving_type_val = st.selectbox('Serving format',
                                        ['Hot', 'Iced', 'Frappe'])
        milk_val = st.select_slider('Milk intensity',
                                    ['None', 'Low', 'Medium', 'High'])
        owncup_val = st.checkbox('Bring own cup')

        # Every form must have a submit button
        submitted = st.form_submit_button('Submit')

    if submitted:
        st.markdown(f'''
            ☕ You have ordered:
            - Coffee bean: `{coffee_bean_val}`
            - Coffee roast: `{coffee_roast_val}`
            - Brewing: `{brewing_val}`
            - Serving type: `{serving_type_val}`
            - Milk: `{milk_val}`
            - Bring own cup: `{owncup_val}`
            ''')
    else:
        st.write('☝️ Place your order!')

    # Short example of using an object notation
    st.header('2. Example of object notation')

    form = st.form('my_form_2')
    selected_val = form.slider('Select a value')
    form.form_submit_button('Submit')

    st.write('Selected value: ', selected_val)


#########################################
# Day - 23
#########################################
def day_23():
    st.header('Day 23 - st.experimental_get_query_params')

    with st.expander('About this app'):
        st.write(
            "`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser."
        )

    # 1. Instructions
    st.header('1. Instructions')
    st.markdown('''
    In the above URL bar of your internet browser, append the following:
    `?name=Jack&surname=Beanstalk`
    after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
    such that it becomes 
    `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
    ''')

    # 2. Contents of st.experimental_get_query_params
    st.header('2. Contents of st.experimental_get_query_params')
    st.write(st.experimental_get_query_params())

    # 3. Retrieving and displaying information from the URL
    st.header('3. Retrieving and displaying information from the URL')

    firstname = st.experimental_get_query_params()['firstname'][0]
    surname = st.experimental_get_query_params()['surname'][0]

    st.write(f'Hello **{firstname} {surname}**, how are you?')


#########################################
# Day - 24
#########################################
def day_24():
    st.header('Day 24 - Caching')

    st.title('st.cache')

    # Using cache
    a0 = time()
    st.subheader('Using st.cache')

    @st.cache(suppress_st_warning=True)
    def load_data_a():
        df = pd.DataFrame(np.random.rand(2000000, 5),
                          columns=['a', 'b', 'c', 'd', 'e'])
        return df

    st.write(load_data_a())
    a1 = time()
    st.info(a1 - a0)

    # Not using cache
    b0 = time()
    st.subheader('Not using st.cache')

    def load_data_b():
        df = pd.DataFrame(np.random.rand(2000000, 5),
                          columns=['a', 'b', 'c', 'd', 'e'])
        return df

    st.write(load_data_b())
    b1 = time()
    st.info(b1 - b0)


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
num = st.slider("Pick the day ... ", 1, 30, 10)

myfunction = '{}_{:02}'.format("day", num)

st.write("Calling " + myfunction)

locals()[myfunction]()

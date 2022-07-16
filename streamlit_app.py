import streamlit

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.title('Omega 3 & Blueberry Oatmeal')
streamlit.title('Kale, Spinach & Rocket Smoothie ')
streamlit.title('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

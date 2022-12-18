# SETUP

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from pathlib import Path

home_path = str(Path.home())

# IMPORT DATA

df = pd.read_csv('https://raw.githubusercontent.com/nelealyssa/homework-1/main/data/external/data.csv')


# HEADER
st.header('Group L: Dashboard')

# Title of our app
st.title("Task 5: Streamlit")

st.dataframe(df)


# BODY
st.write("Visualisierung 1: Bar Chart Altair")

c = alt.Chart(df).mark_bar().encode(
        x=alt.X('What is your gender?',
               sort='-y'), 
        y=alt.Y('count(What is your gender?)')
)
st.altair_chart(c, use_container_width=True)


st.write("Visualisierung 2: Dodged Bar Chart Altair")

c = alt.Chart(df).mark_bar().encode(
    x=alt.X('Age', 
            sort = '-y', 
            axis=alt.Axis(titleAnchor="start", 
                          labelAngle=0)),
    y=alt.Y('count(Age)', 
            axis=alt.Axis(title = "Count", 
                          titleAnchor="start")),
    color=alt.Color('Do you typically check a daily weather report?', 
                    sort="descending", 
                    legend=alt.Legend(title="Type"))
).properties(
    title='Do you typically check a daily weather report?',
    width=500,
    height=350
).configure_title(
    fontSize=16,
    font='Arial',
    anchor='start',
)
st.altair_chart(c, use_container_width=True)


st.write("Visualisierung 3: Scatterplot Paired Data Altair (interactive)")

c = alt.Chart(df).mark_circle(size=70).encode( 
    x=alt.X('US Region', 
            title='US Region'),
    y=alt.Y('Age', 
            title='Age'),
    tooltip=['US Region', 'Age'],
    color= alt.Color('count(US Region)',
                     legend=alt.Legend(title="count"))
).interactive()

st.altair_chart(c, use_container_width=True)


st.write("Visualisierung 4: Pie Chart Altair")

c = chart = alt.Chart(source).encode(
    theta=alt.Theta("value:Q", stack=True), 
    color=alt.Color("category:N", legend=None)
).properties(
    title='If you had a smartwatch (like the soon to be released Apple Watch), how likely or unlikely would you be to check the weather on that device?',
    width=500,
    height=350
)
pie = chart.mark_arc(outerRadius=130)
text = chart.mark_text(radius=165, size=10).encode(text="category:N")

pie + text 

st.altair_chart(c, use_container_width=True)
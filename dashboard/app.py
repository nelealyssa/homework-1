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
st.header('Group L')

# Title of our app
st.title("Task 5: Dashboard")

st.dataframe(df)

# BODY 1
st.write("Visualisierung 1: Bar Chart Altair")

c = alt.Chart(df).mark_bar().encode(
        x=alt.X('What is your gender?',
               sort='-y'), 
        y=alt.Y('count(What is your gender?)')
)
st.altair_chart(c, use_container_width=True)

# Body 2
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

# Body 3
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

# Body 4
st.write("Visualisierung 4: Pie Chart Altair")

#Spalte umbenennen
df["smartwatch"] = df["If you had a smartwatch (like the soon to be released Apple Watch), how likely or unlikely would you be to check the weather on that device?"] 

# Data Format von Objekt in Kategorie ändern 
df['smartwatch'].astype("category")

# create data for pie chart
source = pd.DataFrame(df.smartwatch.value_counts())

# set index to column
source = source.reset_index()

# rename columns
source.rename(columns={"index": "category", "smartwatch": "value"}, inplace=True)

c = chart = alt.Chart(source).encode(
    theta=alt.Theta(field="value", type="quantitative"), 
    color=alt.Color('category',
                    legend=alt.Legend(title="Answers"))
     
).properties(
    title='If you had a smartwatch, how likely or unlikely would you be to check the weather on that device?',
    width=735,
    height=350
)
pie = chart.mark_arc()

pie
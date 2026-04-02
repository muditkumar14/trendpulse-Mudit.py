import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")

st.sidebar.title("Filters")
st.sidebar.markdown('---')

day_filter= st.sidebar.multiselect(
    "Day of the week:",
    options=df['day'].unique().tolist(),
    default=df['day'].unique().tolist()[0],
)
time_filter= st.sidebar.radio(
    "Meal time:",
    options=["Lunch","Dinner"]
    #default=df['day'].unique().tolist()[0],
)

st.title("Tips Dashboard")
df_filtered=df[df['day'].isin(day_filter)]
df_filtered=df_filtered[df_filtered['time']==time_filter]


st.write(df_filtered)

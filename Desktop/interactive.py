import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")
st.subheader("Generate Report")

if st.button("Run Analysis"):
    st.write("Here's the Tips data 5 Rows")
    st.write(df.head())
    st.dataframe(df.describe())
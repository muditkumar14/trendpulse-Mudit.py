import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("tips")
st.header("Tips Data Sample")
st.write(df.head())
#st.dataframe(df.head())
#st.table(df.head())
fig,ax= plt.subplots(figsize=(8,4))
sns.boxplot(data=df,x='day',y='total_bill',ax=ax)
ax.set_xlabel("Day of the Week")
ax.set_ylabel("Total Bill($)")

st.pyplot(fig)
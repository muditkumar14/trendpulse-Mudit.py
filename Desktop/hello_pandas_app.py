import streamlit as st
import pandas as pd

st.title("My First Dashboard")
st.header("Header block")
st.write("A plain string")
st.write(7)
st.write({"key":"Value"})
st.write(pd.DataFrame({"col":[1,2,3]}))
st.text("Fixed width text")

st.caption("Small Caption")
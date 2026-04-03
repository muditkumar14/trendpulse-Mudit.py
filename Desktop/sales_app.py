import streamlit as st
import pandas as pd

st.title("Company Sales App")
st.subheader("This contain sales information of the company")
df=pd.DataFrame({
    "Product":["A","B","C","D","E"],
    'Category':["V","W","X","Y","Z"],
    "Sales":[100,200,300,400,500]
})

st.sidebar.title("Sales Filters")
st.sidebar.markdown('---')
selected_input=st.sidebar.selectbox("Select a Category",options=df['Category'])
output=df[df['Category']==selected_input]
st.dataframe(output)
st.line_chart(output.set_index('Product')['Sales'])

import streamlit as st
import predict
import eda_m2

navigation =st.sidebar.selectbox('Pilih Halaman: ',('EDA','Predict Diabetes'))

if navigation == "EDA": 
    eda_m2.run()
else:
    predict.run()
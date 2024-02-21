import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
page_title = 'Diabetes Dataset',
layout = 'wide',
initial_sidebar_state = 'expanded'
)

def run():
    st.title('Exploratory Data Analysis of Diabetes')

    '''
    Exploratory data analysis will be conducted to the said dataset at this file
    '''

    #Create Straight line
    st.markdown('---')
    #show dataframe
    df1 = pd.read_csv('diabetes_prediction_dataset.csv')
    st.dataframe(df1)

    #show figures

    st.write('### Amount of people with diabetes or not with heart disease ')
    fig = plt.figure(figsize = (15,5))
    sns.countplot(x = 'heart_disease', data = df1, hue = 'diabetes')
    st.pyplot(fig)

    st.write('### Gender of people with diabetes or not')
    fig = plt.figure(figsize = (15,5))
    sns.countplot(x = 'gender', data = df1, hue = 'diabetes')
    st.pyplot(fig)


if __name__ == '__main__':
    run()
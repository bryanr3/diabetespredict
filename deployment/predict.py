import pickle
import json
import pandas as pd
import numpy as np
import streamlit as st

with open('best_dt.pkl', 'rb') as file_1:
    best_dt = pickle.load(file_1)
with open('n_col.txt','r') as file_4:
 n_col = json.load(file_4)
with open('c_col.txt', 'r') as file_5:
 c_col = json.load(file_5)
with open('nc_col.txt', 'r') as file_6:
 nc_col = json.load(file_6)

def run():
  
    with st.form(key = 'diabetes_predict'): 
        gender = st.radio('Gender =', ['Male','Female'],index = None)
        age = st.number_input('Age =', min_value = 0, max_value = 100, value = None, step = 1, help = 'Your Age')
        ht = st.slider('Hypertension = ',min_value = 0,max_value = 1, help = '0 = No, 1 = Yes')
        hd = st.slider('Heart Disease = ',min_value = 0,max_value = 1, help = '0 = No, 1 = Yes')
        smoke = st.radio('Smoking History = ',['not current','former','No Info','current','never','ever'], index = None)
        bmi_category = st.radio('Your BMI Category = ',['underweight','normal','overweight','obese'], index = None, help = 'Underweight = BMI Below 18.5, normal = BMI: 18.5-24.9, overweight = BMI: 25-29.9, obese = BMI is 30 and above')
        hba1c = st.number_input('HbA1c', min_value = 0.00, max_value = 100.00, value = None,step =1e-2,format="%.2f", help ='Your HbA1c levels')
        bgc = st.number_input('blood glucose level', min_value = 0, max_value = 500, value = None, step = 1, help = 'Your blood glucose levels')
        submitted = st.form_submit_button('predict')
    
        df_inf = {
        'gender': gender,
        'age':age,
        'hypertension': ht,
        'heart_disease':hd,
        'smoking_history': smoke,
        'bmi_category': bmi_category,
        'HbA1c_level': hba1c,
        'blood_glucose_level': bgc
        }

        df_inf1 = pd.DataFrame([df_inf])
        df_inf1

        if submitted:
            y_pred_inf = best_dt.predict(df_inf1)
            a = round(y_pred_inf[0],2)

    st.write('Diabetes ?:', a )

    if a == 1:
        st.write('The person is predicted to have diabetes')
    else:
        st.write('The person is not predicted to have diabetes')

if __name__ == '__main__':
    run()
    
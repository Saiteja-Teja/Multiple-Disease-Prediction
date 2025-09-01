# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 19:04:41 2025

@author: sait6
"""

import pickle

import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open("C:/Users/sait6/Downloads/diabetes_prediction.sav",'rb'))
heart_model=pickle.load(open("C:/Users/sait6/Downloads/heart_disease_prediction.sav",'rb'))
cancer_model=pickle.load(open("C:/Users/sait6/Downloads/breast_cancer_prediction (1).sav",'rb'))

#sidebar of navigation
with st.sidebar:
    selected=option_menu('multiple Desease Prediction System',['Diabetes prediction','Heart Disease Prediction','Breast Cancer Prediction'],default_index=0)


#Diabetes Prediction
if (selected=='Diabetes prediction'):
    st.title('Diabetes prediction')
        #getting input data
    col1,col2,col3=st.columns(3)
        #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    with col1:
        Pregnancies=st.number_input('enter number of pregnencies')
    with col2:
        Glucose=st.number_input('enter glucose value')
    with col3:
        BloodPressure=st.number_input('enter BloodPressure Value')
    with col1:
        SkinThickness=st.number_input('enter SklinThickness Value')
    with col2:
        Insulin=st.number_input('enter Insulin Value')
    with col3:
        BMI=st.number_input("enter BMI Value")
    with col1:
        DiabetesPedigreeFunction=st.number_input("enter DiabetesPedigreeFunction value")
    with col2:
        Age=st.number_input("enter your age")
        
            
        #code for prediction
    diab_diagnosis=''
        #creating button for prediction
    if st.button('Submit'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness,
                  Insulin, BMI, DiabetesPedigreeFunction, Age]

        diab_prediction = diabetes_model.predict([input_data])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)

            
#cancer Prediction
if (selected=='Breast Cancer Prediction'):
    st.title('Breast Cancer Prediction')
    #getting input data
    col1,col2,col3=st.columns(3)
       #mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness

    with col1:
        mean_radius=st.number_input('enter mean_radius value')
    with col2:
        mean_texture=st.number_input('enter mean_texture value')
    with col3:
        mean_perimeter=st.number_input('enter mean_perimeter Value')
    with col1:
        mean_area=st.number_input('enter mean_area Value')
    with col2:
        mean_smoothness=st.number_input('enter mean_smoothness Value')
           
        #code for prediction
    cancer_diagnosis=''
        #creating button for prediction
    if st.button('Submit'):
        input_data = [mean_radius, mean_texture, mean_perimeter,
                  mean_area, mean_smoothness]

        cancer_prediction = cancer_model.predict([input_data])

        if cancer_prediction[0] == 1:
            cancer_diagnosis = 'The person has Breast Cancer'
        else:
            cancer_diagnosis = 'The person does not have Breast Cancer'

        st.success(cancer_diagnosis)

            
#Heart Disease Prediction
if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
        #getting input data
    col1,col2,col3=st.columns(3)
        #age,sex,cp,trestbps,chol,fbs,restecg,thalachh,exang,oldpeak,slope,ca,thal
    with col1:
        age=st.number_input('enter number of age')
    with col2:
        sex=st.number_input('enter sex value')
    with col3:
        cp=st.number_input('enter cp Value')
    with col1:
        trestbps=st.number_input('enter trestbps Value')
    with col2:
        chol=st.number_input('enter chol Value')
    with col3:
        fbs=st.number_input("enter fbs Value")
    with col1:
        restecg=st.number_input("enter restecg value")
    with col2:
        thalachh=st.number_input("enter your thalachh")
    with col3:
        exang=st.number_input("enter exang Value")
    with col1:
        oldpeak=st.number_input('enter number of oldpeak')
    with col2:
        slope=st.number_input('enter slope value')
    with col3:
        ca=st.number_input('enter ca Value')
    with col1:
        thal=st.number_input('enter thal Value')
            
        #code for prediction
    heart_diagnosis=''
        #creating button for prediction
    if st.button('Submit'):
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg,
                  thalachh, exang, oldpeak, slope, ca, thal]

        heart_prediction = heart_model.predict([input_data])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has Heart Disease'
        else:
            heart_diagnosis = 'The person does not have Heart Disease'

        st.success(heart_diagnosis)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
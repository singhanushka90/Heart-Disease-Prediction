import streamlit as st
import pickle
import numpy as np

model=pickle.load(open("heart_model.pkl",'rb'))
scaler=pickle.load(open("heart_scaler.pkl",'rb'))

st.set_page_config(page_title="Heart Disease Prediction",layout='centered')

st.markdown("""<h1 style='text-align : center ; color: red;'> Heart Disease Prediction </h1>
            <p style='text-align : center; color: blue;'> Enter patient details to check heart disease risk </p>
            <hr>
            """,unsafe_allow_html=True)

col1,col2=st.columns(2) 

with col1:
    st.subheader("Patient Details")
    age=st.number_input("Age",1,120,45)
    sex=st.selectbox('Sex',['Female','Male'])
    cp=st.selectbox('Chest Pain Tyep',[0,1,2,3])
    st.subheader("Health Stats")
    rbp=st.number_input("Resting Blood Pressure",50,250,120)
    chol=st.number_input("Cholestrol",50,600,200)
    fbs=st.selectbox("Fasting Blood Sugar > 120 ",['No','Yes'])

with col2:
    st.subheader("Medical Data")
    ecg=st.selectbox("Resting ECG",[0,1,2])
    maxhr=st.number_input("Max Heart Rate",50,250,150)
    exang=st.selectbox("Exercise Angina",['No','Yes'])
    st.subheader("Advanced")
    oldpeak=st.number_input("Oldpeak",0.0,10.0,1.0)
    slope=st.selectbox("ST Slope",[0,1,2])


sex=1 if sex=='Male' else 0
fbs=1 if fbs=='Yes' else 0
exang=1 if exang=='Yes' else 0


if st.button("Predict"):
    if chol==0 or rbp==0:
        st.warning("Please enter valid health values !")
    else:
        features=np.array([[age,sex,cp,rbp,chol,fbs,ecg,maxhr,exang,oldpeak,slope]])

        scaled=scaler.transform(features)
        result=model.predict(scaled)[0]
        try:
            prob=model.predict_proba(scaled)[0][1]
            st.info(f" Risk Probability: {prob*100:.2f}%")
        except:
            pass

        if result==1:
            st.error("High Risk : HEART DISEASE DETECTED!")
        else:
            st.success("Low Risk : NO HEART DISEASE DETECTED!")
        st.balloons()
    

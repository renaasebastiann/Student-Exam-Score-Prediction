import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("best_model_pipeline.pkl", "rb") as f:
    model= pickle.load(f)

st.set_page_config(page_title="Student Score Predictor", layout="centered")
st.title("📊 Predict Future Student Scores")

with st.form("student_form"):
    st.subheader("Enter Student Details:")

    gender= st.selectbox("Gender", ["Male", "Female"])
    parent_educ= st.selectbox("Parent Education", [
        " Not Completed High School", "High School", "Not Completed College", "Associate's Degree", "Bachelor's Degree", "Master's Degree"
    ])
    lunch= st.selectbox("Lunch Type", ["Standard", "Free"])
    test_prep= st.selectbox("Test Preparation", ["Completed", "Some/None"])
    marital_status= st.selectbox("Parent Marital Status", ["Married", "Single", "Widowed", "Divorced"])
    practice_sport= st.selectbox("Sport Frequency", ["Never", "Sometimes", "Regularly"])
    is_first_child= st.selectbox("First Child", ["Yes", "No"])
    nr_siblings= st.slider("Number of Siblings", 0, 7, 1)
    transport= st.selectbox("Transport Means", ["School Bus", "Private"])
    study_hours= st.selectbox("Weekly Study Hours", [
        "Less than 5 hrs", "Between 5 and 10 hrs", "More than 10 hrs"
    ])

    st.subheader("Enter Current Scores:")
    math_score= st.number_input("Math Score (0-100)", 0, 100, 75)
    reading_score= st.number_input("Reading Score (0-100)", 0, 100, 78)
    writing_score= st.number_input("Writing Score (0-100)", 0, 100, 80)
    
    
    submitted= st.form_submit_button("Predict Future Scores")

if submitted:
    input_data= pd.DataFrame([{
        "Gender": gender,
        
        "ParentEduc": parent_educ,
        "LunchType": lunch,
        "TestPrep": test_prep,
        "ParentMaritalStatus": marital_status,
        "PracticeSport": practice_sport,
        "IsFirstChild": is_first_child,
        "NrSiblings": nr_siblings,
        "TransportMeans": transport,
        "WklyStudyHours": study_hours,
        "MathScore": math_score,
        "ReadingScore": reading_score,
        "WritingScore": writing_score
    }])
    
    input_data["HasCompletedTestPrep"]= 1 if test_prep == "completed" else 0
    input_data["TotalScore"]= input_data[['MathScore', 'ReadingScore', 'WritingScore']].mean(axis=1)


    prediction= model.predict(input_data)

    st.success("✅ Predicted Future Scores:")
    st.write(f"📘 Math Score: **{prediction[0][0]:.2f}**")
    st.write(f"📗 Reading Score: **{prediction[0][1]:.2f}**")
    st.write(f"📕 Writing Score: **{prediction[0][2]:.2f}**")

# Student-Exam-Score-Prediction
The Student Score Predictor is a machine learning-powered web application designed to forecast 
students' performance in mathematics, reading, and writing based on key demographic and 
academic input features. As academic performance is influenced by various socio-educational 
factors, this project aims to leverage predictive analytics to support early intervention and 
provide actionable insights for educators, parents, and students. 
The dataset used, Expanded_data_with_more_features.csv, contains detailed information such as 
gender, parental level of education, lunch type, test preparation status, and weekly study hours. 
Additional engineered features like Total Score and Test Preparation Completion were created to 
improve model accuracy. After thorough data preprocessing and exploratory data analysis, the 
project applied a machine learning pipeline using a MultiOutputRegressor with a Random Forest 
Regressor as the core model. This setup allows for simultaneous prediction of all three subject 
scores, considering feature interdependencies and maximizing performance. 
Model performance was evaluated using metrics such as Mean Absolute Error (MAE), Root 
Mean Squared Error (RMSE), and R-squared (R²), ensuring robust and reliable outputs. 
Visualizations including predicted vs actual plots and feature importance charts further validate 
the model’s interpretability. 
The model was then deployed through an interactive Streamlit web application, allowing users to 
input individual student characteristics and receive real-time predictions for their Math, Reading, 
and Writing scores. The app simplifies complex machine learning operations behind a 
user-friendly interface, making it accessible to users without technical expertise. 
This project not only highlights the practical utility of machine learning in education but also 
demonstrates end-to-end deployment of an ML system—from data ingestion and model training 
to real-time user interaction. By removing bias-related features like ethnicity and focusing on 
actionable attributes such as preparation time and parental education, the model remains ethical 
and impactful. 
In conclusion, the Student Score Predictor serves as a valuable educational support tool that 
enables early identification of performance gaps and encourages data-driven strategies for 
academic improvement. Future enhancements could include expanding the dataset, integrating 
time-series learning progress, or recommending personalized study plans based on predicted 
weaknesses.

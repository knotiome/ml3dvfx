import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier


st.write("""
Hello this app is now ran      
""") 

st.sidebar.header("User input data features")
st.sidebar.markdown("""
[CSV inpute file: ]
- This is just a **TEST**
""")

uploaded_file = st.sidebar.file_uploader("CSV File: ", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)

else:
    def user_input_features():
        SepalLengthCm = st.sidebar.slider('SepalLengthCm', 4.3, 8.0, 6.0)
        SepalWidthCm = st.sidebar.slider('SepalWidthCm', 2.0, 5.0, 3.0)
        PetalLengthCm = st.sidebar.('PetalLengthCm', 1.0, 7.0, 4.0)
        PetalWidthCm = st.sidebar.('PetalWidthCm', 0.1, 3.0, 2.0)
        data = {'SepalLengthCm': SepalLengthCm,
                'SepalWidthCm': SepalWidthCm,
                'PetalLengthCm': PetalLengthCm,
                'PetalWidthCm': PetalWidthCm}
        
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()
        
iris_raw = pd.read_csv('iris.csv')
iris = iris_raw.drop(['Species', 'Id'])
df







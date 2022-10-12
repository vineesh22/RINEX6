import streamlit as st
import joblib

model = joblib.load('spam-ham')# we are loading the pipelined model using joblib
st.title('SPAM-HAM CLASSIFIER')#It creates a title in webapp
ip = st.text_input('Enter the message')#It creates a text box in the webapp
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) #st.button will create a button with the name Predict
  #st.title(op[0]) # the 0th element in op variable is displayed as a title

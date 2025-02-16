import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI")

sys_prompt = """You are an intelligent Python code review assistant. 
Your task is to analyze user-submitted Python code, identify potential bugs, and provide clear, actionable feedback. 
You should highlight syntax errors, logical issues, and inefficiencies while suggesting accurate fixes with explanations. 
Ensure that your responses are user-friendly, concise, and helpful for both beginners and experienced developers. 
Maintain efficiency in processing code and focus on improving the overall quality and readability of the submitted script
"""

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("Python Code Reviewer")

user_input = st.text_area(label="Enter your python code ", placeholder="import pandas as pd?")

btn_click = st.button(" Search")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)
import os
from pprint import pprint
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai. configure(api_key= os.gentenv("GOOGLE_API_KEY"))
model= genai.GenerativeModel('genmini-pro')

prompt_template= """
You are an expert at planning oversea trips.

Please take the users request and plan a comprehensive trip for them.

...
"""

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title("Gemini Playgroung")

prompt = st.text_area("Promt")
if prompt:
    reply = generate_content(prompt)
    st.write(reply)

# utils/llm.py

import os
from dotenv import load_dotenv
#import google.generativeai as genai - This has become old now so commenting this google.generativeai package and switching to the new one below
import google.genai as genai

load_dotenv()

""" genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
) """

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

#model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(prompt):
    #response = model.generate_content(prompt)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
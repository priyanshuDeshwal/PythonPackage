import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_FOR_AI = os.getenv("API_KEY")

# Configure the API key
genai.configure(api_key= API_KEY_FOR_AI)

# Instantiate the generative model
model = genai.GenerativeModel(model_name='gemini-1.0-pro')

while True:
    # Prompt the user for input
    user_input = input("Please enter your prompt (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Generate content based on the user's input
    response = model.generate_content(user_input)

    # Print the generated response
    print(response.text)

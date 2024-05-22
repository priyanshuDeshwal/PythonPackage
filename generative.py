import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key="AIzaSyAC50n7kbB-5sRGLV6ydzpRe9UDkAJmZZE")

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

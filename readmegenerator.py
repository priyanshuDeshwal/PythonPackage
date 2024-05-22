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
    user_input = input("Please enter your code (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Generate a README based on the provided code
    prompt = "Generate a README.md for the following code:\n\n" + user_input
    response = model.generate_content(prompt)

    # Print the generated README content
    readme_content = response.text
    print("\nGenerated README.md content:\n")
    print(readme_content)

    # Ask if the user wants to save the README to a file
    save_to_file = input("Do you want to save the README.md to a file? (yes/no): ").strip().lower()
    if save_to_file == 'yes':
        with open('README.md', 'w') as file:
            file.write(readme_content)
        print("README.md has been saved to the current directory.")

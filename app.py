from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

# Retrieve the open AI key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(
    api_key = openai_api_key
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') #Calls the index html

@app.route("/ask", methods = ['POST'])
def ask():
    user_message = request.form.get("user_input")  # This is what the user asks


    example_blogs = read_files()

    prompt = "Create a blog in markdown form on this set of information " + user_message + ". Based on the following examples (ENSURE to maintain the exact structure, format, structuring in markdown and ensure to use quotes from the infromation that I just gave.) Here are the example blogs: " + example_blogs + " Do not add chatgpt commentary/auxilary notes."


    # Open AI response
    response = openai.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": "respond to the user as a chatbot."},
            {"role": "user", "content": prompt}
        ]
    )

    print(response)
    openai_response = response.choices[0].message.content   # Get the response

    return render_template('index.html', user_message=user_message, openai_response=openai_response)  # Pass it to the frontend

def read_files():
    # Get the list of uploaded files
    files = request.files.getlist('blog_templates')

    file_contents = ""
    for file in files:
        if file and allowed_file(file.filename):
            print(f"Filename: {file.filename}") # Print the file name
            content = file.read().decode("utf-8")  # Read file content
            file_contents += content + "\n\n"  # Append content from each file
    return file_contents


def allowed_file(filename):
    # Check if the uploaded file is a markdown file
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'md'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template, Response
from openai import OpenAI
import os
import re
from dotenv import load_dotenv

# Retrieve the open AI key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(
    api_key = openai_api_key
)

app = Flask(__name__)

openai_response = ""

@app.route('/')
def home():
    return render_template('index.html') #Calls the index html

@app.route("/ask", methods = ['POST'])
def ask():
    user_message = request.form.get("user_input")  # This is what the user asks


    example_blogs = read_files()

    prompt = "Create a blog in markdown form on this set of information " + user_message + ". The blog you write must adhere STRICTLY to how the following example blogs are written" + example_blogs + " Do not add chatgpt commentary/auxilary notes. Ensure you follow the structures correctly. Additionally include Front Matter: Include a title, date, author, and a brief description of the content. Also, include any relevant keywords in an array. Introduction: Provide a concise introduction to the topic. Explain the main subject matter and what the blog will cover.Main Content: Divide the content into sections with descriptive headings. Each section should be focused on a specific aspect of the topic. Use numbered or bulleted lists to break down complex ideas, steps, or information. Examples and Visuals: If applicable, provide examples, screenshots, or images using markdown syntax. Embed the images properly. Conclusion: End with a brief conclusion, summarizing the main points or offering advice or recommendations. Call to Action (optional): If appropriate, end with a call to action, encouraging readers to share their thoughts, comments, or take the next steps. Ensure the tone is informative, clear, and professional, while being easy to follow. Write in short paragraphs, and break up large sections of text to enhance readability. Follow a structured and consistent markdown format for headings, lists, images, and other formatting. Add placeholder images, videos links with subtitles YOU MUST DO THIS. USE QUOTES. Do not include this at the start \"```markdown\" I DO NOT WANT THIS. ENSURE that the metadata/keys follow the exact format for example the quotations must be the same as a string.EXACTLY FOLLOW THE STRUCTURE FOR IMAGES AND CAPTIONS. it must need a caption the figure caption should appear below the image/video so there needs top be a double new line. Also include more \">\""


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

    # Save the OpenAI response to a markdown file
    save_to_markdown(openai_response)

    return render_template('index.html', user_message=user_message, openai_response=openai_response)  # Pass it to the fronten

@app.route("/download")
def download():
    # Path to the generated markdown file
    markdown_file = "generated_blog.md"

    # Return the markdown file as a downloadable file
    return Response(
        open(markdown_file, 'r').read(),
        mimetype='text/markdown',
        headers={"Content-Disposition": "attachment;filename=generated_blog.md"}
    )


import os

def read_files():
    blog_templates_dir = "blog_templates"  # Directory containing markdown templates
    file_contents = ""

    # Make sure the blog template directory exists
    if not os.path.exists(blog_templates_dir):
        print(f"Directory '{blog_templates_dir}' does not exist!")
        return file_contents

    # Iterate through all files in the directory
    for filename in os.listdir(blog_templates_dir):
        if filename.endswith(".md"):  # Only read Markdown files
            file_path = os.path.join(blog_templates_dir, filename)
            print(f"Reading file: {file_path}")  # Should print the file
            with open(file_path, "r", encoding="utf-8") as file:
                file_contents += file.read() + "\n\n"
    return file_contents

def save_to_markdown(content):
    # Save the OpenAI response to a markdown file
    with open("generated_blog.md", "w") as file:
        file.write(content)

if __name__ == '__main__':
    app.run(debug=True)
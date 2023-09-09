from flask import Flask, render_template
import requests
from jinja_markdown import MarkdownExtension

app = Flask(__name__)
app.jinja_env.add_extension(MarkdownExtension)


@app.route('/')
def hello():
    url = "https://raw.githubusercontent.com/lawrenceaph/text-tree/main/one.txt"
    response = requests.get(url)
    title = "Flask on Google Cloud Run 🎉"
    message = response.text or "hi"
    url2 = "https://raw.githubusercontent.com/lawrenceaph/text-tree/main/two.md"
    responsemd = requests.get(url2)
    md = responsemd.text or "markdown"
    description = "Awesome Sample Python App for Cloud Run With Flask and Markdown"
    image="https://images.unsplash.com/photo-1595500381966-eee2034aae48?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80"

    return render_template('index.html', page_title=title, content=title, message = message, md=md, description=description, image=image) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')


 

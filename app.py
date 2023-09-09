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
    return render_template('index.html', page_title=title, content=title, message = message, md=md) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')


 

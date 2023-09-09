from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route('/')
def hello():
    url = "https://raw.githubusercontent.com/lawrenceaph/text-tree/main/one.txt"
    response = requests.get(url)
    title = "Flask on Google Cloud Run 🎉"
    message = response.text or "hi"
    return render_template('index.html', page_title=title, content=title, message = message) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')


 

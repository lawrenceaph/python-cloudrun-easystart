from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route('/')
def hello():
    url = "https://gist.githubusercontent.com/lawrenceaph/532ae1423a43d1b17ee41780f9a93d18/raw/55dc8fac2044a5c9d7954b7287bb627b5ec73ead/message.txt"
    response = requests.get(url)
    title = "Flask on Google Cloud Run 🎉"
    message = response.text or "hi"
    return render_template('index.html', page_title=title, content=title, message = message) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')


 

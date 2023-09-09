from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def hello():
    title = "Flask on Google Cloud Run 🎉"
    return render_template('index.html', page_title=title, content=title) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')


 

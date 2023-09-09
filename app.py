from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return HTML_TEMPLATE

if __name__ == '__main__':
    app.run(host='0.0.0.0')



HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask on Google Cloud Run</title>
    <style>
        body {
            margin: 0;
            font-family: 'sans-serif';
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        h1 {
            font-size: 44px;
            font-family:'arial';
            color: #0079c1;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <h1>Flask on Google Cloud Run</h1>
</body>
</html>
"""

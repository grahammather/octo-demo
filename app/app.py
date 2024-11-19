from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def show_token():
    token = os.getenv('TOKEN', 'TOKEN environment variable not set')
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Token Viewer</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #121212;
                color: #ffffff;
                font-family: 'Arial', sans-serif;
                font-size: 3em;
                text-align: center;
            }
            .container {
                max-width: 90%;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Token Value</h1>
            <p>{{ token }}</p>
        </div>
    </body>
    </html>
    """, token=token)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

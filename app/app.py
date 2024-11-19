from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def show_token():
    token = os.getenv('TOKEN', 'TOKEN environment variable not set')
    return f"<h1>Token Value</h1><p>{token}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

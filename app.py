from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from Flask! You're awesome for making it this far."

if __name__ == '__main__':
    app.run()

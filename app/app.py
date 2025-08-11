from flask import Flask
app = Flask(__name__)

@app.route("/")
def resume():
    return "Hello, this is my resume API!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>hello world!</h1>"

@app.route('/projects/')
def projects():
    return "<h1>hello project</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")


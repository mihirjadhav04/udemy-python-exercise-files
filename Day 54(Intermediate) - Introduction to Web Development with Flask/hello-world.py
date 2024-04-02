from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# learnt basics of flask
# decorators
# __name__
# __main__
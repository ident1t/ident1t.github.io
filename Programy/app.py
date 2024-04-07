from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello world!"

if __name__ == "_main":
    app.run(host='0.0.0.0', debug=True)

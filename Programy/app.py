from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def helloworld():
    return render_template("Homepage/index.html")

if __name__ == "_main":
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bihin")
def bihin():
    return "<h1>備品管理ページ</h1>"

@app.route("/忘れ物")
def 忘れ物():
    return "<h1>忘れ物管理ページ</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
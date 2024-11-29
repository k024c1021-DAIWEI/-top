from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 仮のユーザーデータ（ログイン用）
users = {"admin": "password123"}

# ホームページ
@app.route("/")
def home():
    return render_template("index.html")

# 備品管理ページ
@app.route("/bihin")
def bihin():
    return "<h1>備品管理ページ</h1>"

# 忘れ物管理ページ
@app.route("/忘れ物")
def 忘れ物():
    return "<h1>忘れ物管理ページ</h1>"

# ログインページ
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # ユーザー名とパスワードが正しい場合、管理ページへリダイレクト
        if username in users and users[username] == password:
            return redirect(url_for("management"))
        else:
            return "<h1>ログイン失敗！</h1>"

    return render_template("login.html")

# データ管理ページ（管理機能）
@app.route("/management")
def management():
    # 現在は仮のデータ表示（後で実際のデータを表示することができます）
    return "<h1>データ管理ページ</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
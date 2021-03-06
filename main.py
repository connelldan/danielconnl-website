from flask import Flask, render_template, url_for, request, redirect
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/music')
def music():
    return render_template("music.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
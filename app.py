from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/profile')
def index():
    return render_template("index.html")

@app.route('/')
def redirect_to_profile():
    return redirect(url_for('index'))

app.run(host="localhost", port=5000, debug=True)
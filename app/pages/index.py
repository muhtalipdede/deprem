from flask import render_template

def index_page():
    return render_template("index.html")
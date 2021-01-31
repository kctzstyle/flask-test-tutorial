
from flask import Flask, render_template, url_for, redirect

from models import Index


Application = Flask(__name__)

# Application.add_url_rule(
#     "/favicon.ico",
#     redirect_to=url_for("static", filename="favicon.ico"))


@Application.route("/")
def index():
    index = Index(title='Index', content="Hello, Flask!")
    return render_template("index.html", index=index)


@Application.route("/kctzstyle/")
def kctzstyle():
    return redirect("https://github.com/kctzstyle")

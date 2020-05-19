from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def index():
     headline = "TinTuyenSinh"
     return render_template("index.html", test= headline)
@app.route("/ltd")
def ltd():
     return "Hello LTD!"
@app.route("/<string:name>")
def hello(name):
     name = name.capitalize()
     return "<h1>Hello, " + name + "</h1>"
@app.route("/new_year")
def new():
     now = datetime.datetime.now()
     new_year = now.month == 1 and now.day == 1
     new_year = True
     return render_template("index.html", new_year=new_year)
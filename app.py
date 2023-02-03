from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return """<h1>Home page</h1>"""

@app.route("/temperature", methods= ['GET', 'POST'])
def temp_con():
    if request.method == "GET":
        return render_template("temp_main.html")
    elif request.method == "POST":
        celsius_ = request.form["celsius"]
        fahrenheit_ = request.form["fahrenheit"]
        if celsius_ == "" and fahrenheit_ == "":
            return render_template("invalid.html")
        elif celsius_ != "" and fahrenheit_ != "":
            celsius_ = int(celsius_)
            fahrenheit = (celsius_*9/5) + 32
            fahrenheit_ = int(fahrenheit_)
            celsius = (fahrenheit_ - 32)* 5/9
            return render_template("temp_main.html", fahrenheit= fahrenheit, celsius= celsius )
        elif celsius_ != "":
            celsius_ = int(celsius_)
            fahrenheit = (celsius_*9/5) + 32
            return render_template("temp_main.html", fahrenheit= fahrenheit )
        elif fahrenheit_ != "":
            fahrenheit_ = int(fahrenheit_)
            celsius = (fahrenheit_ - 32)* 5/9
            return render_template("temp_main.html", celsius= celsius)
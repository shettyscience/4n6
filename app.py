from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/art")
def articles():
    return render_template("articles.html")


@app.route("/res")
def research():
    return render_template("research.html")


@app.route("/reso")
def resources():
    return render_template("resources.html")


@app.route("/kan")
def kannada():
    return render_template("kannada.html")

if __name__ == '__main__':
    app.run()
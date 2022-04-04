# Flask port number: localhost:5000

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add')
def Add():
    return render_template("add.html")

@app.route('/search')
def Search():
    return render_template("search.html")

@app.route('/update')
def Update():
    return render_template("update.html")

@app.route('/delete')
def Delete():
    return render_template("delete.html")

if __name__ == "__main__":
    app.run()


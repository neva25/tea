from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route("/")
def index():
    df = pd.read_csv("data/tea-new.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('main.html', items=items)


@app.route("/glenburn")
def glenburn():
    df = pd.read_csv("data/glenburnfinetea-final2.csv", index_col=0, encoding= 'unicode_escape')
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('glenburn.html', items=items)


@app.route("/tata")
def tata():
    df = pd.read_csv("data/tata-new.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('tata.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)


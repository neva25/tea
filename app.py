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
    df = pd.read_csv("data/glenburn-tea.csv", encoding= 'unicode_escape')
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('glenburn.html', items=items)


@app.route("/tata")
def tata():
    df = pd.read_csv("data/tata-new.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('tata.html', items=items)


@app.route("/weaveskart")
def weavekart():
    df = pd.read_csv("data/weaveskart-new.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('spice.html', items=items)


@app.route("/prideofindia")
def pride():
    df = pd.read_csv("data/prideofindia.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('prideofindia.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5001)


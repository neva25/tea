from flask import Flask, render_template
import pandas as pd
import pdfkit

app = Flask(__name__)


@app.route("/")
def home():
    df = pd.read_csv("tea-new.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')

    # html = render_template("eg.html", items=items)
    # try:
    #     path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    #     configuration = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    #     pdfkit.from_string(html, "tea.pdf", configuration=configuration)
    # except Exception as e:
    #     print(e)

    return render_template('main.html', items=items)


@app.route("/glenburn")
def glenburn():
    df = pd.read_csv("glenburnfinetea-new.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('glenburn.html', items=items)


@app.route("/tata")
def tata():
    df = pd.read_csv("tata-new.csv", index_col=0)
    df = df.fillna(0)
    items = df.to_dict('records')
    return render_template('tata.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
    print("jjjj")



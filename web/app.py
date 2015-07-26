import pandas as pd

from flask import Flask
from flask import render_template

app = Flask(__name__)

data = pd.load('../notebooks/data3.df').sort('upvotes', ascending=False)


@app.route('/')
def hello_world():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

import pandas as pd

from flask import Flask
from flask import render_template

app = Flask(__name__)

data = pd.load('../notebooks/data2.df').sort('upvotes', ascending=False)


@app.route('/')
def hello_world():
    return render_template('index.html', data=data[:100])


if __name__ == '__main__':
    app.run(debug=True)

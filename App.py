from typing import Protocol
from flask import Flask, render_template, request, json
import json
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')
    
@app.route('/filter', methods=['POST'])
def filter():
    data = pd.read_excel('C:/Users/adsieg/Desktop/flask_tuto/wine_filter.xlsx', encoding='utf8')
    data = data[(data['country']==request.form["Country"]) & (data['province']==request.form["Region"])]
    data = data.head(50)
    data = data.to_dict(orient='records')
    response = json.dumps(data, indent=2)
    return response
    
if __name__ == '__main__':
    app.run(host='localhost', port=9874)
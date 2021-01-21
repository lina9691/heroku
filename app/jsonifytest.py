from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

f = open('Datas.json')
data = json.load(f)
f.close()


@app.route('/api')
def hello():
    print (list(data))
    return data

if __name__=="__main__":
    app.run()
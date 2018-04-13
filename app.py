from flask import Flask
from pymongo import MongoClient
import random
app = Flask(__name__)
client = MongoClient('172.19.0.2',27017)
db=client['datas']

@app.route('/')
def hello():
    db.col.insert({"hits":random.random()})
    return 'Hello World! I have been seen %s times.' % (db.col.count())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


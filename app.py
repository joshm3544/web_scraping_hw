from flask import Flask, render_template

import pymongo

app = (Flask(__name__)
       
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)






@app.route('/')


if __name__ = "__main__":
    app.run(debug=True)
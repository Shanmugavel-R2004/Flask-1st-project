#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div style='background:blue'><h1>Hello world</h1><br><h1>Hii</h1></div>"
if __name__=='__main__':
    app.run(debug=True)
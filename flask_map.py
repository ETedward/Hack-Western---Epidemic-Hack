from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new index',methods = ['POST', 'GET'])
def login():
    return render_template("new index.html")

if __name__ == "__main__":
    app.run()

    
#http://localhost:5000/new%20index

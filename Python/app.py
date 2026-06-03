from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>coaching class manager</h1>"

@app.route("/students")
def students():
    return "<h1>students page</h1>"

@app.route("/teachers")
def teachers():
    return "<h1>teachers page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    

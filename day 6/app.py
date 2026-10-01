from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "web development in python"

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True) 

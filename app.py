from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    print('Hello World !')
    


if __name__ == "__maim__":
    app.run(host="0.0.0.0", debug=True)
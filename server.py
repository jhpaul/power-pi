from flask import Flask
import light
app = Flask(__name__)

@app.route('/')
def hello_world():
    light.light()
    return "Light Toggle"


@app.route('


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

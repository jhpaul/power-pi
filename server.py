from flask import Flask
from flask import request
import light
app = Flask(__name__)

@app.route('/')
def hello_world():
    light.toggle()
    return "Light Toggle"


@app.route('/light', methods=['GET', 'POST'])
def lights():
    if request.method == 'POST':
        light.toggle()
    else:
        return light.status()


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

from flask import Flask
from flask import request, redirect, url_for
import light, helpers
app = Flask(__name__)

@app.route('/')
def hello_world():
    light.toggle()
    return "Light Toggle"


@app.route('/light', methods=['GET', 'PUT', 'POST'])
def lights():
    if request.method in ('PUT', 'POST'):
        helpers.toggle()
    else:
        return light.status() + "\n"

@app.route ('/light/toggle', methods=['GET','PUT','POST'])
def toggle():
    if request.method in ('PUT',"POST"):
        return redirect(url_for('lights'), code=302)
    else:
        return helpers.toggle()
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

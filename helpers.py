from server import *
def toggle():
    light.toggle()
    # return "Light Toggled <br>\n" + light.status() +"\n"
    flash("Light Toggled")
    return light.status()
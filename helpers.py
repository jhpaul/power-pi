from server import *
def toggle():
    light.toggle()
    return "Light Toggled \n" + light.status() +"\n"
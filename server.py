#!/usr/bin/python2
from flask import Flask
from flask import request, flash, redirect, url_for, render_template, jsonify
import power
import light
import helpers
import powerstate
import cleanup
import time
# import RPi.GPIO as GPIO
import sys
# from OpenSSL import SSL

# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('jhpaul.key')
# context.use_certificate_file('ssl.crt')
try:
    app = Flask(__name__)
    app.secret_key = 'some_secret'

    @app.context_processor
    def util():
        def lightStatus():
            return str(light.status())
        def powerState():
            return str(powerstate.status())
        return dict(lightStatus=lightStatus(),powerState=powerState())

    @app.route('/')
    def index():
        return  render_template('index.html')
        # return light.status() + "<br><a href='/light/toggle' target='_blank'>Toggle</a>"


    @app.route('/light', methods=['GET', 'PUT', 'POST'])
    def lights():
        if request.method in ('PUT', 'POST'):
            helpers.toggle()
        else:
            return light.status() + "\n"

    @app.route ('/light/toggle', methods=['GET','PUT','POST'])
    def toggle():
        if request.method in ('PUT',"POST"):
            return redirect(url_for('light'), code=302)
        else:
            return helpers.toggle()

    @app.route('/button')

    @app.route('/button/short', methods=['GET', 'PUT', 'POST'])
    def short():
        return power.short()

    @app.route('/button/long', methods=['GET', 'PUT', 'POST'])
    def long():
        return power.long()

    @app.route('/button/state', methods=['GET', 'PUT', 'POST'])
    def state():
        return powerstate.status(),

    @app.route('/light/state', methods=['GET', 'PUT', 'POST'])
    def lightstate():
        return light.status(),

    if __name__ == '__main__':
        app.debug = True
        app.run(host="0.0.0.0",)# ssl_context=context)

except:
    cleanup.clean()
    print "cleaned"

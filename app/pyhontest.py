# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 23:07:38 2021

@author: etudiant
"""

from flask import Flask, render_template

app = Flask('testapp')

@app.route('/')
def index():
    return render_template('index.html', variable='12345')

if __name__ == '__main__':
    app.run()
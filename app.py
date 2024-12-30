# Copyright (c) 2024 Vikas-06978
# Licensed under the MIT License
# Unauthorized copying of this file, via any medium, is strictly prohibited
# Written by Vikas


from flask import Flask, render_template

app = Flask(__name__)

import config

import models

import routes

import api

if __name__ == '__main__':
    app.run(debug=True)

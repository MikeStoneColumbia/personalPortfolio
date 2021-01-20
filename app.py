from flask import Flask, render_template, request, json, jsonify, current_app as app
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1')
import json

import flask.cli
from flask import Flask, request, Response, render_template, jsonify
import requests
import random


app = Flask(__name__, static_url_path='/static')



@app.route("/kogpt2", methods=["POST"])
def gpt2():
    context = request.form['context']
    headers = {'Content-Type': 'application/json; charset=\'utf-8\''}
    num_samples = 1
    length = 300

    data = {
        "text": context,
        "num_samples": num_samples,
        "length": length
    }

    response = requests.post('https://train-kovgd07j8yvco5i03qo3-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune',headers=headers,json=data)

    res = response.json()

    return jsonify(res)


@app.route("/")
def main():
    return render_template("index.html")


# Health Check
@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)


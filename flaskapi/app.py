#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import abort, jsonify

# 测试数据暂时存放
tasks = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1> hello world..<h1>'

@app.route('/add_task', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)

    task={
        'id':request.json['id'],
        'info':request.json['info']
    }
    tasks.append(task)
    return jsonify({'result':'success'})

@app.route('/get_task', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        return jsonify(tasks)

    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result':'not found'})


if __name__=='__main__':
    app.run(host="0.0.0.0", port=8383, debug=True)
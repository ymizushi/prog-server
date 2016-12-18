#!/usr/bin/env python3

import traceback
import logging

from flask import Flask
from flask import request
from flask import jsonify
from model.session import Session, SessionRepository
from model import redis_client
from lang import Env, evaluate
from config import app_config

logging.basicConfig()
logger = logging.getLogger('prog')

app = Flask(__name__)


@app.route("/session", methods=["POST"])
def create_session():
    try:
        json = request.get_json()
        seed = json.get('seed')
        env = Env()
        session = Session.create(seed, env)
        session_repo = SessionRepository(redis_client)
        session_repo.save(session)
        return jsonify(status=200, data=dict(session_id=session.id))
    except Exception as e:
        logger.error(traceback.print_exception(e))
        return jsonify(status=500)


@app.route("/session/<session_id>", methods=["DELETE"])
def delete_session(session_id):
    try:
        session_repo = SessionRepository(redis_client)
        session_repo.delete(session_id)
        return jsonify(status=200)
    except Exception as e:
        logger.error(traceback.print_exception(e))
        return jsonify(status=500)


@app.route("/session/<session_id>/eval", methods=["POST"])
def eval(session_id):
    session_repo = SessionRepository(redis_client)
    json = request.get_json()
    input_string = json.get('input')
    session = session_repo.get(session_id)
    if session:
        env = session.env
        output, enved = evaluate(input_string, env)
        session.env = enved
        session_repo.save(session)
        return jsonify(status=200, data=dict(output=output))
    else:
        return jsonify(status=400, message="sessionが見つかりませんでした")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app_config.get('port'), debug=app_config.get('debug'))

"""Deliberately unsafe code for the SecondBrain GitHub integration test org.

It exists only so CodeQL raises a code scanning alert. Never copy it.
"""

import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/run")
def run() -> str:
    os.system(request.args.get("cmd", ""))
    return "ok"

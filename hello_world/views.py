from hello_world import app
from formater import get_formatted
from formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Adrianna"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)


@app.route('/Adrian')
def show_name():
    return "Adrian"

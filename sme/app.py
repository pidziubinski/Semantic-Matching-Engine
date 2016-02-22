#!/usr/bin/env python


"""Semantic matching engine."""


from flask import Flask, render_template, request, redirect
from flask import send_from_directory
from forms import MainForm
from match import match_texts, RESULTS_FOLDER, FILES_EXTENTION
from os import environ
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_object(environ['SME_SETTINGS'])
SERV_LOG = "serv_logs/dev.logs"


@app.route('/', methods=['GET', 'POST'])
def main():
    """Main page."""
    form = MainForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('main.html', form=form)
        else:
            link = match_texts(form.text_1.data, form.text_2.data)
            return redirect('results/' + link)
    elif request.method == 'GET':
        return render_template('main.html', form=form)


@app.route('/results/<id>')
def results(id):
    """Results."""
    return send_from_directory(RESULTS_FOLDER, id + FILES_EXTENTION)


@app.route('/results/')
def results_main():
    """Results main."""
    return "Please provide results id in URL i.e. results/1234-5678-ABCD"

if __name__ == '__main__':
    handler = RotatingFileHandler(SERV_LOG, maxBytes=10000, backupCount=10000)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    print "Config:", environ['SME_SETTINGS']
    app.run(host='0.0.0.0', port=6069, threaded=True)

#!/usr/bin/python
# coding: utf-8
import math
import os

import cairo
from flask import Flask, render_template, send_file

from .functions import FILENAME, PDF_PATH, create_pdf

# Flask app
app = Flask(__name__)

# Homepage
@app.route("/")
def entry_point():
    return render_template("index.html")


# Create and Return PDF
@app.route("/createfile")
def deliver_file():

    create_pdf()
    return send_file(
        PDF_PATH + "/" + FILENAME + ".pdf",
        attachment_filename=FILENAME + ".pdf",
        as_attachment=True,
        cache_timeout=0,
    )


if __name__ == "__main__":
    app.run(debug=True)

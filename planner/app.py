#!/usr/bin/python
# coding: utf-8
from flask import Flask, render_template, send_file

from .functions import FILENAME, PDF_PATH, create_pdf

# Flask app
app = Flask(__name__)

# Test data to pass to the index.html
dates = [{"month": 8, "day": 1, "year": 2022}]

# Homepage
@app.route("/")
def entry_point():
    """Home Page"""
    return render_template("index.html", messages=dates)


# Create and Return PDF
@app.route("/createfile", methods=["POST"])
def deliver_file():
    """Create File"""
    try:
        create_pdf()
        print("---- PDF CREATED SUCCESSFULLY! ----")
    except OSError:
        print("---- PDF CREATION FAILED :( ----")
        return render_template("index.html")

    return send_file(
        PDF_PATH + "/" + FILENAME + ".pdf",
        attachment_filename=FILENAME + ".pdf",
        # as_attachment=True,
        cache_timeout=0,
    )


# Fetch PDF results
@app.route("/files/<string:name>", methods=["GET"])
def files(name: str):
    """Retrieve File"""
    return send_file(
        f"{PDF_PATH}/{name}.pdf", attachment_filename=f"{name}.pdf", cache_timeout=0
    )


# Run locally by executing app.py
if __name__ == "__main__":
    app.run(debug=True)

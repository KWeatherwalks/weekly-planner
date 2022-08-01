"""Flask App for Weekly Planner"""
#!/usr/bin/python
# coding: utf-8
from flask import Flask, redirect, render_template, send_file

from .functions import PDF_PATH, create_pdf

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
@app.route("/createfile/<year>/<month>/<day>", methods=("GET", "POST"))
def create_file(year: int, month: int, day: int):
    """
    Create File
    """
    try:
        create_pdf({"year": year, "month": month, "day": day})
        print("---- PDF CREATED SUCCESSFULLY! ----")
        http_response_code = 201
    except OSError:
        print("---- PDF CREATION FAILED :( ----")
        http_response_code = 404

    return redirect("http://localhost:5000/", code=http_response_code)


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

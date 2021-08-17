#!/usr/bin/python
# coding: utf-8
import math
import os

import cairo
from flask import Flask, send_file
from .functions import FILENAME, PDF_PATH, create_pdf, create_txt

# Flask app
app = Flask(__name__)

# File info
create_txt()
create_pdf()

@app.route("/")
def entry_point():
    print('---- in entry_point() ----')
    print('Current working directory: ', os.getcwd())
    print(f'saving file {FILENAME} in {PDF_PATH}')
    
    return send_file(PDF_PATH+'/'+FILENAME+'.pdf',
     attachment_filename=FILENAME+'.pdf',
     )


if __name__ == "__main__":
    print('---- Running App ---')
    print('Current working directory: ', os.getcwd())
    app.run(debug=True)

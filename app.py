#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, jsonify
from werkzeug.utils import secure_filename
import json
import os
import subprocess
import re
import shutil

UPLOAD_FOLDER = 'uploads/'
TIKA_EXE = 'external/'
TIKA_INPT = 'uploads/'
FULL = os.getcwd()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TIKA_EXE'] = TIKA_EXE
app.config['TIKA_INPT'] = TIKA_INPT
app.config['FULL'] = FULL


@app.route('/pdf2txt', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            file_path = request.values['file']
            file_name = file_path.split('\\')[-1]
            if len(file_path) == len(file_name):
                file_name = file_path.split('/')[-1]
            cmd = 'java -jar ' + '/'.join(app.config['FULL'].split('\\'
                    )) + '/' + '/'.join(app.config['TIKA_EXE'
                    ].split('\\')) + 'tika-app.jar -t  ' \
                + '/'.join(file_path.split('\\'))
            json_done = subprocess.check_output(cmd,
                    shell=True).decode('windows-1252')
            res = {'name': file_name, 'text': json_done}
            return jsonify(res)
        except:
            return 'WS Error !'
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
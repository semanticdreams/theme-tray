#!/usr/bin/env python

import os
import subprocess

python_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), '.venv/bin/python')

app_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'main.py')

subprocess.call([python_path, app_path])

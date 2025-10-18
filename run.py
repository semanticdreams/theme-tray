#!/usr/bin/env python

import os
import subprocess

subprocess.Popen(['uv', 'run', 'main.py'], cwd=os.path.abspath(os.path.dirname(__file__)))

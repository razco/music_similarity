'''
Created on Jun 9, 2017

@author: Raz
'''
# This module just adds this project to python path and runs the argument script
import sys
import os
import subprocess
project_base_path = os.path.dirname(os.path.realpath(__file__))
# run:
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
    print '%s <script_file> <script_input>' % script_name
    sys.exit(2)

os.environ['PYTHONPATH'] = '%s%s%s' % (os.environ['PYTHONPATH'], os.pathsep, project_base_path)

subprocess_params = [sys.executable] + sys.argv[1:]
sys.exit(subprocess.call(subprocess_params))

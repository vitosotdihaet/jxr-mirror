#!/usr/bin/sh
set -e

py -3.10 -m venv .env
source ./.env/Scripts/activate
py -m pip install -r requirements.txt
py -m pip uninstall opencv-python-headless -y
py -m pip install opencv-python

echo "All done!"
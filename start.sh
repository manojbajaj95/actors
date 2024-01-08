#!/bin/bash

# exit when any command fails
set -e

# apt install python-venv

if [ ! -d ".venv" ]; then
  # Script statements if $DIR exists.
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -q --upgrade -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

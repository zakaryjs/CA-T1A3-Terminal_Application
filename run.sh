#!/bin/bash

cd src/
python3 -m venv calendar-venv
source calendar-venv/bin/activate
pip install -r requirements.txt
clear
python3 main.py
#!/bin/bash

# to use this file run '. ./develop.sh' ensure the command starts with '.' so it runs in your current session.

echo "[DEBUG] Create python virtual environment"
python3 -m venv dev_env

echo "[DEBUG] Activate Python virtual environment"
. dev_env/bin/activate

echo "[DEBUG] Upgrade Python PIP"
pip install --upgrade pip

echo "[DEBUG] install python requirements for ansible"
pip install -r ./CI/ansible/requirements.txt

echo "[DEBUG] install python requirements for commitizen"
pip install -r ./CI/commitizen/requirements.txt

echo "[DEBUG] install python module cz_nfc"
pip install CI/gitlab_release/python-module/cz_nfc/.

echo "Development environment setup. when you have completed development you can clear the python virtual environment by running the command 'deactivate'"

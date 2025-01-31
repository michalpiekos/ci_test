#!/bin/bash
set -e

MY_DIR=$(readlink -f $(dirname $0))

echo "Set up test environment"
rm -rf /tmp/tests
python3 -m venv /tmp/tests
source /tmp/tests/bin/activate
cd /tmp/tests
python3 -m pip install -r $MY_DIR/requirements.txt

pytest $MY_DIR/tests.py -v -s
exit_code=$?
deactivate
rm -rf /tmp/tests
exit $exit_code


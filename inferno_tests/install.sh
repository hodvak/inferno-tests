#!/usr/bin/env bash

# this program add alias to the 'python tests.py' with the name test_ex

SCRIPT=$(readlink -f "$0")
BASEDIR=$(dirname "$SCRIPT")
echo "alias test_ex python $BASEDIR/tests.py" >> ~/.tcshrc
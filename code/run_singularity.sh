#!/bin/bash
CODEDIR=$1
RESULTSDIR=$2

cd $CODEDIR

export PYTHONUSERBASE=$SCRATCHDIR
export PATH=$PYTHONUSERBASE/bin:$PATH
export PYTHONPATH=$PYTHONUSERBASE/lib/python3.8/site-packages:$PYTHONPATH
pip install bayesian-optimization==1.1.0


python main.py $RESULTSDIR

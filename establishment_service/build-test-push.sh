#!/bin/bash

set -x

result=0 # OK

if [ $result == 0 ] ; then
    docker build -t ivorcaldwell/python-service-example .
    result=$?
fi

if [ $result == 0 ] ; then
    docker run --rm ivorcaldwell/python-service-example bash -c 'PYTHONPATH=.:$PYTHONPATH py.test'
    result=$?
fi

exit $result

#!/bin/bash

mongoimport --uri="mongodb://127.0.0.1/cabhyd" --collection=meta --jsonArray \
	<(python convert.py $1 <(./refactor.sh $2))

#!/bin/bash

mongoimport --uri="mongodb://127.0.0.1" --collection=cabhyd --jsonArray <(python convert.py)

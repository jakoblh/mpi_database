#!/bin/bash

# $1 : delivery csv file

sed -e "/^\[.*\]$/d" -e "s/Saccharose/Sucrose/g" <(python refactor_delivery.py <(sed "/^,*\$/d" $1))

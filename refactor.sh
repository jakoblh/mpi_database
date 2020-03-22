#!/bin/bash

sed "/^\[.*\]$/d" <(python refactor_delivery.py <(sed "/^,*\$/d" csv/delivery.csv))

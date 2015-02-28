#!/usr/bin/python

# Exploratory data analysis for Jeopardy data

import csv

with open('JEOPARDY_CSV.csv', 'rb') as fh:
    jeopardy = csv.reader(fh)

print jeopardy[1:3]

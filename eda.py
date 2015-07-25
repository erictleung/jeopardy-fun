#!/usr/bin/python

# Exploratory data analysis for Jeopardy data

import pandas as pd

with open('./data/JEOPARDY_CSV.csv', 'rb') as fh:
    jeopardy = pd.read_csv(fh)

print jeopardy[1:3]

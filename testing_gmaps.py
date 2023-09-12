# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:41:11 2023

@author: joema
"""

# Import Libraries
import gmaps_calc as gm # Import gmaps function
import pandas as pd # for reading csv

# load example journeys csv
journeys = pd.read_csv('test_journeys.csv')

mileages = [] # define empty mileages list

# iterate through dataframe
for i, r in journeys.iterrows():
    # if transit_mode not specified, calc mileage using calc_distance function 
    if type(r['transit_mode']) != str:
        miles = gm.calc_distance(r['origin'], r['destination'], mode=r['mode'], is_return=bool(r['is_return']))
    # if transit_mode specified, calc mileage using calc_distance function using with transit_mode
    else:
        miles = gm.calc_distance(r['origin'], r['destination'], mode=r['mode'], transit_mode=r['transit_mode'], is_return=bool(r['is_return'])) 
    
    # append mileage calculated to mileages list
    mileages.append(miles)
    
# create mileage column and assign calculated milages
journeys['mileage'] = mileages

# print dataframe and save as csv
print(journeys)
journeys.to_csv('journeys_calculated.csv', index=False)
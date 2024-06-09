# ENSF 692 Spring 2024
# June 04 Lab 9
# Exercises
#! /Users/rzhang/Desktop/U of C/ENSF692/ENSF692-Lab/Lab 9/env/lib
 
import numpy as np
import pandas as pd

# Refer to the weather data stored in WeatherData.xlsx


# Demo: creating/exporting a multi-dimensional DataFrame from Excel
#all_data = pd.read_excel("WeatherData.xlsx")
all_data = pd.read_excel("WeatherData.xlsx", usecols = [2,5,6,7,8,9,10], index_col = [0,1,2,3])
#all_data.to_excel("WeatherExport2.xlsx", index = True, header = True)

all_data.to_excel("test.xlsx", index = True, header = True)



print(all_data.index)
#print("1")
print(all_data.head(10))
print(all_data.describe())
print(all_data.columns)

# Add a column to calculate the delta for day (difference between max and min)

#all_data["Delta"] = all_data["Max Temp (°C)"] - all_data["Min Temp (°C)"]
#print(all_data)

# Find the average measurements for each month (across both years)

#print(all_data.groupby(level="Month").mean())

# Print the data in both locations on May 1, 2021

print(all_data.loc[:,2021,5,1])
print(all_data.loc[:,2021,5,:])


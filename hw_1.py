# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data



cwb_filename = '108061271.csv'

data = []

header = []

with open("108061271.csv") as csvfile:

    mycsv = csv.DictReader(csvfile)

    header = mycsv.fieldnames

    for row in mycsv:
        data.append(row)



#=======================================


# Part. 3

#=======================================


# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

MIN0 = 100000000.000
MAX0 = -100000000.000
MIN1 = 100000000.000
MAX1 = -100000000.000
MIN2 = 100000000.000
MAX2 = -100000000.000
MIN3 = 100000000.000
MAX3 = -100000000.000
MIN4 = 100000000.000
MAX4 = -100000000.000

redata = list(filter(lambda data: data['WDSD'] != "-99.000", data))

#for row in data:
#    if (row['WDSD'] != "-99.000" or row['WDSD'] != "-999.000"):
#        redata.append(row)

#print(redata[1][1])

for row in redata:
    
    if (row['station_id'] == 'C0A880'):
        if (float(row['WDSD']) > MAX0):
            MAX0 = float(row['WDSD'])
        elif (float(row['WDSD']) < MIN0):
            MIN0 = float(row['WDSD'])
    
    if (row['station_id'] == 'C0F9A0'):
        if (float(row['WDSD']) > MAX1):
            MAX1 = float(row['WDSD'])
        elif (float(row['WDSD']) < MIN1):
            MIN1 = float(row['WDSD'])

    if (row['station_id'] == 'C0G640'):
        if (float(row['WDSD']) > MAX2):
            MAX2 = float(row['WDSD'])
        elif (float(row['WDSD']) < MIN2):
            MIN2 = float(row['WDSD'])

    if (row['station_id'] == 'C0R190'):
        if (float(row['WDSD']) > MAX3):
            MAX3 = float(row['WDSD'])
        elif (float(row['WDSD']) < MIN3):
            MIN3 = float(row['WDSD'])

    if (row['station_id'] == 'C0X260'):
        if (float(row['WDSD']) > MAX4):
            MAX4 = float(row['WDSD'])
        elif (float(row['WDSD']) < MIN4):
            MIN4 = float(row['WDSD'])   
   

OUTPUT=[["C0A880", MAX0-MIN0],["C0F9A0", MAX1-MIN1],["C0G640", MAX2-MIN2],["C0R190", MAX3-MIN3],["C0X260", MAX4-MIN4]]
print(OUTPUT)



target_data = OUTPUT[:10]


#=======================================


# Part. 4

#=======================================

# Print result

print(target_data)

#========================================

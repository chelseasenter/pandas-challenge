# Dependencies and Setup
import pandas as pd
import math

# File to Load (Remember to Change These)
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

#Create a dataframe to view the initial data
purchase_data_df = pd.DataFrame(purchase_data)
purchase_data_df.head(20)

## dynamic bins - this will create a dynamic bins method

# step 1: create bins list
# start bins at 0, 10 - the minimum needed (if ages are less than 10)
bins = [0, 10]
list_appender = 10

## find the maximum age, then determine iterations by rounding up to the nearest 5 
# NOTE: (nothing changes if already divisible by 5 i.e. 20, 35, etc)
large_age = purchase_data_df["Age"].max()
iterations = math.ceil((large_age + 1) / 5) - 2

# skip the for loop to add anything if max number is less than 10...
# otherwise add a number 5 greater than previous list_appender to create bins (for x-interations)
if large_age < 10 :
    bins = [0, 10]
else:
    for x in range(iterations):
        bins.append(list_appender + 5)
        list_appender += 5
print(bins)

# step 2: create age_group list
# sets first label to "<10" (for when bins is just [0, 10]), then add string to list for x-iterations
age_groups = ["<10"]
for x in range(iterations):
    age_groups.append(f"{bins[x+1]}-{bins[x+1]+4}")
print(age_groups)

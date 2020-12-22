# pandas-challenge
pandas homework
#Heroes of PyMoli
##Table of Contents
 > Overview
 > Brainstorming/Pseudocode steps
 > Reflection and resource links

## Overview
As a "Lead Analyst" for an independent gaming company, I am tasked with analyzing the data for their most recent fantasy game Heroes of Pymoli. I will be applying what we've learned thus far from Python, Pandas library, and the Jupyter Notebook web application. Working mostly with data digestion, I am looking to derive the following: 
 > Player Count
 > Purchasing analysis of all data points
 > Gender demographics: analysis
 > Age Demographics
 > Top Spenders
 > Most Popular Items
 > Most Profitable Items

Enjoy!

## Brainstorming
Player Count
  [] - purchase ID is transaction ID, not player ID. Find total unique screen names ('SN')
     -can accomplish multiple ways: len("SN".unique()), df("SN").nunique()
  
Purchasing Analysis (Total)

    Number of Unique Items
      [] - .unique() with length or .count() of "Price"
    Average Purchase Price
      [] - "Price" .mean()
    Total Number of Purchases
      [] - equal to purchase ID, therefore len(purchase ID)
    Total Revenue
      [] - sum of "Price" column


Gender Demographics

    Percentage and Count of Female, Male and Other/Non-Disclosed Players
      [] - unique IDs first (purchase ID can have duplicate SNs!)
      [] - count gender occurances using: value_counts
      [] - set each count to divide by total from counts combined (SHOULD equal total unique IDs)
      

Purchasing Analysis (Gender)

  The below each broken by gender (per Gender group)

    Purchase Count
      - total purchase count by Gender
      [] - sum grouped genders by purchase ID count
    Average Purchase Price
      [] - count purchase ID for each gender group
      [] - for each gender, divide sum from previous step by count
    Total Purchase Value
      [] - Sum of Price per Gender group
    Average Purchase Total per Person by Gender
      [] - sum of Price/People.count() per gender group


Age Demographics

  The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
  
    Purchase Count
      - total purchases by age group (binning)
      [] - bin groups (0, 10, 15, 20, 25, 30, 35, 40, 45, etc)
      [] - make bins dynamic - find highest number, round up to nearest 5, divide by 5
          - i.e. if number is 43, round up (45), divide by 5 (9), will give how many iterations (1-9, not 0-9)
            num_bins = [0, 10]
            list_appender = 10
            large_age = highest number in age column
            round_up = round(large_age/5)
            iterations = round_up/5
            num_bins.append(list_appender+5) for x in range(iterations)
    Average Purchase Price
     
    Total Purchase Value
    
    Average Purchase Total per Person by Age Group




Top Spenders

  Identify the the top 5 spenders in the game by total purchase value, then list (in a table):

    SN
    Purchase Count
    Average Purchase Price
    Total Purchase Value




Most Popular Items

  Identify the 5 most popular items by purchase count, then list (in a table):

    Item ID
    Item Name
    Purchase Count
    Item Price
    Total Purchase Value




Most Profitable Items

  Identify the 5 most profitable items by total purchase value, then list (in a table):

    Item ID
    Item Name
    Purchase Count
    Item Price
    Total Purchase Value



As final considerations:

  You must use the Pandas Library and the Jupyter Notebook.
  You must submit a link to your Jupyter Notebook with the viewable Data Frames.
  You must include a written description of three observable trends based on the data.
  See Example Solution for a reference on expected format.

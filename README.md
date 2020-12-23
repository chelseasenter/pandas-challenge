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
  [x] - purchase ID is transaction ID, not player ID. Find total unique screen names ('SN')
     -can accomplish multiple ways: len("SN".unique()), df("SN").nunique()
  
Purchasing Analysis (Total)

    Number of Unique Items
      [x] - .unique() with length or .count() of "Price"
    Average Purchase Price
      [x] - "Price" .mean()
    Total Number of Purchases
      [x] - equal to purchase ID, therefore len(purchase ID)
    Total Revenue
      [x] - sum of "Price" column


Gender Demographics

    Percentage and Count of Female, Male and Other/Non-Disclosed Players
      [x] - unique IDs first (purchase ID can have duplicate SNs!)
      [x] - count gender occurances using: value_counts
      [x] - set each count to divide by total from counts combined (SHOULD equal total unique IDs)
      

Purchasing Analysis (Gender)

  The below each broken by gender (per Gender group)

      [x] - groupby "Gender", then run the following functions with the [columns] designated
    Purchase Count
      [x] - .count() ["Purchase ID"] to get total purchase count per gender type
    Average Purchase Price
      [x] - from the 
    Total Purchase Value
      [x] - Sum of Price per Gender group
    Average Purchase Total per Person by Gender
      [x] - sum of Price/People.count() per gender group

 
     [x] Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
     [x] Create a summary data frame to hold the results
     [x] Optional: give the displayed data cleaner formatting
     [x] Display the summary data frame

Age Demographics

  The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
     
     Binning:
       - this section requires binning, so I decided to create a dynamic bins script. If another csv file 
        with the same formatting is downloaded, the script will automatically expand or shrink the number of bins
      [x] - bin groups (0, 9, 14, 19, 24, 29, 34, 39, 44, etc) to include (but not equal to) - <10, 10-14, 15-19, 20-24, etc
      [x] - make bins dynamic - find highest number, round up to nearest 5, divide by 5
          - i.e. if number is 43, round up (45), divide by 5 (9), will give how many iterations (1-9, not 0-9)
            num_bins = [0, 9]
            list_appender = 10
            large_age = highest number in age column
            round_up = round(large_age/5)
            iterations = round_up/5
            num_bins.append(list_appender+5) for x in range(iterations)
     [x] - verify bins work
     
    Age Demographics (total players, percentage of players)
     [x] - create Age Groups column in purchase_data_df
     [x] - age_count - drop duplicates of players, count values of Age Groups
     [x] - age_pct - divide previous number by number of players (576 in this case)
    
    Purchase Count (age_pc)
     [x] - age_gb = groupby Age Groups
     [x] - of age_gb, count Purchase IDs (number of purchases)
    Average Purchase Price (age_app)
     [x] - age_gb, mean of Price column (average purchase price per age group)
    Total Purchase Value (age_tpv)
     [x] - age_gb, add up Price column (sum of price per age group)
    Average Purchase Total per Person by Age Group (age_atppp)
     [x] - age_tpv divided by the total count of players per age group (age demographics Age Totals)

Top Spenders

  Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
    SN, Purchase Count, Average Purchase Price, Total Purchase Value

    [x] - player_gb = groupby SN
    [x] - player_pc = count Purchase ID of player_gb
    [x] - player_app = mean Price of player_gb
    [x] - player_tpv = sum Price of player_gb
    [x] - create dataframe
    [x] - sort data frame (ascending=False)
    [x] - format tpv (would  not sort correctly if formatted in dataframe setup)


Most Popular Items

  Identify the 5 most popular items by purchase count, then list (in a table):
   Item ID, Item Name, Purchase Count, Item Price, Total Purchase Value

    [x] - create dataframe using purchase_data_df columns: Item ID, Item Name, Item Price
    [x] - item_gb/pc/app/tpv = same process as previous sections
    [x] - create analysis dataframe, sort and format

Most Profitable Items

  Identify the 5 most profitable items by total purchase value, then list (in a table):
    Item ID, Item Name, Purchase Count, Item Price, Total Purchase Value

    [x] - using previous item_analysis_df, sort the values by TPV
    [x] - format


Reflections:

This homework was more difficult than the last, particularly due to the UI of Jupyter Notebook. I found it difficult to see the code as a whole while writing my script and often struggled visually comprehending how each section connected. To me, it felt more like each box was its own python file, and for whatever reason that perception was hard to shake. 

After looking at the data, I am interested add further analysis on the top spenders. Specifically, I would like to look at the top 50 spenders and their gender designations, how if they bought the most popular or most expensive items, if there were any outliers, etc.

Resource Links:
[Kite Answers in general, but here's an example of an answer I used for finding max()](https://www.kite.com/python/answers/how-to-find-the-max-value-of-a-pandas-dataframe-column-in-python#:~:text=max()%20to%20find%20the,from%20the%20previous%20result%20column%20.)
[Pandas' Documentation was EXTREMELY helpful (albeit confusing to navigate and understand at first](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
[And of course, Youtube was vital when my mind had had it with reading](https://www.youtube.com/watch?v=W5wo3KIUuw4)

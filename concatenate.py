# -*- encoding: utf-8 -*- 
"""
concatenate.py

Creates MySQL databases and .csv files from given Make School Summer Academy Feedback datasets.
"""

import glob
import csv

# UNCLEANED DATA FILEPATHS
FILEPATH = "./datasets/raw/"
FILEPATH_YEAR_ONE = FILEPATH + "2016/"
FILEPATH_YEAR_TWO = FILEPATH + "2017/"

# UNCLEANED YEAR ONE DATASETS
YEAR_ONE_DATASETS = glob.iglob(FILEPATH_YEAR_ONE + "Anon Week * Feedback - *.csv")

# WTF WEEK 8 ???
UNCLEANED_WEEK_EIGHT_2016 = FILEPATH_YEAR_TWO + "Week 8 Feedback (2016, incomplete) - results"

# Destinations for cleaned data
DATASETS = [
    "2016.csv",
    "2017.csv",
    "2016_2017.csv",
    "2016_WEEK_8.csv", # week 8 data seperately
]

# ABBREVIATION TO LOCATION LOOKUP 
LOCATIONS = {
    "SG" : "Singapore",
    "LA" : "Las Vegas",
    "SF" : "San Francisco",
    "HK" : "Hong Kong",
    "NY" : "New York",
    "SV" : "Silicon Valley"
}

# COLUMN INDEX LOOKUP
DATASETS 

def main():

    # create the .csv files for the concatenated datasets
    for filename in DATASETS:
        with open("./datasets/" + filename, "w") as dataset:
            # create a filewriter to write a row, formatted
            wr = csv.writer(dataset, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)

            # create headers
            wr.writerow(["STUDENT ID",
                         "YEAR", 
                         "WEEK", 
                         "TRACK", 
                         "LOCATION",
                         "SATISFACTION",
                         "PACE RATING",
                         "DATETIME"])

    """
    2016 Datasets
    """
    for filepath in YEAR_ONE_DATASETS:

        if filepath == UNCLEANED_WEEK_EIGHT_2016:
            pass
       
        with open(filepath, "wr") as uncleaned_dataset:
            reader = csv.reader(uncleaned_dataset)
            writer = csv.writer(dataset, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)

            configure_lookup_table(reader[0])

            # configure 
            for row, row_number in reader:

                if row_number == 0:
                    pass

            # student id
            # check if exists

            # track
            # check if exists

            # week
            # parse from file name

            # location
            # parse from name
            # lookup and convert

            # satisfaction
            # double

            # year
            # only include for last two items
            
        # now we deal with week 8

    """
    2017 Datasets
    """

if __name__ == "__main__":
    main()


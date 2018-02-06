# -*- encoding: utf-8 -*- 
"""
concatenate.py

Creates MySQL databases and .csv files from given Make School Summer Academy Feedback datasets.
"""

import glob
import csv
import os

# UNCLEANED DATA FILEPATHS
FILEPATH = "./datasets/raw/"
FILEPATH_YEAR_ONE = FILEPATH + "2016/"
FILEPATH_YEAR_TWO = FILEPATH + "2017/"

# WTF WEEK 8 ???
UNCLEANED_WEEK_EIGHT_2016 = FILEPATH_YEAR_TWO + "Week 8 Feedback (2016, incomplete) - results"

# UNCLEANED YEAR ONE DATASETS
YEAR_ONE_DATASETS = glob.iglob(FILEPATH_YEAR_ONE + "Anon Week * Feedback - *.csv")

# ABBREVIATION TO LOCATION LOOKUP 
LOCATIONS = {
    "SG" : "Singapore",
    "LA" : "Las Vegas",
    "SF" : "San Francisco",
    "HK" : "Hong Kong",
    "NY" : "New York",
    "SV" : "Silicon Valley",
    "TA" : "Taipei",
    "TY" : "Tokyo"
}

# Destinations for cleaned data
DATASETS = [
    "2016_2017.csv",
]

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
    PRE
    """
    for filepath in glob.iglob(FILEPATH_YEAR_ONE + "Anon Week * Feedback - *.csv"):
        if "Singapore" in filepath:
            os.rename(filepath, filepath[:-13] + "SG.csv")

        if "Taipei" in filepath:
            os.rename(filepath, filepath[:-10] + "TA.csv")

        if "Tokyo" in filepath:
            os.rename(filepath, filepath[:-9] + "TY.csv")

    """
    2016 Datasets
    """
    for filepath in YEAR_ONE_DATASETS:

        print(filepath)

        # ignore week 8
        if filepath == UNCLEANED_WEEK_EIGHT_2016:
            pass
       
        with open(filepath, "r") as uncleaned_dataset:

            # read in dataset using CSV reader module
            reader = csv.reader(uncleaned_dataset)

            for row_number, row in enumerate(reader):
                    
                # set the headers
                if row_number == 0:
                    headers = parse_headers(row)
                    continue

                # parse week and location from file path
                week_loc = filepath[-19:-4]

                # set empty values for all columns
                student_id = None
                year = 2016
                week = int(week_loc[0])
                track = None
                loc = LOCATIONS[week_loc[-2:]]
                satisfaction = None
                pace_rating = None
                datetime = None

                for column_number, item in enumerate(row):

                    item_data = item
                    item_type = headers[column_number]

                    # student id
                    if item_type is "STUDENT ID":
                        student_id = item_data

                    # year
                    if item_type is "YEAR":
                        year = item_data

                    # week  
                    if item_type is "WEEK":
                        item_data = int(item_data[-1])
                        week = item_data

                    # track
                    if item_type is "TRACK":
                        track = item_data

                    # location
                    if item_type is "LOCATION":
                        loc = LOCATIONS[item_data]

                    # satisfactory rating
                    if item_type is "SATISFACTION":
                        if item_data != "#REF!":
                            satisfaction = int(item_data) * 2

                    # pace rating
                    if item_type == "PACE RATING":
                        if item_data != "#REF!":
                            pace_rating = int(item_data) * 2

                    # Date
                    if item_type is "DATETIME":
                        datetime = item_data

                for filename in DATASETS:
                    with open("./datasets/" + filename, "a") as dataset:
                        # create a filewriter to write a row, formatted
                        wr = csv.writer(dataset, delimiter=',',
                                       quotechar='|', quoting=csv.QUOTE_MINIMAL)

                        # write row
                        wr.writerow([student_id,
                                     year,
                                     week,
                                     track,
                                     loc,
                                     satisfaction,
                                     pace_rating,
                                     datetime])


def parse_headers(header_row):

    headers = {}

    for column_number, header in enumerate(header_row):

        header = header.lower()
        header_type = ""

        # student id
        if "#" in header or "ID" in header:
            header_type = "STUDENT ID"

        # track
        if "track" in header:
            header_type = "TRACK"

        # location
        if "loc" in header:
            header_type = "LOCATION"

        # week
        if "week" in header:
            header_type = "WEEK"

        # satisfaction rating
        if "satisfaction" in header or "num" in header:
            header_type = "SATISFACTION"

        # pace
        if "pac" in header:
            header_type = "PACE RATING"

        # date
        if "timestamp" in header or "date" in header:
            header_type = "DATETIME"
    
        headers[column_number] = header_type

    return headers

if __name__ == "__main__":
    main()


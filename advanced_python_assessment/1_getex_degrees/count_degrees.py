# Write a function which reads in a csv file, and then returns
# a dictionary where keys are (standardized) degrees and
# values are their frequencies in the file

# your function will be tested with the data faculty.csv

# use regular expressions to treat PhD and Ph.D. the same way
# (considers them to be the same string)

# no pandas

"""
notes:
https://regexr.com/ is a useful site for testing Regular Expressions
"""

def read_data(filename):
    """Returns a list of lists representing rows of the csv file data

    arguments: filename is the name of a csv file as a string
    returns:
    data: list of lists of strings
    """
    import csv
    filename = 'faculty.csv'
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            data.append(list(row))
    return data

def get_prof_degrees(data):
    """Extracts the degrees from 1-eth column of the data, rows 1-eth through all
    arguments: the data from the csv
    returns:
    degrees: a list of the degrees
    """
    degrees = []
    for row in data[1:]:
        degrees.append(row[1])
    return degrees

def count_degrees_beta(degrees):
    from collections import defaultdict
    d = defaultdict(int)
    for degree in degrees:
        d[degree] += 1
    return dict(d)

def process_degrees(degrees):
    import re
    result = []
    for degree in degrees:
        if re.search(".{0,1}Ph.{0,1}D.{0,1}", degree):
            result.append("PhD")
        else:
            result.append(degree)
    return result

def count_degrees(csv_file_name):
    filename = 'faculty.csv'
    degrees = get_prof_degrees(read_data(filename))
    degrees = process_degrees(degrees)
    return (count_degrees_beta(degrees))

filename = 'faculty.csv'
print(count_degrees(filename))

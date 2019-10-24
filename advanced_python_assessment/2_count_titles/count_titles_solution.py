from collections import Counter

def read_data(filename):
    """Returns a list of lists representing rows of the csv file data

    arguments: filename is the name of a csv file as a string
    returns:
    data: list of lists of strings
    """
    import csv
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        for row in csv_reader:
            data.append(list(row))
    return data

def get_prof_titles(data):
    """Extracts the degrees from 1-eth column of the data, rows 1-eth through all
    arguments: the data from the csv
    returns:
    titles: a list of the titles
    """
    titles = []
    for row in data[1:]:
        titles.append(row[2])
    return titles

def count_titles(csv_file_name):
    pass
    data = read_data(csv_file_name)
    titles = get_prof_titles(data)
    #print(titles)
    titles_corrected = []
    for title in titles:
        title = title.replace(' is ', ' of ')
        titles_corrected.append(title)


    #print(Counter(titles_corrected))
    d = dict(Counter(titles_corrected))
    return d

count_titles('faculty.csv')

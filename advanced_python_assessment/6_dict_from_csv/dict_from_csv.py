import re

def read_data(filename):# gets data from the csv file, filename
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

def get_dict():
    data = read_data('faculty.csv')
    d = {}

    for row in data:
        name = row[0]
        last_name= re.findall('[A-Za-z]*$', name)[0]
        if last_name in d:
            d[last_name].append(row[1:])
        else:
            d[last_name] = [row[1:]]
    #print(d)
    return(d)

print(get_dict())

# this seems to be right, but on submission I'm getting
# an AssertionError about n == facultycsv.count('\n')

import re

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

def get_emails(data):
    """Extracts the degrees from 1-eth column of the data, rows 1-eth through all
    arguments: the data from the csv
    returns:
    emails: a list of the emails
    """
    emails = []
    for row in data[1:]:
        emails.append(row[3])
    return emails

def emails(csv_file_name):
    data = read_data(csv_file_name)
    emails = get_emails(data)
    return emails

def unique_domains(emails):
    for i, email in enumerate(emails):
        emails[i] = re.findall("(?<=@).*", email)[0]
    return list(set(emails))




data = read_data('faculty.csv')
emails = get_emails(data)
print(unique_domains(emails))

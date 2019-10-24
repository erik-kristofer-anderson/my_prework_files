import csv

def read_data(filename): # gets data from the csv file, filename
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

def get_emails(data): # gets emails, given the data list
    """Extracts the degrees from 1-eth column of the data, rows 1-eth through all
    arguments: the data from the csv
    returns:
    emails: a list of the emails
    """
    emails = []
    for row in data[1:]:
        emails.append(row[3])
    return emails

def emails(csv_file_name): # gets the emails, given the csv file name
    data = read_data(csv_file_name)
    emails = get_emails(data)
    return emails

def write_to_csv(list_of_emails):
    with open('emails.csv', mode='w') as emails_file:
        emails_writer = csv.writer(emails_file)
        emails_writer.writerow(['list_of_emails'])
        for email in list_of_emails:
            emails_writer.writerow([email])




data = read_data('faculty.csv')
emails = get_emails(data)
write_to_csv(emails)

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values.
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    import csv
    filename = 'football.csv'
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        t = []
        for row in csv_reader:
            t.append(list(row))
        return(t)



def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    # apparently goals is data
    data = goals
    diffs = []
    for t in data[1:]:
        diff = abs(int(t[5]) - int(t[6]))
        diffs.append(diff)
    min = max(diffs)
    for i, diff in enumerate(diffs):
        if diff < min:
            min = diff
            least_diff_index = i
    return least_diff_index

def get_team(index_value, parsed_data):
    """Returns the team name at a given index.

    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above

    Returns: the team name
    """
    return parsed_data[index_value + 1][0]

# filename = 'football.csv'
# data = (read_data(filename))
# least_diff_index = get_index_with_min_abs_score_difference(data)
# print(least_diff_index)
# print(get_team(least_diff_index, data))


footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))

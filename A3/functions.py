import os
import re

import matplotlib.pyplot as plt


def openFile(file_path, argument):
    """ Checks if the files exists in the path passed in and returns the opened file
        with the argument provided """
    file = None
    list_arguments = ['r', 'w', 'w+', 'a', 'rb',
    'r+', 'rb+', 'wb', 'wb+', 'ab', 'a+', 'ab+']
    if os.path.exists(file_path):
        if argument in list_arguments:
            try:
                file = open(file_path, argument)
                return file
            except FileNotFoundError:
                print("Good bye!")
                exit(1)
        print("Given argument: {} isn't predefined!".format(argument))
    else:
        print("File {} could not be found!".format(file_path))
    return file


def _removePattern(data):
    """ Removes spaces from the given data """
    removed_pattern = []
    # Checks if the data is null
    if len(data) <= 0:
        print("Length of data is null!")
        # Returns none if null
        return None

    # If not finds a pattern and replaces it
    # with the chosen character
    for line in data:
        try:
            string = re.sub(' +', ',', line)
        except:
            pass
        removed_pattern.append(string)
    # Then returns the data after
    return removed_pattern


def _dateSplit(data, argument):
    """ Splits a given data by some argument """
    altered_data = []
    # Checks if data is null
    if len(data) <= 0:
        print("Length of data is null")
        # Returns none if null
        return None

    # Iterates through the data
    for line in data:
        # Splitting each line of the data
        split = line.split(argument)
        try:
            # Accessing the data from the index 0 till 7
            # Assuming date is always between index 0 and 7
            date = line[0:7]
        except:
            # if not pass it
            pass

        # Splitting the data to get the year and month
        dates = date.split('/')
        month = int(dates[1]) * 0.083
        rounded_month = "{:2.3}".format(month)

        # Making a new string based on the recently new data
        # which is the normalisations of the month
        newstring = str(int(dates[0])+float(rounded_month))
        # The old is replaced with the new string using a list comprehension
        split = [word.replace(date, newstring) for word in split]
        # appended into the data and return it
        altered_data.append(split)
    return altered_data


def write_tofile(data, file):
    """ Opens a file and writes the passed in data to a file """
    if len(data) <= 0:
        return False

    for line in data:
        file.write(line + '\n')
    return True


def _chunks(list_, offset):
    """ Divides a list into smaller chunks using the yield function """
    for i in range(0, len(list_), offset):
        yield list_[i:i + offset]


def checkSize(n, m, l):
    """ Checks if the given integers are equal to one another """
    # print("Function checkSize", n, m, l)
    return True if n == m and l == m else False


def change(list_):
    """ Changes some elements into lists, in here its changing tuples into lists """
    return [list(element) for element in list_]


def _tofloat(list_):
    """ Changes a list of strings into floats using the float function"""
    return [float(i) for i in list_]


def _average(list_):
    """ It calculates the average of a given list of tuples """
    average_list = []
    # Iterates through the list
    for line in list_:
        sum1 = 0
        average1 = 0
        sum2 = 0
        average2 = 0
        i = 0
        j = 0
        # Iterates through each data in the list
        while len(line) - i != 0 and len(line[i]) - j != 0:
            sum1 = sum1 + float(line[i][j])
            average1 = sum1 / len(line)
            sum2 = sum2 + float(line[i][j + 1])
            average2 = sum2 / len(line)
            i += 1
        # It formats the averges and appends them into the list to be returned
        tuple1 = ("{:5.3f}".format(average1), "{:5.3f}".format(average2))
        average_list.append(tuple1)
    return average_list


def _retrieve(list_):
    """ Makes a list of tuples with the desired elements in the list """
    list_data = []
    size = len(list_)
    # Iterates through the list, using an even and odd number generator
    for i in range(size):
        # even index stored in the list_ are x-axis values and odd numbers
        # are y-axis values
        c1data = 2 * (i - 1)
        c2data = (2 * i) - 1

        # Checks if there is any values out of bounds
        # if not continue and break respectively
        if c1data < 0 or c2data < 0:
            continue
        if c1data > size or c2data > size:
            break
        tuple_ = (list_[c1data], list_[c2data])
        # appends it to the list and is returned
        list_data.append(tuple_)
    return list_data

def makeList(fullpath):
    list1 = []
    if type(fullpath) == str:
        #checks if the parameter given is a string
        fr = open(fullpath, 'r')
        data = [line.rstrip('\n') for line in fr]
        for i in data:
            l = i.split(' ')
            #makes a list with the space in between
            tuple1 = (l[0], l[1])
            #makes a tuple from the first and second values of list
            list1.append(tuple1)
    return list1

# def makeList(full_path):
#     """ Makes a list of the data with the given file path, passed in as argument """
#     # print(data_full_path)
#     full_list = []
#     argument = ' '
#     # Checks if the file exists or not
#     f = openFile(full_path, 'r')
#     if not f:
#         exit(1)

#     # Reads the data from the list and appends it to a list
#     lines = [line.rstrip('\n') for line in f]
#     f.close()
#     # Iteration through the data and splits by a space
#     for line in lines:
#         try:
#             split = line.split(argument)
#         except:
#             pass
#         # Saves it to a tuple to be appended to a list
#         year_data_tuple = (split[0], split[1])
#         full_list.append(year_data_tuple)
#     # Checks if list is empty, if not it returns the list
#     return full_list if len(full_list) != 0 else None
def makeList(fullpath):
    list1 = []
    if type(fullpath) == str:
        fr = open(fullpath, 'r')
        data = [line.rstrip('\n') for line in fr]
        for i in data:
            l = i.split(' ')
            tuple1 = (l[0], l[1])
            list1.append(tuple1)
    return list1


def plotList(name, list_tuples, color, xaxis, yaxis):
    """ Plots a given list into a screen with the passed in arguments """
    # Creates new empty lists for the x and y axis respectively
    x = []
    y = []
    # Goes through the list of tuples
    # And appends it to its corresponding list
    for (xp, yp) in list_tuples:
        x.append(xp)
        y.append(yp)
    # Plots a 2-dimensional graph
    # With the corresponding values of x and y
    plt.plot(x, y, color, label=name, markersize=2)
    # Shows the legend, which is the label name in the argument
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.legend()


def makeAverageList(input_file, column_v1=0, column_v2=0, number_months=0):
    """ It makes averages lists given the file and the columns to average over using
    a granularity of months """
    columns_ = []

    # Opens a file and read the data of the file into a list
    file = openFile(input_file, 'r')
    lines = [line.rstrip('\n') for line in file]
    # Closes the file if not closed
    if not file.close():
        file.close()

    # Iterates the data and appends it to a list if the columns are found
    for element in lines:
        lines_split = element.split(',')
        for i in range(len(lines_split)):
            if i == column_v1 or i == column_v2:
                columns_.append(lines_split[i])
            else:
                pass

    # Requests the data to be retrieved from the list
    # And divides it into chunks
    data_list = _retrieve(columns_)
    list1 = list(_chunks(data_list, number_months))
    # Asks the functions to average over the data
    # print(list1)
    average_list = _average(list1)
    # Returns the data
    return average_list


def correctFile(input_file, output_file):
    """ Corrects a passed in file and by removing the unnecessary characters
    from the file and appends it to a new file """
    removed_pattern = []
    data = []
    full_data = []

    # Requests for the parameter files to be open for reading and writing
    _readfile = openFile(input_file, 'r')
    _writefile = openFile(output_file, 'w')
    # Checks if they exist and are opened
    if _readfile and _writefile:
        pass
    elif _readfile and not _writefile:
        # If not the write file is created as the inputfile must exist
        print("File, {} could't be found! \n File being created.".format(output_file))
        _writefile = open(output_file, 'w')

    # Reads the data in the file and closes it
    lines = [line.rstrip('\n') for line in _readfile]
    _readfile.close()
    # Asks the function to remove the pattern
    removed_pattern = _removePattern(lines)
    # Requests for the data to be split
    data = _dateSplit(removed_pattern, ',')

    # Iterates through to join each one with a comma
    for line in data:
        string_ = ','.join(line)
        full_data.append(string_)

    success = write_tofile(full_data, _writefile)
    # Closes the file
    _writefile.close()
    return success


#                                              UPPER VAR    LOWER VAR
def plotWithError(name, type_s, list_tuples, list_tuples2, list_tuples3, color1='m', color2='r', x_name='X',
                  y_name='Y'):
    """ It plots lists of tuples with the nominal values and their corresponding
    lower and upper variation """
    # The corresponding length of each list is stored to be checked
    n = len(list_tuples)
    m = len(list_tuples2)
    k = len(list_tuples3)
    if checkSize(n, m, k):
        pass
    else:
        # Exits if all values are not equal
        print("Size of lists not equal: ", n, m, k)
        exit(1)
    _plot(list_=list_tuples, list_2=list_tuples2, list_3=list_tuples3,
          type_=type_s, name_=name, nominalColour=color1, uncertaintyColour=color2)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    return


def _plot(list_, list_2, list_3, type_, name_, nominalColour, uncertaintyColour):
    """ This function is an extension of plotWithError """
    err_low_variation = []
    err_upp_variation = []
    x = []
    y = []
    # The following for loops append the data into their corresponding list
    # to be plotted
    for (xp, yp) in list_:
        x.append(xp)
        y.append(yp)

    for (xerr, yerr) in list_2:
        err_upp_variation.append(yerr)

    for (xerr, yerr) in list_3:
        err_low_variation.append(yerr)

    # Converted to floats to be drawn to the screen
    err_low_variation = _tofloat(err_low_variation)
    err_upp_variation = _tofloat(err_upp_variation)
    x = _tofloat(x)

    # fill_between used to draw the error bands
    plt.fill_between(x, err_low_variation, err_upp_variation, color=uncertaintyColour, label=type_)
    # Shows the legend before the nominal curve
    plt.legend()  # when there is multiple plots then uncomment this line of code
    # Plots the nominal curve
    plt.plot(x, y, color=nominalColour, label=name_)
    # plt.legend() # when there is only one plot of one data set, one plot is related to the number of times this function is called
    # Labels the x and y-axis
    return


def oddFormat(file_path, output):
    """ Picks the odd indexes """
    # Opens the files for read and write respectively
    file = openFile(file_path, 'r')
    file2 = openFile(output, 'w')
    # reads the data in the first file
    lines = [line.rstrip('\n') for line in file]
    # Splits the first character of the data to have separate lists of the data
    splitData = [lines[i].lstrip(' ') for i in range(0, len(lines), 2)]
    # print(splitData)
    # Invokes the removePattern function to remove the spaces between the elements in the data
    list_ = _removePattern(splitData)
    # Then writes it to a file
    write_tofile(list_, file2)
    return

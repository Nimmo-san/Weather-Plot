import matplotlib.pyplot as plt
import re


def makeList(data_full_path):
    full_list = []
    try:
        f = open(data_full_path, 'r')
    except FileNotFoundError:
        print("FILE COULD NOT BE OPENED!")
        exit(1)

    lines = [line.rstrip('\n') for line in f]
    for line in lines:
        try:
            split = line.split(' ')
        except:
            pass
        year_data_tuple = (split[0], split[1])
        full_list.append(year_data_tuple)
    if len(full_list) != 0:
        return full_list


def plotList(name, list_tuples, color, xaxis, yaxis):
    x = []
    y = []
    for i in range(len(list_tuples)):
        for j in range(len(list_tuples[i]) - 1):
            xi = list_tuples[i][j]
            yi = list_tuples[i][j + 1]
            x.append(xi)
            y.append(yi)
    plt.plot(x, y, color, label=name)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.legend()


def remove_pattern(data):
    removed_pattern = []
    if len(data) <= 0:
        print("Length of data is null!")
        return None

    for line in data:
        try:
            string = re.sub(' +', ',', line)
        except:
            pass
        removed_pattern.append(string)
    return removed_pattern


def split_date(data):
    altered_data = []
    if len(data) <= 0:
        print("Length of data is null")
        return None

    for line in data:
        split = line.split(',')
        try:
            date = line[0:7]
        except:
            pass

        dates = date.split('/')
        month = int(dates[1]) * 0.083
        roundedmonth = "{:2.3}".format(month)

        newstring = str(int(dates[0])+float(roundedmonth))
        split = [word.replace(date, newstring) for word in split]
        altered_data.append(split)
    return altered_data


def write_File(data, file_opened):
    if len(data) <= 0:
        return False

    for line in data:
        file_opened.write(line + '\n')
    return True


def correctFile(input_file, output_file):
    removed_pattern = []
    data = []
    full_data = []

    try:
        toreadfile = open(input_file, 'r')
        writefile = open(output_file, 'w')
    except FileNotFoundError:
        print("File, {} couldn't be found!".format(input_file))
        print("File, {} could't be found! \n File being created.".format(output_file))
        writefile = open(output_file, 'w+')
        exit(1)

    lines = [line.rstrip('\n') for line in toreadfile]
    removed_pattern = remove_pattern(lines)
    data = split_date(removed_pattern)

    for line in data:
        string1 = ','.join(line)
        full_data.append(string1)

    success = write_File(full_data, writefile)
    toreadfile.close()
    writefile.close()
    return success


# # file = 'E:/University\Coding\A3ProjectPython\ProjectData\Data.nh.txt'
# file = '..\A3\Data.nh.txt'
# print(make_list(file))

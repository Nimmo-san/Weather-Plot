import matplotlib.pyplot as plt

from classes import Analysis
from functions import makeList, plotList, correctFile, makeAverageList, plotWithError

# Constant variables to be used globally
parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh', '_out.nh', '_ns',
                    '_out.ns', '_sh', '_out.sh',
                    '_tropical', '_out.tr']
test_data = '..\A3/textfiles\FakeData.txt'
test_output = '..\A3/textfiles/Here.txt'
monthly_input = '\Data.monthly'
monthly_output = '/Parsed.monthly'
colours = {1: 'darkcyan', 2: 'c', 3: 'aqua'}
tuple_columns = (0, 1, 8, 9, 10, 11)

# The test data to be plotted
data_file = '..\A3/textfiles\Data.nh.txt'
# Requests for the data in the file to be appended into a list
list_tuples = makeList(data_file)

plotList('DEAD!', list_tuples, 'r', 'DEAD I', 'DEAD II')
# The figure is saved and displayed
plt.savefig('..\A3/images/test.png')
plt.show()

correctFile(test_data, test_output)

# Iterates through the files stored
# and applies the correctFile function
n = len(IO_monthly_files)
for i in range(n - 1):
    # The input files are in the index where index is an even number
    # output files are in odd index values
    input_file_index = 2 * (i - 1)
    output_file_index = 2 * i - 1
    # If they exceed some value it either continues or breaks respectively
    if input_file_index < 0 and output_file_index < 0:
        continue
    if input_file_index > n or output_file_index > n:
        break
    # The input and output files full path is formed here
    input_file = parent_path + monthly_input + IO_monthly_files[input_file_index] + '.txt'
    output_file = parent_path + monthly_output + IO_monthly_files[output_file_index] + '.txt'
    # The function is invoked with the necessary parameters
    correctFile(input_file, output_file)

# Averaging over three different periods for a same file
period1 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, 1)
period2 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, 24)
period3 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, 48)
# Plots the list for each of the averaged periods using different names and colours
plotList('p1', period1, 'm', 'x', 'y')
plotList('p2', period2, 'k', 'x', 'y')
plotList('p3', period3, 'r', 'x', 'y')
# Shows the plotted list
plt.show()

# Columns (0,1), (8,9) are used to plot the function with the correspoding error
# using plotWithError function
nominal = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, 12)
uncertainty = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 8, 12)
uncertainty2 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 9, 12)
plotWithError('nominal', 'uncertainty', nominal, uncertainty, uncertainty2, colours[1], colours[3])
plt.show()

# An instance of the class Analysis, two correct format files and their correspoding
# titles are added and printed respectively
ana = Analysis()
ana.addFile(monthly_output + '_out.ns', 'ns')
ana.addFile(monthly_output + '_out.tr', 'tr')
ana.updateLists(tuple_columns, 48, 'type I uncertainty', 'type II uncertainty', 0, 2037)
ana.printLists()

ana.plotWithErrors(1, 1, 0)
ana.scatterPlot(0, 1, 'me')

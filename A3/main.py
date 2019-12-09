import matplotlib.pyplot as plt

from classes import Analysis
from functions import plotList, makeList, correctFile, makeAverageList, plotWithError

# Constants necessary for the project
parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh.txt', '_out.nh.txt', '_ns.txt',
                    '_out.ns.txt', '_sh.txt', '_out.sh.txt',
                    '_tropical.txt', '_out.tr.txt']
monthly_input = '\Data.monthly'
monthly_output = '/Parsed.monthly'
colors = {1: 'darkcyan', 2: 'c', 3: 'aqua'}
tuple_columns = (0, 1, 8, 9, 10, 11)

# File data
file_data = '..\A3/textfiles\Data.nh.txt'
# Changes into a list of tuples
tuples_list = makeList(file_data)

# Plot list plots after the data is split into two new lists
plotList(name='Northern hemisphere', color='slateblue',
         list_tuples=tuples_list, xaxis='year', yaxis='temprature anomalies')
# Saves the graph
plt.savefig('..\A3/images/A3part1.png')
plt.show()

# Iterates through the list of files and invokes the correctFile
# function to each of those files to reformat the data inside those files
N = len(IO_monthly_files)
for i in range(N - 1):
    II = 2 * (i - 1)
    OI = (2 * i) - 1
    if II < 0 and OI < 0:
        continue
    if II > N or OI > N:
        break

    IF = parent_path + monthly_input + IO_monthly_files[II]
    OF = parent_path + monthly_output + IO_monthly_files[OI]
    success = correctFile(IF, OF)
    # print("Files, {}, {} -> {}".format(IF, OF, success))

#
#
# To see this following plot make sure you read the comment in plotWithError
# function so you don't get confused with the legend for the nominal curve not showing up
#
#

# Granularity of months to average over
months = 12
# makeAverageList function invoked for each of the data sets using the Granularity
list_nh = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, months)
list_ns = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 1, months)
list_sh = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 1, months)
list_tr = makeAverageList(parent_path + '\Parsed.monthly_out.tr.txt', 0, 1, months)
# They are all plotted on a same plot with different colours
plotList('nh', list_nh, 'm', 'years', 'temprature')
plotList('ns', list_ns, 'k', 'years', 'temprature')
plotList('sh', list_sh, 'r', 'years', 'temprature')
plotList('tr', list_tr, 'c', 'years', 'temprature')
# Number of plots are saved with different names for each plot
# plt.savefig('..\A3/images/A3part2a10Years.png')
# The plot is displayed on the screen
plt.show()

months = 48
# List for each data set, four for each one
list_nh = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, months)
list_nh1 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 8, months)
list_nh2 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 9, months)
list_nh3 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 10, months)
list_nh4 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 11, months)

list_ns = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 1, months)
list_ns1 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 8, months)
list_ns2 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 9, months)
list_ns3 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 10, months)
list_ns4 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 11, months)

list_sh = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 1, months)
list_sh1 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 8, months)
list_sh2 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 9, months)
list_sh3 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 10, months)
list_sh4 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 11, months)

list_trp = makeAverageList(parent_path + '\Parsed.monthly_out.tr.txt', 0, 1, months)
list_trp1 = makeAverageList(parent_path + '\Parsed.monthly_out.tr.txt', 0, 8, months)
list_trp2 = makeAverageList(parent_path + '\Parsed.monthly_out.tr.txt', 0, 9, months)
list_trp3 = makeAverageList(parent_path + '\Parsed.monthly_out.tr.txt', 0, 10, months)
list_trp4 = makeAverageList(parent_path + '\Parsed.monthly_out.tr.txt', 0, 11, months)

# Invokes the function to plot with the corresponding variation
# Saves the figure into an image
# Displays the plot
# respectively
plotWithError('nh', 'uncertainty', list_nh, list_nh3, list_nh4, colors[1], colors[3], 'time(years)', 'temp(c)')
plotWithError('nh', 'uncertainty2', list_nh, list_nh1, list_nh2, colors[1], colors[2], 'time(years)', 'temp(c)')
plt.savefig('..\A3/images/A3part2b.png')
plt.show()

plotWithError('ns', 'uncertainty', list_ns, list_ns3, list_ns4, colors[1], colors[3], 'time(years)', 'temp(c)')
plotWithError('ns', 'uncertainty2', list_ns, list_ns1, list_ns2, colors[1], colors[2], 'time(years)', 'temp(c)')
plt.savefig('..\A3/images/A3part2c.png')
plt.show()

plotWithError('sh', 'uncertainty', list_sh, list_sh3, list_sh4, colors[1], colors[3], 'time(years)', 'temp(c)')
plotWithError('sh', 'uncertainty2', list_sh, list_sh1, list_sh2, colors[1], colors[2], 'time(years)', 'temp(c)')
plt.savefig('..\A3/images/A3part2d.png')
plt.show()

plotWithError('trp', 'uncertainty', list_trp, list_trp3, list_trp4, colors[1], colors[3], 'time(years)', 'temp(c)')
plotWithError('trp', 'uncertainty2', list_trp, list_trp1, list_trp2, colors[1], colors[2], 'time(years)', 'temp(c)')
plt.savefig('..\A3/images/A3part2e.png')
plt.show()

# An instance of the class to be used for plotting
ana = Analysis('year', 'temprature')

# Files are added into the list of files to be plotted
ana.addFile(monthly_output + '_out.nh', 'nh')
ana.addFile(monthly_output + '_out.sh', 'sh')
ana.addFile(monthly_output + '_out.tr', 'tr')

# The updateLists function is called with the given rows and granularity
ana.updateLists(tuple_columns, 2, 'Type I Uncertainty', 'Type II Uncertainty', 1677, 2037)
ana.updateLists(tuple_columns, 2, 'Type I Uncertainty', 'Type II Uncertainty', 1917, 2037)

# plotWithErrors function is invoked for each of the data sets that were added and their plots are saved
ana.plotWithErrors(0, 0, 0)
plt.savefig('..\A3/images/A3part3a.png')
plt.show()

ana.plotWithErrors(1, 0, 0)
plt.savefig('..\A3/images/A3part3b.png')
plt.show()

ana.plotWithErrors(2, 0, 0)
plt.savefig('..\A3/images/A3part3c.png')
plt.show()

# updateLists function invoked again with different granularity to test for correlation between reigns
# using the scatterPlot function for each data set
ana.updateLists(tuple_columns, 2, 'Type I Uncertainty', 'Type II Uncertainty', 1677, 2037)
ana.scatterPlot(0, 1, 'me')
ana.scatterPlot(1, 2, 'me')
ana.scatterPlot(0, 2, 'me')

ana.updateLists(tuple_columns, 12, 'Type I Uncertainty', 'Type II Uncertainty', 1917, 2037)
ana.scatterPlot(0, 1, 'me')
ana.scatterPlot(1, 2, 'me')
ana.scatterPlot(0, 2, 'me')

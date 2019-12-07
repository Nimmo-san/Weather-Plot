import matplotlib.pyplot as plt

from functions import plotList, makeList, correctFile, makeAverageList, plotWithError

parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh.txt', '_out.nh.txt', '_ns.txt',
                    '_out.ns.txt', '_sh.txt', '_out.sh.txt',
                    '_tropical.txt', '_out.tr.txt']
monthly_input = '\Data.monthly'
monthly_output = '/Parsed.monthly'
colors = {1: 'darkcyan', 2: 'c', 3: 'aqua'}

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

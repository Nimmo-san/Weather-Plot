import matplotlib.pyplot as plt

from functions import makeList, plotList, correctFile

# The file Data.nh.txt is being run through
# the makeList function to turn into a list of tuples
data_file = '..\A3/textfiles\Data.nh.txt'
list_tuples = makeList(data_file)
# Passed through the function to be plotted with the given arguments
plotList('DEAD!', list_tuples, 'r', 'DEAD I', 'DEAD II')
# Saves the graph with the passed in name as a PNG
# plt.savefig('..\A3/images/test.png')
# Shows the plotted graph
# plt.show()

fakedata = '..\A3/textfiles\FakeData.txt'
fakeoutput = '..\A3/textfiles/Here.txt'
correctFile(fakedata, fakeoutput)

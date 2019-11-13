import matplotlib.pyplot as plt

from functions import makeList, plotList, correctFile

parent_path = '..\A3/textfiles'
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

fake_data = parent_path + '\Data.monthly_nh.txt'
fake_output = parent_path + '/parsed.monthly_nh.txt'
print(correctFile(fake_data, fake_output))

import matplotlib.pyplot as plt

from classes import Analysis
from functions import makeList, plotList, correctFile, makeAverageList, plotWithError

# Constant variables to be used globally
parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh', '_out.nh', '_ns', '_out.ns', '_sh', '_out.sh', '_tropical', '_out.tr']
test_data = '..\A3/textfiles\FakeData.txt'
test_output = '..\A3/textfiles/Here.txt'
monthly_input = '\Data.monthly'
monthly_output = '/Parsed.monthly'

# The test data to be plotted
data_file = '..\A3/textfiles\Data.nh.txt'
# Requests for the data in the file to be appended into a list
list_tuples = makeList(data_file)

plotList('DEAD!', list_tuples, 'r', 'DEAD I', 'DEAD II')
# The figure is saved and displayed
plt.savefig('..\A3/images/test.png')
plt.show()

print(correctFile(test_data, test_output))

# Iterates through the files stored
# and aplies the correctFile function
n = len(IO_monthly_files)
for i in range(n - 1):

    input_file_index = 2 * (i - 1)
    output_file_index = 2 * i - 1
    if input_file_index < 0 and output_file_index < 0:
        continue
    if input_file_index > n or output_file_index > n:
        break

    input_file = parent_path + monthly_input + IO_monthly_files[input_file_index] + '.txt'
    output_file = parent_path + monthly_output + IO_monthly_files[output_file_index] + '.txt'

    success = correctFile(input_file, output_file)

# Please keep away from this code  from this line till 53, Arigato #
# def removefile(file):
#     import os
#     if os.path.exists(file):
#         os.remove(file)
#         return True
#     return False

# for i in range(len(IO_monthly_files)-1):
#     monthly_input = '\Data.monthly'
#     monthly_output = '/Data.monthly'
#
#     input_file_index = 2 * (i-1)
#     output_file_index = 2 * i - 1
#     if input_file_index < 0 and output_file_index < 0:
#         continue
#
#     if input_file_index > len(IO_monthly_files) or output_file_index > len(IO_monthly_files):
#         break
#
#     # print("File, I:O -> {}:{}".format(IO_monthly_files[input_file_index],
#         # IO_monthly_files[output_file_index]))
#     input_file = parent_path + monthly_input + IO_monthly_files[input_file_index] + '.txt'
#     output_file = parent_path + monthly_output + IO_monthly_files[output_file_index] + '.txt'
#
#     # print("INPUT:OUTPUT -->> {}:{}".format(input_file, output_file))
#     success = correctFile(input_file, output_file)
#     print("FILE: {} --> {}".format(input_file, success))
#
#     # print("FILE: {} --> {}".format(output_file, removefile(output_file)))
#     # print('\n')

import matplotlib.pyplot as plt

from functions import _average, _chunks, _tofloat, openFile


class Analysis:
    # The init method od this class initiliases some empty
    # variables to their corresponding variables to be used in this class
    def __init__(self, x='x', y='y'):
        self.x_title = x
        self.y_title = y
        self.input_files = []
        self.titles = []
        self.list_tuples = []
        self.uncer1 = []
        self.uncer2 = []
        self.parent_path = '..\A3/textfiles'
        # Dictionary of colors to be used in the plotting of the data sets
        self.colors = {'d': 'darkcyan', 'me': 'c', 'l': 'aqua', 'vl': 'cyan'}

    def addFile(self, input_file, title):
        """ Lets the user add files into the list to be processed by updateLists """
        if input_file and title:
            self.input_files.append(input_file)
            self.titles.append(title)

    def printLists(self):
        """ Prints the input files and their corresponding titles into the console """
        print("\nInput files, titles: \n")
        for data in range(len(self.input_files)):
            print(" -> {}.txt, {}".format(self.input_files[data], self.titles[data]))

            # for i in self.list_tuples:
            #     print(i)

    def plotWithErrors(self, index_=None, value_=0, key_=''):
        """ Plots the processed data using the plot function after appending it into
            their corresponding lists  """
        # corresponding lists for the plots
        xpoints = []
        ypoints = []
        upper_uncertainty = []
        lower_uncertainty = []
        upper_uncertainty2 = []
        lower_uncertainty2 = []

        # Iterating through the list and appending the data points to their lists after checking the index
        if not (not (index_ >= 0) or not (index_ < len(self.list_tuples))):
            for (a, b, c, d, e, f) in self.list_tuples[index_]:
                xpoints.append(a)
                ypoints.append(b)
                upper_uncertainty.append(c)
                lower_uncertainty.append(d)
                upper_uncertainty2.append(e)
                lower_uncertainty2.append(f)

            xpoints = _tofloat(xpoints)
            upper_uncertainty = _tofloat(upper_uncertainty)
            lower_uncertainty = _tofloat(lower_uncertainty)
            upper_uncertainty2 = _tofloat(upper_uncertainty2)
            lower_uncertainty2 = _tofloat(lower_uncertainty2)

            if value_ == 2:
                plt.fill_between(xpoints, upper_uncertainty2, lower_uncertainty2, color=self.colors['vl'],
                                 label=self.uncer1[index_])
                plt.fill_between(xpoints, upper_uncertainty, lower_uncertainty, color=self.colors['me'],
                                 label=self.uncer2[index_])
            elif value_ == 1:
                plt.fill_between(xpoints, upper_uncertainty, lower_uncertainty, color=self.colors['me'],
                                 label=self.uncer1[index_])
            else:
                pass
            plt.plot(xpoints, ypoints, color=self.colors['d'], label=self.titles[index_])
            plt.xlabel(self.x_title)
            plt.ylabel(self.y_title)
            plt.legend()
        else:
            print("\n Index out of bounds!")
        return

    """ # The following function is better
    def plotListTuples(self, nominalName, uncerName1, uncerName2):
           #Plots the processed data using the plot function after appending it into
            #their corresponding lists
        # corresponding lists for the plots
        xpoints = []
        ypoints = []
        upper_uncertainty = []
        lower_uncertainty = []
        upper_uncertainty2 = []
        lower_uncertainty2 = []

        # Iterating through the list and appending the data points to their lists
        for (a, b, c, d, e, f) in self.list_tuples:
            xpoints.append(a)
            ypoints.append(b)
            upper_uncertainty.append(c)
            lower_uncertainty.append(d)
            upper_uncertainty2.append(e)
            lower_uncertainty2.append(f)

        # Changing the lists into floats to be used by the fill_between function
        xpoints = _tofloat(xpoints)
        upper_uncertainty = _tofloat(upper_uncertainty)
        lower_uncertainty = _tofloat(lower_uncertainty)
        upper_uncertainty2 = _tofloat(upper_uncertainty2)
        lower_uncertainty2 = _tofloat(lower_uncertainty2)

        # Plotting the errors and the nominal values
        plt.fill_between(xpoints, upper_uncertainty2, lower_uncertainty2, color=self.colors['vl'], label=uncerName1)
        plt.fill_between(xpoints, upper_uncertainty, lower_uncertainty, color=self.colors['me'], label=uncerName2)
        plt.plot(xpoints, ypoints, color=self.colors['d'], label=nominalName)
        # Shows the legend/labels for each of the data sets and display the plots
        plt.legend()
        plt.show()
        return
        """
    def updateLists(self, tuple_columns, granularity=0, type_='', type_2='', min_=0, max_=0):
        """ This function will be called to process the opened files and invoke the _formatData
            function to each of the files present in the input_files """

        # Iterating through the files and invoking the _formatData function and calling the plotListTuples
        # with the corresponding labels for each of the data sets

        n = len(self.input_files)
        for i in range(n):
            file = openFile(self.parent_path + self.input_files[i] + '.txt', 'r')
            # opened_Files.append(file)
            if file:
                lines = [line.rstrip('\n') for line in file]
                files_data = self._formatData(data=lines, tuple_=tuple_columns,
                                              gra=granularity, min_=min_, max_=max_)

                self.uncer1.append(type_)
                self.uncer2.append(type_2)
                self.list_tuples.append(files_data)
            else:
                exit(1)
        # print(self.list_tuples)
        return

    def to_tuple(self, list_):
        """ Changes the data stored in list_ into tuples """
        return [tuple(element) for element in list_]

    def _formatData(self, data, tuple_, gra, min_, max_):
        """ Retrieves the data and formats it to the correct format to be
            averaged over and plotted """

        # Empty lists for the data points
        list_ = []  # all values
        list_xy = []  # nominal values
        list_u = []  # type uncertainty 1
        list_u2 = []  # type uncertainty 2

        # Checks if the min_ and max_ are within bounds
        if min_ >= 0 and max_ <= len(data):
            # Iterates through the list between the max and min and adds it
            # into the list if its corresponding column is found in the tuple of columns passed in
            for elem in range(min_, max_, 1):
                split = data[elem].split(',')
                for j in range(len(split)):
                    if j in tuple_:
                        list_.append(split[j])
        else:
            print(min_, max_, "Out of bounds!")
            exit(1)

        # print(list_)
        # Divides it into a list of every two elements in each sublist and changes the sublists into tuples
        list_ = _chunks(list_, 2)
        list_ = self.to_tuple(list_)

        # Iterates through the list to acquire the nominal values and their corresponding errors
        size = len(list_)
        for i in range(1, size):
            in1 = 3 * (i - 1)  # nominal values
            in2 = 3 * i - 2  # uncertainty 1
            in3 = 3 * i - 1  # uncertainty 2
            if in1 > size or in2 > size or in3 > size:
                break

            list_xy.append(list_[in1])
            list_u.append(list_[in2])
            list_u2.append(list_[in3])

        # Averages over the lists after dividing it yet again into the granularity passed in
        list_xy = _average(list(_chunks(list_xy, gra)))
        list_u = _average(list(_chunks(list_u, gra)))
        list_u2 = _average(list(_chunks(list_u2, gra)))

        # Clears the unnecessary list and adds the values into one final list to be returned
        list_.clear()
        for i in range(len(list_xy)):
            tuple_ = list_xy[i] + list_u[i] + list_u2[i]
            list_.append(tuple_)

        return list_

    def scatterPlot(self, list_1, list_2, key_='m'):
        xc = []
        yc = []
        for (a, b, c, d, e, f) in self.list_tuples[list_1]:
            xc.append(b)

        for (a, b, c, d, e, f) in self.list_tuples[list_2]:
            yc.append(b)

        plt.plot(xc, yc, self.colors[key_] + 'o', label=self.titles[list_1] + ' ' + self.titles[list_2], markersize=2)
        plt.xlabel('{} temp'.format(self.titles[list_1]))
        plt.ylabel('{} temp'.format(self.titles[list_2]))
        plt.legend()
        plt.show()
        return

import matplotlib.pyplot as plt

from functions import _average, _chunks, _tofloat, to_tuple


class Analysis:

    def __init__(self, x='x', y='y'):
        self.x_title = x
        self.y_title = y
        self.input_files = []
        self.titles = []
        self.list_tuples = []
        self.uncer1 = []
        self.uncer2 = []
        self.colors = {'d': 'm', 'me': 'fuchsia', 'l': 'magenta', 'vl': 'orchid'}

    def addFile(self, input_file, title):
        if input_file and title:
            self.input_files.append(input_file)
            self.titles.append(title)

    def printLists(self):
        print("\nInput files, titles: \n")
        for data in range(len(self.input_files)):
            print(" -> {}.txt, {}".format(self.input_files[data], self.titles[data]))

    def plotListTuples(self):
        xpoints = []
        ypoints = []
        upper_uncertainty = []
        lower_uncertainty = []

        for (a, b, c, d, e, f) in self.list_tuples:
            xpoints.append(a)
            ypoints.append(b)
            upper_uncertainty.append(c)
            lower_uncertainty.append(d)

        xpoints = _tofloat(xpoints)
        ypoints = _tofloat(ypoints)
        upper_uncertainty = _tofloat(upper_uncertainty)
        lower_uncertainty = _tofloat(lower_uncertainty)
        plt.fill_between(xpoints, upper_uncertainty, lower_uncertainty, color='m')
        plt.plot(xpoints, ypoints, 'ro', markersize=2)
        plt.show()
        return

    def updateLists(self, tuple_columns, granularity=0, type_='', type_2='', min_=0, max_=0):

        for i in self.input_files:
            file = open(i + '.txt', 'r')
            # opened_Files.append(file)
            lines = [line.rstrip('\n') for line in file]
            files_data = self._retrieveData(data=lines, tuple_=tuple_columns,
                                            gra=granularity, min_=min_, max_=max_)
            self.list_tuples = files_data
            self.uncer1.append(type_)
            self.uncer2.append(type_2)
            self.plotListTuples()

    def _retrieveData(self, data, tuple_, gra, min_, max_):
        list_ = []

        list_xy = []
        list_u = []
        list_u2 = []
        # print(len(data))
        if min_ >= 0 and max_ <= len(data):
            for elem in range(min_, max_, 1):
                split = data[elem].split(',')
                for j in range(len(split)):
                    if j in tuple_:
                        list_.append(split[j])
        else:
            print(min_, max_, "Out of bounds!")

        list_ = _chunks(list_, 2)
        list_ = to_tuple(list_)

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

        list_xy = _average(list(_chunks(list_xy, gra)))
        list_u = _average(list(_chunks(list_u, gra)))
        list_u2 = _average(list(_chunks(list_u2, gra)))

        list_.clear()
        for i in range(len(list_xy)):
            tuple_ = list_xy[i] + list_u[i] + list_u2[i]
            list_.append(tuple_)

        return list_

    def scatterPlot(self, one, two, color='m'):
        return

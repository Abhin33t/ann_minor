__author__ = 'Abhineet Saxena'

"""
Loads the normalized data from the csv file and returns a supervised dataset (PyBrain) for that data.
"""

# The Imports
import random as rd
from pybrain.datasets import SupervisedDataSet as sdset


def dataLoad(file_name, num_train, num_valid, num_test, switch=0, num_iter=0):

    # Asserting the type of value for num_of_records to be of int.
    assert isinstance(num_train, int)
    assert isinstance(num_valid, int)
    assert isinstance(num_test, int)

    readfile = open(file_name, 'r')
    train_datset = sdset(10, 1)
    valid_datset = sdset(10, 1)
    test_datset = []
    line_count = 0
    valid_count = num_train + num_valid
    line = readfile.readline()
    if switch:
        train_dict = {}
    while line:
        line_count += 1
        line = [float(elem) for elem in line.strip().split(',')]
        # print line_count, '::', line
        if switch:
            train_dict.setdefault(line_count, line)
        if line_count <= num_train:
            train_datset.addSample(line[:10], line[10])
        elif line_count <= valid_count:
            valid_datset.addSample(line[:10], line[10])
        else:
            test_datset.append((tuple(line[:10]), line[10]))
        line = readfile.readline()
    if switch:
        for iterv in xrange(num_iter):
            rand_val = rd.randint(1, num_train)
            train_datset.addSample(train_dict[rand_val][:10], train_dict[rand_val][10])
    return (train_datset, valid_datset, test_datset)

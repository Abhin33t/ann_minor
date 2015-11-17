__author__ = 'Abhineet Saxena'

"""
Neural Net Classification and Evaluation Trial
"""
# The imports:

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
# from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.structure import BiasUnit
from Data_Loader_Module import dataLoad as dload
import math as mt
import random as rnd

def roundOff(xvar):
    """
    Returns the rounded value to signify the meaning of the output of the Neural Network.
    :param xvar:
    :return:
    """
    if xvar <= 0.5:
        return 0
    else:
        return 1
# # Here we instantiate a Feed-Forward Network.
# annet = FeedForwardNetwork()
#
# # Creation of the input layer: Here the integer denotes the number of nodes we wish to have in the layer.
# inLayer = LinearLayer(10, 'inlyr')
#
# # Creation of the hidden layer.
# hid1Layer = SigmoidLayer(5, 'hiddenlyr')
#
# # Creation of the Output layer.
# outLayer = LinearLayer(1, 'outlyr')
#
# # Instantiating the Bias Unit.
# bias_val = BiasUnit()
#
# # Adding the corresponding layers to the network.
# annet.addInputModule(inLayer)
# annet.addModule(hid1Layer)
# annet.addModule(bias_val)
# annet.addOutputModule(outLayer)
#
# # Adding the connections b/w layers pair-wise.
# # Note,FullConnection denotes all the nodes of one- #layer are connected to all the nodes of the next layer.
# annet.addConnection(FullConnection(inLayer, hid1Layer))
# annet.addConnection(FullConnection(bias_val, hid1Layer))
# annet.addConnection(FullConnection(hid1Layer, outLayer))
#
# # The method performs internal management of the specifications.
# annet.sortModules()

annet = buildNetwork(10, 4, 1, bias=True) # ,outclass=SoftmaxLayer)
outFile = open('Neural_Net_Output_Non_Repeat.txt', 'w')
print annet

# Loading the supervised dataset.
trainset_var, valdset_var, testset_var = dload('ilpd_modd_normalized_data.csv', 435, 100, 48, 0, 1000)

# print trainset_var
# print valdset_var
# print len(testset_var)
trainer = BackpropTrainer(annet, learningrate=0.01, momentum=0.9)
trainer.trainUntilConvergence(verbose=True, trainingData=trainset_var, validationData=valdset_var, maxEpochs=25)

#print testset_var[:10]
count = 0
for iterv in xrange(48):
    outval = annet.activate(testset_var[iterv][0])
    if float(roundOff(outval)) == testset_var[iterv][1]:
        count += 1
    print 'Neural Network Output: ', outval, 'Rounded Value: ', roundOff(outval), 'Actual Value: ', testset_var[iterv][1]
    outFile.write('Neural Network Output: {0}, Rounded Value: {1}, Actual Value: {2}\n'.format(
        outval, roundOff(outval), testset_var[iterv][1]))
print 'Output Match %age: ', (count/48.0)*100
outFile.write('Output Match %age: {0}'.format((count/48.0)*100))

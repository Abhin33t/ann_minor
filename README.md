# ann_minor
<b>Minor Project on Artificial Neural Networks</b>
<br><br>
The Project aims to perform classification operation on the standard dataset which has been retrieved from the UCI Machine Learning Repository:<br>
http://archive.ics.uci.edu/ml/datasets/ILPD+%28Indian+Liver+Patient+Dataset%29
<br>
The Project makes use of PyBrain Python module specifically focussed on Artificial Neural Networks:<br>
http://pybrain.org/docs/index.html
<br><br>
The Project consists of the following major components:<br>
1> The standard dataset, ilpd_data.csv<br>
2> The Normailzer Module (Normalization_module.py) that takes as input the dataset specified in point <1> and normalizes the specified input columns.<br>
3> The Data Loader Module that loads the normalized data into a SupervisedDataSet instance.<br>
4> Neural_Net_Eval1.py trains the Neural Network on the Supervised Training dataset constituted previously and then prduces output over the test set.<br> 
5> Neural_Net_Output_Non_Repeat.txt provides a sample run output. <br>

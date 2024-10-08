# -*- coding: utf-8 -*-
"""Sensor Combination Public Dataset-2 kinetics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OfmLx79FC5cwm1X4aJIe9nN8oVAM_gC5
"""

import h5py
import json
import matplotlib.pyplot as plt
import numpy as np
import numpy
import tensorflow as tf
import statistics 
from numpy import loadtxt
import matplotlib.pyplot as plt
import pandas
import math
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import GRU,LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from statistics import stdev 
import math
import h5py
from sklearn.utils import resample
 
import numpy as np

from scipy.signal import butter,filtfilt
 
import sys 
import numpy as np # linear algebra
from scipy.stats import randint
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv), data manipulation as in SQL
import matplotlib.pyplot as plt # this is used for the plot the graph 
import seaborn as sns # used for plot interactive graph. 
import pandas
import matplotlib.pyplot as plt
 
## for Deep-learing:
import tensorflow.keras

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
to_categorical([0, 1, 2, 3], num_classes=4)
from tensorflow.keras.optimizers import SGD 
from tensorflow.keras.callbacks import EarlyStopping
# from tensorflow.keras.utils import np_utils
import itertools
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import TimeDistributed
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Bidirectional
#import constraint
 
from sklearn.model_selection import train_test_split
from tensorflow.keras.regularizers import l2
 
 
###  Library for attention layers 
 
import pandas as pd
#import pyarrow.parquet as pq # Used to read the data
import os 
import numpy as np
from tensorflow.keras.layers import * # Keras is the most friendly Neural Network library, this Kernel use a lot of layers classes
from tensorflow.keras.models import Model
#from tqdm import tqdm # Processing time measurement
from sklearn.model_selection import train_test_split 
from tensorflow.keras import backend as K # The backend give us access to tensorflow operations and allow us to create the Attention class
from tensorflow.keras import optimizers # Allow us to access the Adam class to modify some parameters
from sklearn.model_selection import GridSearchCV, StratifiedKFold # Used to use Kfold to train our model
from tensorflow.keras.callbacks import * # This object helps the model to train in a smarter way, avoiding overfitting
 
from tensorflow.keras.layers import Layer
import tensorflow.keras.backend as K
from tensorflow.keras import initializers
from tensorflow.keras import regularizers
import statistics
import gc


 
### Early stopping 
 
from tensorflow.keras.callbacks import EarlyStopping

 

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.compat.v1.Session(config=config)

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())



"""# Data loader"""


 
main_dir = "/home/sanzidpr/JBHI_revision/Bagging/Subject25"
#os.mkdir(main_dir) 
path="/home/sanzidpr/JBHI_revision/Bagging/Subject25/"
subject='Subject_25'
hf = h5py.File('/home/sanzidpr/Public Kinetics dataset/Subject_25_data.h5', 'r')

train_X_3 = np.array(hf.get('train_dataset_X'))
train_y_3 = np.array(hf.get('train_dataset_y'))
test_X_1D = np.array(hf.get('test_dataset_X'))
test_y = np.array(hf.get('test_dataset_y'))




w=100


train_X_1D, X_validation_1D, train_y_5, Y_validation = train_test_split(train_X_3,train_y_3, test_size=0.20, random_state=True)
#train_X_1D, X_validation_1D_ridge, train_y, Y_validation_ridge = train_test_split(train_X_1D_m,train_y_m, test_size=0.10, random_state=True)   [0:2668,:,:]

print(train_X_1D.shape,train_y_5.shape,X_validation_1D.shape,Y_validation.shape)

features=6

train_X_2D=train_X_1D.reshape(train_X_1D.shape[0],train_X_1D.shape[1],features,3)
test_X_2D=test_X_1D.reshape(test_X_1D.shape[0],test_X_1D.shape[1],features,3)
X_validation_2D= X_validation_1D.reshape(X_validation_1D.shape[0],X_validation_1D.shape[1],features,3)
#X_validation_2D_ridge= X_validation_1D_ridge.reshape(X_validation_1D_ridge.shape[0],X_validation_1D_ridge.shape[1],8,2)


s=test_X_1D.shape[0]*w

print(train_X_2D.shape,test_X_2D.shape,X_validation_2D.shape)

import tensorflow as tf
# tensorflow import keras
from tensorflow.keras import layers

Bag_samples=train_X_2D.shape[0]
print(Bag_samples)


test_o=test_y.reshape((s,7))
 
y_test_1=test_o[:,0]
y_test_2=test_o[:,1]
y_test_3=test_o[:,2]
y_test_4=test_o[:,3]
y_test_5=test_o[:,4]
y_test_6=test_o[:,5]
y_test_7=test_o[:,6]

n_1=max(y_test_1)-min(y_test_1)
n_2=max(y_test_2)-min(y_test_2)
n_3=max(y_test_3)-min(y_test_3)
n_4=max(y_test_4)-min(y_test_4)
n_5=max(y_test_5)-min(y_test_5)
n_6=max(y_test_6)-min(y_test_6)
n_7=max(y_test_7)-min(y_test_7)





print(n_1)
print(n_2)
print(n_3)
print(n_4)
print(n_5)
print(n_6)
print(n_7)








gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()

 
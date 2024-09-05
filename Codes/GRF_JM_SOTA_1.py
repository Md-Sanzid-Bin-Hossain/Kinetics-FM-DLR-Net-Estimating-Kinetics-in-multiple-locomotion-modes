# -*- coding: utf-8 -*-
"""Future_Gait_DLR_Net_public_data_Stair_slope_Kinematics_kinetics_Public_dataset_kinematics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/116DLyfghavEPPeefrKabrJvohcuH2_xs
"""

# -*- coding: utf-8 -*-
"""Future_Gait_DLR_Net_public_data_Stair_slope_Kinematics_kinetics_Public_dataset_kinematics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/116DLyfghavEPPeefrKabrJvohcuH2_xs
"""

# Let's import all packages that we may need:
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
from tcn import TCN 
import numpy as np

from scipy.signal import butter,filtfilt
from tensorflow.keras.callbacks import EarlyStopping

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
from numpy import savetxt


import os 

### Early stopping 
 
from tensorflow.keras.callbacks import EarlyStopping

 

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.compat.v1.Session(config=config)

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())





 
main_dir = "/home/sanzidpr/JBHI_revision/Dataset_1_SOTA/Subject30"
os.mkdir(main_dir) 
path="/home/sanzidpr/JBHI_revision/Dataset_1_SOTA/Subject30/"
subject='Subject_30'
hf = h5py.File('/home/sanzidpr/Public Kinetics dataset/Subject_30_data.h5', 'r')

train_X_3 = np.array(hf.get('train_dataset_X'))
train_y_3 = np.array(hf.get('train_dataset_y'))
test_X_1D = np.array(hf.get('test_dataset_X'))
test_y = np.array(hf.get('test_dataset_y'))

#hf.create_dataset('train_dataset_X', data=train_X_3)
#hf.create_dataset('train_dataset_y', data=train_y_3)
#hf.create_dataset('test_dataset_X', data=test_X_1D)
#hf.create_dataset('test_dataset_y', data=test_y)
#

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

gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()
gc.collect()


##########################################################################################################################################################################################  
##########################################################################################################################################################################################    

  
  
  
from sklearn.model_selection import KFold
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import MultiOutputRegressor
import pickle
from sklearn.linear_model import Ridge
from sklearn.utils import resample

"""# Loss Function"""

from keras import backend as K
def correlation_coefficient_loss(y_true, y_pred):
    x = y_true
    y = y_pred
    mx = K.mean(x)
    my = K.mean(y)
    xm, ym = x-mx, y-my
    r_num = K.sum(tf.multiply(xm,ym))
    r_den = K.sqrt(tf.multiply(K.sum(K.square(xm)), K.sum(K.square(ym))))
    r = r_num / r_den

    #r = K.maximum(K.minimum(r, 1.0), -1.0)

    l1=K.sqrt(K.mean(K.square(y_pred - y_true)))
    #l2=1-K.square(r)
    l2=1-r

    l=l2
    return l

from keras import backend as K
def correlation_coefficient_loss_1(y_true, y_pred):
    x = y_true
    y = y_pred
    mx = K.mean(x)
    my = K.mean(y)
    xm, ym = x-mx, y-my
    r_num = K.sum(tf.multiply(xm,ym))
    r_den = K.sqrt(tf.multiply(K.sum(K.square(xm)), K.sum(K.square(ym))))
    r = r_num / r_den

    r = K.maximum(K.minimum(r, 1.0), -1.0)

    l1=K.sqrt(K.mean(K.square(y_pred - y_true)))
    l2=1-K.square(r)

    l=l1
    return l

from keras import backend as K
def correlation_coefficient_loss_joint(y_true, y_pred):
    x = y_true
    y = y_pred
    mx = K.mean(x)
    my = K.mean(y)
    xm, ym = x-mx, y-my
    r_num = K.sum(tf.multiply(xm,ym))
    r_den = K.sqrt(tf.multiply(K.sum(K.square(xm)), K.sum(K.square(ym))))
    r = r_num / r_den

    #r = K.maximum(K.minimum(r, 1.0), -1.0)

    l1=K.sqrt(K.mean(K.square(y_pred - y_true)))
    #l2=1-K.square(r)
    l2=1-r

    l=l1+l2
    return l
    
    
custom_early_stopping=tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    min_delta=0,
    patience=15,
    verbose=0,
    mode='auto',
    baseline=None,
    restore_best_weights=True
) 



def RMSE_prediction(yhat_4,test_y,s):
 
  test_o=test_y.reshape((s,7))
  yhat=yhat_4.reshape((s,7))
  
  
  
  
  y_1_no=yhat[:,0]
  y_2_no=yhat[:,1]
  y_3_no=yhat[:,2]
  y_4_no=yhat[:,3]
  y_5_no=yhat[:,4]
  y_6_no=yhat[:,5]
  y_7_no=yhat[:,6]
  #y_8_no=yhat[:,7]
  #y_9_no=yhat[:,8]
  #y_10_no=yhat[:,9]
  
  
  
  
  y_test_1=test_o[:,0]
  y_test_2=test_o[:,1]
  y_test_3=test_o[:,2]
  y_test_4=test_o[:,3]
  y_test_5=test_o[:,4]
  y_test_6=test_o[:,5]
  y_test_7=test_o[:,6]
  #y_test_8=test_o[:,7]
  #y_test_9=test_o[:,8]
  #y_test_10=test_o[:,9]
  
  
  
  
  
  #print(y_1.shape,y_test_1.shape)
  
  
  
  cutoff=6
  fs=200
  order=4
  
  nyq = 0.5 * fs
  ## filtering data ##
  def butter_lowpass_filter(data, cutoff, fs, order):
      normal_cutoff = cutoff / nyq
      # Get the filter coefficients 
      b, a = butter(order, normal_cutoff, btype='low', analog=False)
      y = filtfilt(b, a, data)
      return y
  
  
  
  y_1=butter_lowpass_filter(y_1_no, cutoff, fs, order)
  y_2=butter_lowpass_filter(y_2_no, cutoff, fs, order)
  y_3=butter_lowpass_filter(y_3_no, cutoff, fs, order)
  y_4=butter_lowpass_filter(y_4_no, cutoff, fs, order)
  y_5=butter_lowpass_filter(y_5_no, cutoff, fs, order)
  y_6=butter_lowpass_filter(y_6_no, cutoff, fs, order)
  y_7=butter_lowpass_filter(y_7_no, cutoff, fs, order)
  #y_8=butter_lowpass_filter(y_8_no, cutoff, fs, order)
  #y_9=butter_lowpass_filter(y_9_no, cutoff, fs, order)
  #y_10=butter_lowpass_filter(y_10_no, cutoff, fs, order)
  
  
  
  
  Z_1=y_1
  Z_2=y_2
  Z_3=y_3
  Z_4=y_4
  Z_5=y_5
  Z_6=y_6
  Z_7=y_7
  #Z_8=y_8
  #Z_9=y_9
  #Z_10=y_10
  
  
  
  ###calculate RMSE
  
  rmse_1 =((np.sqrt(mean_squared_error(y_test_1,y_1)))/(max(y_test_1)-min(y_test_1)))*100
  rmse_2 =((np.sqrt(mean_squared_error(y_test_2,y_2)))/(max(y_test_2)-min(y_test_2)))*100
  rmse_3 =((np.sqrt(mean_squared_error(y_test_3,y_3)))/(max(y_test_3)-min(y_test_3)))*100
  rmse_4 =((np.sqrt(mean_squared_error(y_test_4,y_4)))/(max(y_test_4)-min(y_test_4)))*100
  rmse_5 =((np.sqrt(mean_squared_error(y_test_5,y_5)))/(max(y_test_5)-min(y_test_5)))*100
  rmse_6 =((np.sqrt(mean_squared_error(y_test_6,y_6)))/(max(y_test_6)-min(y_test_6)))*100
  rmse_7 =((np.sqrt(mean_squared_error(y_test_7,y_7)))/(max(y_test_7)-min(y_test_7)))*100
  #rmse_8 =((np.sqrt(mean_squared_error(y_test_8,y_8)))/(max(y_test_8)-min(y_test_8)))*100
  #rmse_9 =((np.sqrt(mean_squared_error(y_test_9,y_9)))/(max(y_test_9)-min(y_test_9)))*100
  #rmse_10 =((np.sqrt(mean_squared_error(y_test_10,y_10)))/(max(y_test_10)-min(y_test_10)))*100
  
  
  print(rmse_1)
  print(rmse_2)
  print(rmse_3)
  print(rmse_4)
  print(rmse_5)
  print(rmse_6)
  print(rmse_7)
  #print(rmse_8)
  #print(rmse_9)
  #print(rmse_10)
  
  
  p_1=np.corrcoef(y_1, y_test_1)[0, 1]
  p_2=np.corrcoef(y_2, y_test_2)[0, 1]
  p_3=np.corrcoef(y_3, y_test_3)[0, 1]
  p_4=np.corrcoef(y_4, y_test_4)[0, 1]
  p_5=np.corrcoef(y_5, y_test_5)[0, 1]
  p_6=np.corrcoef(y_6, y_test_6)[0, 1]
  p_7=np.corrcoef(y_7, y_test_7)[0, 1]
  #p_8=np.corrcoef(y_8, y_test_8)[0, 1]
  #p_9=np.corrcoef(y_9, y_test_9)[0, 1]
  #p_10=np.corrcoef(y_10, y_test_10)[0, 1]
  
  
  print("\n") 
  print(p_1)
  print(p_2)
  print(p_3)
  print(p_4)
  print(p_5)
  print(p_6)
  print(p_7)
  #print(p_8)
  #print(p_9)
  #print(p_10)
  
  
              ### Correlation ###
  p=np.array([p_1,p_2,p_3,p_4,p_5,p_6,p_7])
  
  
  
  
      #### Mean and standard deviation ####
  
  rmse=np.array([rmse_1,rmse_2,rmse_3,rmse_4,rmse_5,rmse_6,rmse_7])
  
      #### Mean and standard deviation ####
  m=statistics.mean(rmse)
  SD=statistics.stdev(rmse)
  print('Mean: %.3f' % m,'+/- %.3f' %SD)
   
  m_c=statistics.mean(p)
  SD_c=statistics.stdev(p)
  print('Mean: %.3f' % m_c,'+/- %.3f' %SD_c)

  return rmse, p, Z_1,Z_2,Z_3,Z_4,Z_5,Z_6,Z_7




############################################################################################################################################################################################################################################################################################################################################################################################################################################################################

 ### ANN (Features) ###

def feature_extractor(data):
  feat=[]
  feat_final=[]

  for i in range(18):
      signal=data[:,:,i]
      A_1=np.mean(signal,axis=1)
      A_2=np.sqrt(np.mean(signal ** 2,axis=1))
      A_3=np.min(signal,axis=1)   ## max- Statistical
      A_4=np.max(signal,axis=1)   ## min- Statistical
      A_5=np.mean(np.absolute(signal),axis=1)   ## mean- Statistical
      A_6=np.std(signal,axis=1)  ## standard Deviation- Statistical
      A_7=np.mean(np.abs(np.diff(signal,prepend=data[:,0:1,i],axis=1)),axis=1) ## Mean Absolute Difference
      A_8=np.mean(np.diff(signal,prepend=data[:,0:1,i],axis=1),axis=1) ## Mean Absolute Difference
      A_9=np.median(np.diff(signal,prepend=data[:,0:1,i],axis=1),axis=1) ## Mean  Difference
      A_10=np.median(np.abs(np.diff(signal,prepend=data[:,0:1,i],axis=1)),axis=1) ## Mean Absolute Difference
      A_11=np.percentile(signal, 75,axis=1) - np.percentile(signal, 25,axis=1)  # Interquartile Range-- Statistical
      A_12=scipy.stats.kurtosis(signal,axis=1)   ## Kurtosis--Statistical
      A_13=scipy.stats.skew(signal,axis=1)       ## Skewness--Statistical
      A_14=np.median(signal,axis=1) ## median- Statistical
      A_15=np.var(signal,axis=1)
      A_16=scipy.stats.median_absolute_deviation(signal,axis=1,scale=1)
      A_17=np.mean(np.abs(signal - np.mean(signal, axis=1).reshape(signal.shape[0],1)), axis=1)
      A_18=np.mean(np.diff(signal,prepend=data[:,0:1,i],axis=1),axis=1)
      dif=np.diff(data[:,:,i],prepend=data[:,0:1,i],axis=1)
      A_19=np.sum(np.absolute(dif),axis=1)  ### Waveform length
      A_20=np.sum(np.absolute(dif>0),axis=1)  ### Zero Crossing
      A_21=np.sum(np.absolute(np.diff(dif,prepend=data[:,0:1,i],axis=1))>0,axis=1)  ## Slope Sign Changes

      feat=np.vstack((A_1,A_2,A_3,A_4,A_5,A_6,A_7,A_8,A_9,A_10,A_11,A_12,A_13,A_14,A_15,A_16,A_17))
      # feat=np.vstack((A_18,A_19,A_20))
      feat_final.append((feat))
  feat_final=np.array(feat_final)    
  feat_final_1=feat_final.reshape([feat_final.shape[0]*feat_final.shape[1],feat_final.shape[-1]])
  feat_final_1=np.transpose(feat_final_1)

  return(feat_final_1)    
  
  
  
import scipy

X_train=feature_extractor(train_X_1D)
X_test=feature_extractor(test_X_1D)
X_validation=feature_extractor(X_validation_1D)


num_pred=7
# 
w1=100

inputs_1D = tf.keras.layers.Input(shape=(X_train.shape[-1]))
inputs_1D_N=BatchNormalization()(inputs_1D)


#model_1=Dense(2048, activation='relu')(inputs_1D)
#model_1=Dropout(0.05)(model_1)
model_1=Dense(1024, activation='relu')(inputs_1D)
model_1=Dropout(0.05)(model_1)
model_1=Dense(512, activation='relu')(model_1)
model_1=Dropout(0.05)(model_1)
model_1=Dense(256, activation='relu')(model_1)
model_1=Dropout(0.05)(model_1)
model_1=Dense(128, activation='relu')(model_1)
model_1=Dropout(0.05)(model_1)
model_1=Dense(64, activation='relu')(model_1)
model_1=Dropout(0.05)(model_1)
model_1=Flatten()(model_1)


model_1=Dense(num_pred*w1,bias_regularizer=l2(0.001), activation='linear')(model_1)
output=Reshape(target_shape=(w1,num_pred))(model_1)

model = Model(inputs=inputs_1D, outputs=output)

opt = tf.keras.optimizers.Adam(learning_rate=3e-4)

model.compile(loss=correlation_coefficient_loss_1, optimizer=opt, metrics=[correlation_coefficient_loss_1])

model.summary()

history=model.fit(X_train, train_y_5, epochs=40, batch_size=64, validation_data=(X_validation, Y_validation), verbose=2, shuffle=True,callbacks=[custom_early_stopping])

model.save(path+'model_ANN(F).h5')

yhat_4= model.predict(X_test)
rmse, p, Z_1,Z_2,Z_3,Z_4,Z_5,Z_6,Z_7= RMSE_prediction(yhat_4, test_y,s)

ablation_1=np.hstack([rmse,p])

print(rmse)
print(p)  





##############################################################################################################################################################################################################################
##############################################################################################################################################################################################################################
##############################################################################################################################################################################################################################     

K.clear_session()
K.clear_session()


### TCN  ###
seed=7

w1=100

inputs_1D = tf.keras.layers.Input( shape=(w1,18))
inputs_1D_N=BatchNormalization()(inputs_1D)

model_1 = TCN(
    nb_filters=128,
    kernel_size=3,
    nb_stacks=1,
    dilations=(1, 2, 4, 8, 16),
    padding='causal',
    use_skip_connections=True,
    dropout_rate=0.05,
    return_sequences=True,
    activation='relu',
    kernel_initializer='he_normal',
    use_batch_norm=False,
    use_layer_norm=False,
    use_weight_norm=True
)(inputs_1D_N)



model_1=Dense(64, activation='relu')(model_1)
model_1=Dropout(0.1)(model_1)
model_1=Dense(32, activation='relu')(model_1)
model_1=Dropout(0.1)(model_1)
model_1=Flatten()(model_1)

model_1=Dense(num_pred*w1,bias_regularizer=l2(0.001), activation='linear')(model_1)
output=Reshape(target_shape=(w1,num_pred))(model_1)

model = Model(inputs=inputs_1D, outputs=output)

opt = tf.keras.optimizers.Adam(learning_rate=3e-4)

model.compile(loss=correlation_coefficient_loss_1, optimizer='Adam', metrics=[correlation_coefficient_loss_1])

model.summary()

history=model.fit(train_X_1D, train_y_5, epochs=40, batch_size=64, validation_data=(X_validation_1D, Y_validation), verbose=2, shuffle=True,callbacks=[custom_early_stopping])
model.save(path+'model_TCN.h5')


yhat_4= model.predict(test_X_1D)
rmse, p, Z_1,Z_2,Z_3,Z_4,Z_5,Z_6,Z_7= RMSE_prediction(yhat_4, test_y,s)

ablation_2=np.hstack([rmse,p])

print(rmse)
print(p)



w1=100

inputs_1D = tf.keras.layers.Input( shape=(w1,18))
inputs_1D_N=BatchNormalization()(inputs_1D)


model_1=Dense(128, activation='relu')(inputs_1D_N)
model_1=Dropout(0.1)(model_1)
model_1=Dense(64, activation='relu')(model_1)
model_1=Dropout(0.1)(model_1)
model_1=Flatten()(model_1)

model_1=Dense(num_pred*w1,bias_regularizer=l2(0.001), activation='linear')(model_1)
output=Reshape(target_shape=(w1,num_pred))(model_1)

model = Model(inputs=inputs_1D, outputs=output)

opt = tf.keras.optimizers.Adam(learning_rate=3e-4)

model.compile(loss=correlation_coefficient_loss_1, optimizer=opt, metrics=[correlation_coefficient_loss_1])

model.summary()

history=model.fit(train_X_1D, train_y_5, epochs=40, batch_size=64, validation_data=(X_validation_1D, Y_validation), verbose=2, shuffle=False)


model.save(path+'model_ANN.h5')

# yhat_main= model_1.predict([test_X_1D,test_X_2D])

yhat_4= model.predict(test_X_1D)
rmse, p, Z_1,Z_2,Z_3,Z_4,Z_5,Z_6,Z_7= RMSE_prediction(yhat_4, test_y,s)


ablation_3=np.hstack([rmse,p])


print(rmse)
print(p)



from numpy.ma.core import concatenate

w1=100

inputs_1D = tf.keras.layers.Input( shape=(w1,18))
inputs_1D_N=BatchNormalization()(inputs_1D)


# model_1=Bidirectional(GRU(128, return_sequences=True))(inputs_1D_N)
# model_1=Bidirectional(GRU(64, return_sequences=True))(model_1)

model_1=Bidirectional(LSTM(128, return_sequences=True))(inputs_1D_N)
model_1=Dropout(0.5)(model_1)
# model_2=tf.keras.layers.Concatenate()([model_1, inputs_1D_N])
model_1=Bidirectional(LSTM(64, return_sequences=True))(model_1)
model_1=Dropout(0.5)(model_1)
# model_1=tf.keras.layers.Concatenate()([model_1, model_2])
# model_1=LSTM(32, return_sequences=True)(model_2)

model_1=Dense(128, activation='relu')(model_1)
model_1=Dropout(0.25)(model_1)
model_1=Dense(64, activation='relu')(model_1)
model_1=Dropout(0.25)(model_1)
model_1=Flatten()(model_1)

model_1=Dense(num_pred*w1,bias_regularizer=l2(0.001), activation='linear')(model_1)
output=Reshape(target_shape=(w1,num_pred))(model_1)

model = Model(inputs=inputs_1D, outputs=output)

opt = tf.keras.optimizers.Adam(learning_rate=3e-4)

model.compile(loss=correlation_coefficient_loss_1, optimizer='Adam', metrics=[correlation_coefficient_loss_1])

model.summary()

history=model.fit(train_X_1D, train_y_5, epochs=25, batch_size=64, validation_data=(X_validation_1D, Y_validation), verbose=2, shuffle=False)


model.save(path+'model_LSTM.h5')

yhat_4= model.predict(test_X_1D)
rmse, p, Z_1,Z_2,Z_3,Z_4,Z_5,Z_6,Z_7= RMSE_prediction(yhat_4, test_y,s)


ablation_4=np.hstack([rmse,p])
print(rmse)
print(p)





All_result=np.vstack([ablation_1,ablation_2,ablation_3,ablation_4])

from numpy import savetxt

savetxt(path+subject+'_SOTA_results.csv', All_result, delimiter=',')




######################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################





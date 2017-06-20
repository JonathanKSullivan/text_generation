import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = [series[i:i+window_size] for i in range(len(series) - window_size)]
    y = series[window_size:]
    
        
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    model = Sequential()
    model.add(Dense(128, activation='softmax', input_shape = (7,1)))
    model.add(LSTM(128))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='softmax'))
    model.summary()


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    for punc in string.punctuation:
    if punc == ',' or punc == '.':
        continue
    text = text.replace(punc, ' ')

    # remove as many non-english characters and character sequences as you can 


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = [text[i:i+window_size] for i in range(len(text) - window_size)[::step_size]]
    outputs = text[window_size::step_size]
    
    return inputs,outputs
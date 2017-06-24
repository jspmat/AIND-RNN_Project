import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    for ind in range(len(series)-window_size):
        X.append(series[ind:ind+window_size])
        y.append(series[ind+window_size])
        
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)       
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # remove as many non-english characters and character sequences as you can 
    text = text.replace('\xa0',' ')
    text = text.replace('¨',' ')
    text = text.replace('©',' ')
    text = text.replace('ã',' ')
    text = text.replace('¢',' ')
    text = text.replace('@',' ')
    text = text.replace('$',' ')
    text = text.replace('"',' ')
    text = text.replace('%',' ')
    text = text.replace('&',' ')
    text = text.replace('(',' ')
    text = text.replace(')',' ')
    text = text.replace('*',' ')
    text = text.replace('-',' ')
    text = text.replace('/',' ')
    text = text.replace("'",' ')
    for i in range(10):
        text = text.replace(str(i),' ')

    unique_chars = sorted(list(set(text)))
    print(unique_chars)


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    for i in range(0, len(text)-window_size, step_size):
        inputs.append(text[i:i+window_size])
        outputs.append(text[i+window_size])
    
    return inputs,outputs

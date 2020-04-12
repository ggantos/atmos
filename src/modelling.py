import numpy as np
import pickle


# function that segments data into input and target values

def chop_data(dataset, start_index, end_index, input_size, target_size):
    data = []
    labels = []
    
    start_index = start_index + input_size
    if end_index is None:
        end_index = len(dataset) - target_size
    
    for i in range(start_index, end_index):
        indices = range(i-input_size, i)
        data.append(np.reshape(dataset[indices], (input_size, 1)))
        labels.append(dataset[i+target_size])
        
    return np.array(data), np.array(labels)


def save_history(obj, model_name, subd=''):
    with open('../src/models/{}{}_hist.pkl'.format(subd, model_name), 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        
def load_history(model_name, subd=''):
    with open('../src/models/{}{}_hist.pkl'.format(subd, model_name), 'rb') as f:
        return pickle.load(f)

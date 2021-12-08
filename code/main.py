import torch # to test torch
import numpy as np

import sys # required for input argumetns

import bayes_opt # test pip installed package


save_dir = sys.argv[1] # input argument is a directory for saving the resutls
# it is on storage, one folder above code RESULTSDIR=$PBS_O_WORKDIR/..


data_dir = '../data'  # data are avaliable 


a = torch.zeros(5).cuda() ### test GPU


# test data loading
with open(data_dir + '/example_data.txt', 'r') as f:
    data = np.fromstring(f.read(), sep=' ')
    


# save something to save_dir
with open(save_dir + '/result.txt', 'w') as f:
	f.write('sum is ' + str(np.sum(data)))
    
    
# you can see prints in log file
print('print something for log file')



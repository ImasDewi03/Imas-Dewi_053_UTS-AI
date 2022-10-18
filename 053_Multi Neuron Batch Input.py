#insialisasi numpy
import numpy as np 

#inisialisasi variable
inputs  = [[1.3, 2.3, 7.5, 7.8, 9.4, 1.7], 
           [1.17, 0.12, 0.35, 2.45, 6.4, 6.52],
           [2.12, 3.15, 1.13, 2.54, 7.52, 9.48],
           [2.43, 2.56, 4.15, 8.21, 9.1, 7.12],
           [2.34, 5.43, 6.64, 7.77, 8.23, 8.1],
           [1.23, 2.24, 3.57, 4.76, 2.28, 2.3]]

#inisialisasi bobot variable
weights = [[0.5, 0.7, 1.4, 2.7, 7.8, 9.4],
           [0.25, 3.41, 0.97, 0.24, 0.15, 2.41],
           [2.7, 1.3, 1.4, 6.51, 5.1, 6.4],
           [4.1, 2.33, 4.21, 3.25, 1.31, 9.3],
           [2.71, 3.25, 0.24, 1.56, 3.12, 1.92]]

#inisialisasi bias
bias = [2.3, 3.5, 0.1, 1.5, 2.0]

#penghitungan ouput
layer_output = np.dot(inputs, np.array(weights).T)+bias

print(layer_output) 
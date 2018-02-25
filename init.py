import numpy as np
import functions as f

Rr = np.array([[0.7, 0.3]])
uR = np.array([0.9, 0.2])
observations = np.array([1, 1])
alpha = 1.82

T = [[0.7, 0.3], [0.3, 0.7]]
O = [[0.9, 0.0], [0.0, 0.2]]

f.forward(alpha, observations, Rr, uR)
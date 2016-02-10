

from Levenshtein import * 
  

import numpy as np

from sklearn.cluster import dbscan
data = ["ACCTCCTAGAAG", "ACCTACTAGAAGTT", "GAATATTAGGCCGA"]
def lev_metric(x, y):
     i, j = int(x[0]), int(y[0])     # extract indices
     return levenshtein(data[i], data[j])

X = np.arange(len(data)).reshape(-1, 1)
print(X)
#array([[0],
#       [1],
#       [2]])
dbscan(X, metric=lev_metric, eps=5, min_samples=2) 
#([0, 1], array([ 0,  0, -1]))

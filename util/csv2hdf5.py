# adapted from https://stackoverflow.com/questions/27203161/convert-large-csv-to-hdf5

import numpy as np
import pandas as pd
import sys

filename = '/tmp/test.h5'

df = pd.read_csv(sys.argv[1]+".csv",header=None)
print(df)

# Save to HDF5
df.to_hdf(sys.argv[1]+".h5", 'data', mode='w', format='table')
del df    # allow df to be garbage collected

print(pd.read_hdf(sys.argv[1]+".h5", 'data'))
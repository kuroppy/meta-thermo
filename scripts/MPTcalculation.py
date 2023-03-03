import os
import gzip
import numpy as np
import sys

if sys.argv[1].endswith('.gz'):
    with gzip.open(sys.argv[1], mode='rt') as f:
        n_seqs = 0
        seq = ''
        for line in f:
            if line[0] == '>':
                n_seqs += 1
                continue
            seq += line.rstrip()
        u,c = np.unique(np.array(list(seq),dtype=str), return_counts=True)
        count_dict = dict(zip(u,c))
else:
    with open(sys.argv[1]) as f:
        n_seqs = 0
        seq = ''
        for line in f:
            if line[0] == '>':
                n_seqs += 1
                continue
            seq += line.rstrip()
        u,c = np.unique(np.array(list(seq),dtype=str), return_counts=True)
        count_dict = dict(zip(u,c))

numerator = 0
for i in list('IVYWREL'):
    numerator += count_dict[i]

denominator = 0
for i in list('ACDEFGHIKLMNPQRSTVWY'):
    denominator += count_dict[i]

temperature = 937*(numerator/denominator)-335

with open(str(sys.argv[2]), 'a') as f:
    f.write('%s,' % sys.argv[1])
    f.write('%s\n' % round(temperature,2)) 

with open(str(sys.argv[3]), 'a') as f:
    f.write('%s' % sys.argv[1])
    f.write('%s\n' % count_dict)

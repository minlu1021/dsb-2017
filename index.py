"""
Create index files for training and validation subsets
"""
import sys
import os
import numpy as np
import settings


def write_meta(data_path, idx_file, meta):
    with open(os.path.join(data_path, idx_file), 'w') as fd:
        fd.write('uid,flag,z_len,y_len,x_len\n')
        for row in meta:
            fd.write(','.join(row) + '\n')

if len(sys.argv) < 3:
    print('Usage: %s <data-path> <metadata-file>' % sys.argv[0])
    sys.exit(0)

data_path = sys.argv[1]
meta_path = sys.argv[2]
meta_agg = np.loadtxt(meta_path, delimiter=',', skiprows=1, dtype=bytes).astype(str)

meta = []
for row in meta_agg:
    uid, label = row[0], row[1]
    filename = uid + '.' + settings.file_ext
    if os.path.exists(os.path.join(data_path, filename)):
        meta.append(row)
    else:
        print('could not find %s' % filename)

print('%d samples' % len(meta))
train_len = int(len(meta) * 0.8)
train_meta = meta[:train_len]
val_meta = meta[train_len:]

write_meta(data_path, 'train-metadata.csv', train_meta)
write_meta(data_path, 'val-metadata.csv', val_meta)

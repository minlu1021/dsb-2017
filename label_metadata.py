# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:40:00 2017

@author: luna
"""

import pandas as pd

metadata = pd.read_csv('E:/stage1/stage1/vids/metadata.csv')
flags = pd.read_csv('stage1_labels.csv')
for i in range(len(metadata)):
    for j in range(len(flags)):
        if metadata['uid'][i] == flags['id'][j]:
            metadata.set_value(i, 'flag', flags['cancer'][j])
metadata.flag = metadata.flag.astype(int)
metadata.z_len = metadata.z_len.astype(int)
metadata.y_len = metadata.y_len.astype(int)
metadata.x_len = metadata.x_len.astype(int)
metadata.to_csv('E:/stage1/stage1/vids/metadata_labeled.csv', index = False)
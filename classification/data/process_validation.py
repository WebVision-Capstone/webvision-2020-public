#!/usr/bin/env python

import glob
import os
from shutil import copyfile

synset_to_index = dict()
index_to_synsets = dict()

# read in the synset map
with open(primary_path + 'info/synsets.txt', 'r') as f:
    for i, line in enumerate(f):
        syn = line.split(' ')[0]
        synset_to_index[syn] = i
        index_to_synsets[i] = syn

# build validation dirs
os.mkdir(primary_path + '/validation')
for syn in synset_to_index.keys():
    os.mkdir(primary_path + '/validation/' + syn)

# distribute files (copy)
with open(primary_path + 'meta/val.txt', 'r') as f:
    for line in f:
        line = line.strip()
        img_name, syn_idx = line.split(' ')
        original_path = primary_path + 'val/' + img_name
        new_path = primary_path + 'validation/' + index_to_synsets[int(syn_idx)] + '/' + img_name
        copyfile(original_path, new_path)

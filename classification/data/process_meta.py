
#!/usr/bin/env python

import glob
import os
import json
from pathlib import Path
from shutil import copyfile
from collections import defaultdict

# get a list of all query files
files = glob.glob('./google/*') + glob.glob('./flickr/*')

# read in the id to synset mapping
id_synset_mapping = defaultdict(list)

with open('./meta/train.txt') as f:
    for line in f:
        synset, id_ = line.split(' ')[0].split('/')
        id_ = id_.split('.')[0]
        id_synset_mapping[id_] += [synset]

for file in files:
    with open(file, 'r') as f:
        # read the query files
        lines = json.load(f)
        # distribute each json object in a pair file
        for json_item in lines:
            for synset in id_synset_mapping[json_item['id']]:
                with open('./train/' + synset + '/' + json_item['id'], 'w') as outfile:
                    json.dump(json_item, outfile)

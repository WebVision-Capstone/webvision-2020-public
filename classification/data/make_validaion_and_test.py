""" sets up val2 and test2 directories
takes a 4% random sample from each synset in the original training dataset
splits that sample into val2 and test2
--doing this removes human annotations completely from training process
val2: ~ 50% (rounding)
test2: ~ 50% (rounding)

aggregates all metadata files into mega_meta.json
Writes copies of relevant metadata (id, title, description) to val2 and test2 folders
"""

import os
import glob
from pathlib import Path

import numpy as np
random_state = np.random.RandomState(42)


new_val_path = './val2'
new_test_path = './test2'
classes = sorted(glob.glob('./train/*'))


os.mkdir(new_test_path)
os.mkdir(new_val_path)

# find all classes and create new dirs
for c in classes:
    c = c.split('/')[-1]
    os.mkdir(new_test_path + '/' + c)
    os.mkdir(new_val_path + '/' + c)


# sample and move files per class
for i, c in enumerate(classes):
    print(f'Working on class {i}')
    print(c)
    # get class files
    files = sorted(glob.glob(c + '/*.*'))
    # randomly sample
    sample = random_state.choice(files, int(len(files) * 0.04), replace = False)
    # split into val and test sets
    val, test = sample[:int(len(sample)/2)], sample[int(len(sample)/2):]

    for v in val:
        new_path = v.split('/')
        new_path[1] = new_val_path[2:]
        new_path = '/'.join(new_path)
        # move image
        os.rename(v, new_path)
        # create json path from image path
        json_path = './' + str(Path(v).with_suffix(''))
        new_json_path = './' + str(Path(new_path).with_suffix(''))
        # ignore files with the same name
        if (not os.path.exists(new_json_path)) and os.path.exists(json_path):
            # move json file
            os.rename(json_path, new_json_path)
        else:
            print('possible error with ' + json_path)

    for v in test:
        new_path = v.split('/')
        new_path[1] = new_test_path[2:]
        new_path = '/'.join(new_path)
        # move image
        os.rename(v, new_path)
        # create json path from image path
        json_path = './' + str(Path(v).with_suffix(''))
        new_json_path = './' + str(Path(new_path).with_suffix(''))
        # move json file
        os.rename(json_path, new_json_path)
        # ignore files with the same name
        if (not os.path.exists(new_json_path)) and os.path.exists(json_path):
            # move json file
            os.rename(json_path, new_json_path)
        else:
            print('possible error with ' + json_path)


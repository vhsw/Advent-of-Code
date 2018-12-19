import numpy as np
import scipy.misc

path = 'Day 17/result1'
with open(path + '.txt') as f:
    data = f.read().splitlines()
d = {'.': (255, 255, 255),
     '#': (203, 65, 84),
     '~': (0, 47, 75),
     '|': (0, 59, 95),
     '$': (0, 47, 75),
     '+': (63, 183, 255),
     }
res = []
for line in data:
    row = []
    for el in line:
        row.append(d[el])
    res.append(row)
img = np.array(res, dtype=np.uint8)
scipy.misc.imsave(path + '.png', img)

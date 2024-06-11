# -*- coding: utf-8 -*-

import numpy as np

u = np.array([1,0])
v = np.array([4,0])

print(f"u = {u}")
print(f"v = {v}")
print("")

def collinear(u, v):
    cross_product = np.cross(u, v)
    if cross_product == 0:
        print("The vectors u and v are collinear.")
    else:
        print("The vectors u and v are not collinear.")
        
collinear(u, v)
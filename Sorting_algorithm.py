# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:34:03 2020

@author: tobia
"""

from random import seed
from random import randint

seed(1)

sequence = []
for i in range(10):
    value = randint(0,10)
    sequence.append(i)
    

def quick_sorting(sequence):
    lenght = len(sequence)
    if lenght <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    greater = []
    lower = []
    
    for item in sequence:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quick_sorting(lower) + [pivot] + quick_sorting(greater)

print(quick_sorting([3,5,8,6,5,4,1,2,7,5,3,9,8,1,5,6,8,9,1,2,3,7,8]))        
    
    
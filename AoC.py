#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:17:03 2021

@author: kookoo2052
"""
import numpy as np
# os.chdir('~/2021/AoC')
infile = np.loadtxt('/Users/kookoo2052/2021/AoC/day1.txt')
#%%
print(len(np.where((infile[:-1]-infile[1:])>0)))

#%%
print(len(np.where(((infile[3:]+infile[2:-1]+infile[1:-2])-(infile[:-3]+infile[1:-2]+infile[2:-1]))>0)[0]))

#%%
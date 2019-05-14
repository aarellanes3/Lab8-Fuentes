# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:56:39 2019

@author: aarel
"""
import math
import mpmath
import random 

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def find(S,i):
    if S[i]<0:
        return i
    return find(S,S[i])

def union(S,i,j):
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj:  
        S[rj] = ri  

def trig_identities(trig):
    for i in range(len(trig)):
        for j in range(len(trig)):
            f1 = eval(trig[i])
            f2 = eval(trig[j])
            if f1 == f2:
                print("True")
            else:
                print ("False")
            
t = random.randint(-mpmath.pi,mpmath.pi)            
trig = ['mpmath.sin(t)','math.cos(t)','mpmath.tan(t)','mpmath.sec(t)','−mpmath.sin(t)','−math.cos(t)','−mpmath.tan(t)','mpmath.sin(−t)','math.cos(−t)','mpmath.tan(−t)','mpmath.sin(t)/math.cos(t)', '2*mpmath.sin(t/2)*math.cos(t/2)','sin(t)**2', '1 − math.cos(t)/2','1−math.cos(2t)/2','1/math.cos(t)']
trig_identities(trig)


def partition(S):
    if len(S)%2 == 1:
        return False
    else:
        S1 = DisjointSetForest(len(S)//2)
        S2 = DisjointSetForest(len(S)//2)
        for i in range(len(S)):
            if S[i]%2 ==1:
                union(S1,S[i],i)
            else:
                union(S2,S[i],i)
        return True
    
t = random.randint(-mpmath.pi,mpmath.pi)            
trig = ['mpmath.sin(t)','math.cos(t)','mpmath.tan(t)','mpmath.sec(t)','−mpmath.sin(t)','−math.cos(t)','−mpmath.tan(t)','mpmath.sin(−t)','math.cos(−t)','mpmath.tan(−t)','mpmath.sin(t)/math.cos(t)', '2*mpmath.sin(t/2)*math.cos(t/2)','sin(t)**2', '1 − math.cos(t)/2','1−math.cos(2t)/2','1/math.cos(t)']
trig_identities(trig)

    
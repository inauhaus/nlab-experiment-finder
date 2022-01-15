#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:19:34 2022

@author: in2293
"""

import numpy as np

def mat2list(mat):
    
    #This takes a string, 'mat', which is a snippet of MATLAB code that generates a vector.
    #It returns the corresponding string that could be evaluated as a python list.
    #Could just evaluate the string in MATLAB and return it, but this assumes you don't
    #have access to MATLAB.
    
    #Each conditional is a different way to create a MATLAB/Python vector
    #It converts the notation to Python/Numpy from Matlab
        
    #This performs the conversion for each element separated by a space inside a set of brackets
    def mat2list_x(mat): 
        
    
        if ':' in mat: 
            
            mat = mat.split(':')
            mat = [float(i) for i in mat]
            if len(mat) == 3:   #e.g. 0:45:315
                nparray = np.arange(mat[0],mat[2]+mat[1],mat[1])
                
            else:               #e.g. 3:20
                nparray = np.arange(mat[0],mat[1]+1)
                
            lst = list(nparray)
         
        elif 'linspace' in mat:
            mat = mat.replace('linspace','np.linspace')
            nparray = eval(mat)
            lst = list(nparray)
            
        elif 'logspace' in mat:
            
            def log10(x):  #MATLAB function is log10
                return np.log10(x) 
            
            mat = mat.replace('logspace','np.logspace')
            nparray = eval(mat)
            lst = list(nparray)
            
        else:

            try:
                lst = [float(mat)]
            except:
                lst = [mat]

    
        return lst
    
    
    
    #Convert basic math notation from MATLAB to Python
    mat = mat.replace('./','/').replace('.*','*').replace('^','**').replace('.^','**')
    
    out = []
    if '[' in mat: #e.g. [1 2  1:4]
        
        mat = mat.replace(']','').replace('[','') #Remove brackets
        mat = mat.replace(',',' ') #Replace commas with a space
        
        mat = mat.split(' ')
        for _ in range(mat.count('')):     #removes double/triple... spaces
                mat.remove('')
        
        #Loop through each element of mat = [A B C...]
        for elem in mat:
            out = out + mat2list_x(elem) #join the lists
        
    else:  
        #If there are no brackets, spaces lose meaning in MATLAB
        mat = mat.replace(' ','')
        out = mat2list_x(mat)
    
    return out
    
    
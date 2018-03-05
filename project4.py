# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 02:34:06 2018

@author: meghaerappa
"""
import numpy as np
import copy
import sys
import time
start_time = time.time()


def Align(x,y,match, mismatch,gap):   
    x_list = list(x)
    y_list = list(y)
    
    
    len_x = len(x)

    len_y=len(y)
 
    j =0
    
    first_row = [0 for i in range(len_x + 1)] #across 
    second_row = [0 for i in range(len_x + 1)]  #across
    
    for i in range(1, len_x +1):
        first_row[i] = first_row[i-1]+ gap
    
    for j in range(1,len_y+1):
        for i in range(1, len_x + 1):
            second_row[0] = first_row[0]+gap
   
            if x_list[i-1]==y_list[j-1]:  #was y_list[i-1]
                second_row[i]= first_row[i-1] +2
                #maxx = max(first_row[i-1], first_row[i],second_row[i-1])
                #second_row[i] = maxx+match
            else:
                maxx = max(first_row[i-1], first_row[i],second_row[i-1])
                second_row[i] = maxx+mismatch
        print(first_row)
        print (second_row)
        print("--------")
        
        
        first_row = copy.deepcopy(second_row)
  
    
        
    return second_row[-1]


def main():
    sequence1 = input("Input sequence: ")
    sequence2 = input("Input sequence: ")
    match= input("match number: ")
    mismatch = input("mismatch number: ")
    gap = input("gap number: ")
    
    try:

        file1 = open(sequence1,'r')
        file2 = open(sequence2,'r')
        text = file1.read().replace('\n','')
        print(text)
        pattern = file2.read().replace('\n','')
        print(pattern)
        match = int(match)
        mismatch = int(mismatch)
        print(mismatch)
        gap =int(gap)
        print("Optimal alignment score is: " ,Align(text,pattern,match,mismatch,gap))  

        
         
    except IOError:
        print("Unable to open files!")
        
main()

#seq1 = sys.argv[1]
#seq2 = sys.argv[2]
#macth
#
#open blusshiittttttt
#Align(seq1,seq2,match,mismatch,gap) 
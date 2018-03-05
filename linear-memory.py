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

#recursive function that outputs the score.
#X and Y are sequences
def Align(x,y,match, mismatch,gap):   
   #creating lists for the sequences 
    x_list = list(x)
    y_list = list(y)
   # get the length of the sequences
    len_x = len(x)
    len_y=len(y)
   
    j =0
    
    first_row = [0 for i in range(len_x + 1)] #across 
    second_row = [0 for i in range(len_x + 1)]  #across
    
    #initializing first row with gap values 
    for i in range(1, len_x +1):
        first_row[i] = first_row[i-1]+ gap
    
    #itirating through the rows across by looking at every j value(down)
    for j in range(1,len_y+1):
        for i in range(1, len_x + 1):
            second_row[0] = first_row[0]+gap
   
            if x_list[i-1]==y_list[j-1]:  #if the chars are the same
                second_row[i]= first_row[i-1] +2  #adding the match value 
            else:
                maxx = max(first_row[i-1], first_row[i],second_row[i-1]) #if they're not the same
                second_row[i] = maxx+mismatch
        print(first_row)
        print (second_row)
        print("--------")
        
        
        first_row = copy.deepcopy(second_row) #since we're mainting only two rows we have to copy the second row to the first.
  
    
        
    return second_row[-1] #gives out the count 


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

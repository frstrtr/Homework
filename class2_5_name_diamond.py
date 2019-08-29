"""Write a function named name_diamond that accepts a string as a parameter and prints it in a "diamond" format as shown below. For example, the call of name_diamond("MARTY") should print:

M
MA
MAR
MART
MARTY
 ARTY
  RTY
   TY
    Y
    
"""
from __future__ import print_function

def name_diamond(str1):

    str2=''
    i=''
    
    for i in str1:
            
        str2=str2+i
        print (str2)
        
        ix=1
        
    for i in str1:
        
        print (' '*ix,end='')
        print(str1[ix::])
        ix+=1

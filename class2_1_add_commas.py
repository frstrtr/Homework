"""
# add_commas  Favorite
#Language/Type: Python String return
#Author: Marty Stepp (on 2017/07/08)

#Write a function named add_commas that accepts a string representing a number and returns a new string with a comma 
#at every third position, starting from the right. For example, the call of add_commas("12345678") returns "12,345,678".
"""

from __future__ import print_function

def add_commas(str1):
    l=len(str1)-1
    n=1
    str2=''
    while l != -1:
        
        #print(str1[l],end="")
        str2=str1[l]+str2
        l -= 1
        
        if n == 3 and l !=-1:
            #print(',', end="")
            str2=','+str2
            n=1
        else:
            n+=1
    #print('/n')
    return str2

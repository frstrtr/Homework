"""
reverse  Favorite
Language/Type: Python strings
Author: Melissa Hovik (on 2017/07/08)

Write a function named reverse that accepts a string parameter returns a new string with the characters in the opposite order. For example, A call of reverse("Pikachu") would return "uchakiP".
"""

def reverse(str1):
    str1_reversed = ''
    i=len(str1)-1
    
    while i!=-1:
        str1_reversed = str1_reversed+str1[i]
        i-=1
        
    return str1_reversed
    #return str1[::-1] - maybe better?

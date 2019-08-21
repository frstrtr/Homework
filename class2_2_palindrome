"""
is_palindrome  Favorite
Language/Type: Python strings parameters return boolean
Author: Marty Stepp (on 2017/07/08)

Write a function named is_palindrome that accepts a string parameter and returns True if that string is a palindrome, or False if it is not a palindrome.

For this problem, a palindrome is defined as a string that contains exactly the same sequence of characters forwards as backwards, case-insensitively. For example, "madam" or "racecar" are palindromes, so the call of is_palindrome("racecar") would return True. Spaces, punctuation, and any other characters should be treated the same as letters so a multi-word string such as "dog god" could be a palindrome, as could a gibberish string such as "123 $$ 321". The empty string and all one-character strings are palindromes by our definition. Your code should ignore case, so a string like "Madam" or "RACEcar" would also count as palindromes.

"""

def is_palindrome(str1):
    str1_lower = str1.lower()
    i=0
    length = len(str1_lower)
    
    while i!=length:
        
        #print(str1_lower[i],str1_lower[(length-i-1)])
        
        
        if str1_lower[i]!=str1_lower[(length-i-1)]:
            return False
            break
        else:
            i+=1
            
    return True

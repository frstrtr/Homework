"""Write a function named switch_pairs that accepts a string as a parameter and returns that string with each pair 
of neighboring letters reversed. If the string has an odd number of letters, the last letter should not be modified. 
For example, the call switch_pairs("example") should return "xemalpe" and the call switch_pairs("hello there") should 
return "ehll ohtree"."""

def switch_pairs(str1):
    
    str2=''
    ix=0
    
    for i in str1:
        
        if not ix%2 and ix<len(str1)-1:
            
            str2=str2+str1[ix+1]+str1[ix]
            #print(str1[ix+1]+str1[ix])
            ix+=2
            
    if len(str1)%2:
        str2=str2+str1[ix]
        
    return str2

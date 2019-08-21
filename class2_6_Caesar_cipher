"""
Write a complete console program that implements a Caesar cipher or rotation cipher,
which is a crude system of encoding strings by shifting every letter forward by a given number.
Your program should prompt the user to type a message and an encoding "key" (number of places to shift each character)
and display the shifted message. For example, if the shift amount is 3, then the letter A becomes D, and B becomes E, 
and so on. Letters near the end of the alphabet wrap around for a shift of 3, X becomes A, and Y becomes B, 
and Z becomes C. 
Here are two example dialogues:

Your message? Attack zerg at dawn
Encoding key? 3
DWWDFN CHUJ DW GDZQ
Your message? DWWDFN CHUJ DW GDZQ
Encoding key? -3
ATTACK ZERG AT DAWN
"""
while True:
    mes = raw_input('Your message?')
    key = int(raw_input('Encoding key?'))
    encoded_message=''
    message = mes.upper()
    #shift_roll=0

    for c in message:

        #check for space
        if ord(c)==32:
            encoded_message=encoded_message+' '
        #check for '
        elif ord(c)==39:
            encoded_message=encoded_message+"'"
        #check for "
        elif ord(c)==34:
            encoded_message=encoded_message+'"'
        #check for !
        elif ord(c)==33:
            encoded_message=encoded_message+'!'
        elif (ord(c)+key)>90:
            encoded_message=encoded_message+chr(ord(c)+key-26)
        elif (ord(c)+key)<65:
            encoded_message=encoded_message+chr(ord(c)+key+26)
        else:
            encoded_message=encoded_message+chr(ord(c)+key)

    #print (message)
    #print(key)
    print(encoded_message)

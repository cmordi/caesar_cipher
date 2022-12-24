#program gives you option to brute force all of the shift values

import sys

def inputMsg():
    msg = input("Please input your message: ")
    return msg  #might be something wrong with this line

def pullKey():
    start = 0 

    while True:
        print("Please enter shift num: ", end = " ")
        
        user_input = int(input())
        if user_input >= 1 and user_input <= 26:
            return user_input
        else:
            print("Value has to fall in range 1 and 26")
            sys.exit(0)  #provides a zero error code for shell 

def decipher(no_change, msg, key):
    decoded = ""
    
    if no_change == 1:
        key = -key

    for symbol in msg:              
        if symbol.isalpha():
            number = ord(symbol)
            number += key
            
            if symbol.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
            elif symbol.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            decoded += chr(number)
            
        else:
            decoded += symbol
    print(f"\n{decoded}")
            

bool_input = "y" 

while bool_input:
    print("""
Select action that you want:
          
1) Decrypt
2) Encrypt
3) Decrypt (with no knowm shift)
4) Leave program :)
        
""")
    
    usr_input = int(input("Select an option:"))
    print(usr_input)
    
    if usr_input == 1 or usr_input == 2:
        msg = inputMsg()
        pk = pullKey()
        
        print("The message is: ")
        
        decipher(usr_input, msg, pk)
        
    elif usr_input == 3:
        msg = inputMsg()
        print("List of attempted decodes: \n")
        
        for i in range(1, 26):
            print(f"The shift = {i}: ", end = " ")
            decipher(usr_input, msg, i)
            print()
            
    elif usr_input == 4:
        sys.exit(0)     #provides a zero error code for shell
    
    else:
        ("Please try again :(")
    
    bool_input = input('Type any key + "enter" to go back to main menu: ')
        

        
        
        
    
    
    
    

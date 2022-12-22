import sys

def inputMsg():
    msg = input("Please input your message: ")
    return msg

def decipher(message, key, mode):
    decoded = ""
    
    if mode == 1:
        key = -key

    for symbol in message:
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
            

def pullKey():
    start = 0 

    while True:
        print("Please enter shift num: ", end = " ")
        
        user_input = int(input())
        if user_input >= 1 and user_input <= 26:
            return user_input
        else:
            print("Value has to fall in range 1 and 26")
            sys.exit(0)  #zero error code for shell
            

usr_input = "Y" 

while usr_input:
    print("""Select what you want:
          
        1) 
          
            """)
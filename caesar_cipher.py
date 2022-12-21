import sys



def inputMsg():
    msg = input("Please input your message: ")
    return msg

def decipher():
    pass

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
            

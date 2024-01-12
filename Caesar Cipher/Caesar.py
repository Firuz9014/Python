# print(ord('S'))

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def Encryption(message, shift):
    result = ""
    for char in message.lower():
        if char == ' ':
            result = result + char
            continue
        if   ord(char) > 122 or ord(char) < 97:
            result = result + char
        elif (ord(char) + shift) > 122:
            tmp = chr(ord(char) + shift - 25)
            result = result + tmp
        else:
            tmp = chr(ord(char) + shift)
            result = result + tmp
    return result



def Decryption(message, shift):
    result = ""
    for char in message.lower():
        if char == ' ':
            result = result + char
            continue
        if   ord(char) > 122 or ord(char) < 97:
            result = result + char
        elif (ord(char) - shift) < 97:
            tmp = chr(ord(char) - shift + 25)
            result = result + tmp
        else:
            tmp = chr(ord(char) - shift)
            result = result + tmp
    return result



def main():
    print(logo)
    print("Welcome \n1.Encrypt \n2.Decrypt \n3.Exit")
    status = True
    while(status):
        choice = int(input("Please, enter your choice (1,2 or 3): "))
        if choice == 1:
            message = input("Enter the message for encryption: ")
            shift = int(input("Shift Number: "))
            print(Encryption(message, shift))
        elif choice == 2:
            message = input("Enter the message for decryption: ")
            shift = int(input("Shift Number: "))
            print(Decryption(message, shift))
        elif choice == 3:
            print("See you soon!")
            return
        else:
            print("Invalid input, please, try again")
            continue






main()

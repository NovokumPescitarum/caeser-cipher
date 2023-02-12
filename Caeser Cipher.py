modulus = 26 #Since alphabet is twenty-six letters, this means 0 - 25

alphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#inputString = input("Enter the message you wish to encrypt: ")

def listToString(string):
    # initialization of string to ""
    new = ""
    # traverse in the string
    for x in string:
        new += x
    # return string
    return new

encryptedLetters = []
def encrypt(winput,key):
    for letter in winput.upper():
        if letter == " ":
            encryptedLetters.append(letter)
        else:
            letterLocation = alphabetList.index(letter)
                
            substitutedEncryptedLetter = alphabetList[(letterLocation + int(key)) % modulus]

            encryptedLetters.append(substitutedEncryptedLetter)

    return listToString(encryptedLetters)


decryptedLetters = []
def decrypt(winput,key):
    for letter in winput.upper():
        if letter == " ":
                decryptedLetters.append(letter)
        else:
                letterLocation = alphabetList.index(letter)
                    
                substitutedDecryptedLetter = alphabetList[(letterLocation - int(key)) % modulus]

                decryptedLetters.append(substitutedDecryptedLetter)

    return listToString(decryptedLetters)



     

def main():
    while True: 
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice == "e":
            winput = input("Enter the message you wish to encrypt: ")
            key = input("Enter the cipher shift key you want to use (1,2,3...26): ")
            print("The encrypted message is:", encrypt(winput,key))
            break
        elif choice == "d":
            winput = input("Enter the message you wish to decrypt: ")
            key = input("Enter the cipher shift key you want to use (1,2,3...26): ")
            print("The decrypted message is:", decrypt(winput,key))
            break
        else:
            print("Invalid input, please try again.")

main()
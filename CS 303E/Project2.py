# File: Project2.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 04/09/2021
# Date Last Modified: 04/12/2021
# Description of Program: This program is a substitution cipher that runs a loop that allows you
# to get a key, change the key, encrypt a text, and decrypt a text. There is a substitution cipher class that
# sets the key, get the key, encrypt, and decrypt while a key is legal. There is a main function that runs a
# loop that generates a random key and executes commands given.

import random

# A global constant defining the alphabet. 
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or 
# define your own.   You don't need to understand this code at this
# point in the semester. 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

# There may be some additional auxiliary functions defined here.
# I had several others, mainly used in encrypt and decrypt. 
def encryptDecrypt( self, key, alphabet, text ):
        textList = list(text)
        keyList = list(key)

        index = 0
        for i in text:
            iUpper = i.isupper()
            if i.isalpha() == False:
                asciiVal = ord(i)
            else:
                i = i.lower()
                asciiVal = ord(i) - 96
            if asciiVal <= 26:
                if iUpper == True:
                    textList[index] = keyList[alphabet.index(i)].upper()
                else:
                    textList[index] = keyList[alphabet.index(i)]
            index += 1
        return ''.join(textList)
    
class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        self.__key = key
        if isLegalKey(self.__key) == False:
            print("Key entered is not legal")
            

    # Note that these are the required methods, but you may define
    # additional methods if you need them.  (I didn't need any.)

    def getKey( self ):
        """Getter for the stored key."""
        return self.__key
        
    def setKey( self, newKey ):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if isLegalKey(self.__key) == True:
            self.__key = newKey

    def encryptText( self, plaintext ):
        """Return the plaintext encrypted with respect to the stored key."""
        return encryptDecrypt(self, self.__key, LCLETTERS, plaintext)
        
        
    def decryptText( self, ciphertext ):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        return encryptDecrypt(self, LCLETTERS, self.__key, ciphertext)

def main():
    """ This implements the top level command loop.  It
    creates an instance of the SubstitutionCipher class and allows the user
    to invoke within a loop the following commands: getKey, changeKey,
    encrypt, decrypt, quit."""
    cipher = SubstitutionCipher()
    command = ''
    validCommands = "getKey, changeKey, encrypt, decrypt, quit"
    while command != 'quit':
        command = input("Enter a command (%s): " %validCommands).lower()

        #getKey algorithm
        if command == 'getkey':
            key = cipher.getKey()
            print("  Current cipher key:", key)

        #changeKey algorithm    
        if command == 'changekey':
            changeKey = ''
            while changeKey != 'quit':
                changeKey = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
                if changeKey == 'random':
                    key = cipher.setKey(makeRandomKey())
                    print("    New cipher key:", cipher.getKey())
                    break
                elif isLegalKey(changeKey) == True:
                    key = cipher.setKey(changeKey)
                    print("    New cipher key:", cipher.getKey())
                    break
                elif changeKey == 'quit':
                    break
                else:
                    print("    Illegal key entered. Try again!")
                
        #encrypt algorithm
        if command == 'encrypt':
            text = input("  Enter a text to encrypt: ")
            encryptedText = cipher.encryptText(text)
            print("    The encrypted text is:", encryptedText)

        #decrypt algorithm
        if command == 'decrypt':
            text = input("  Enter a text to decrypt: ")
            decryptedText = cipher.decryptText(text)
            print("    The decrypted text is:", decryptedText)
        elif command not in validCommands.lower():
            print("  Command not recognized. Try again!")
    print("Thanks for visiting!")
    

main()
    

#!/usr/bin/env python3
import base64
import hashlib

# DISCLAIMER: This should not be considered safe encryption, and as such, should not be used to
# obfuscate sensitive information. The purpose of this script is simply to code and learn about
# information obfuscation.


"""
First takes a message from stdin from user, then takes 'password' to encrypt message with from
stdin from user.
Prints encrypted message.
"""


def encrypt():
    print("--------------------------------------------------------------\n")
    print("Please enter the message you wish to encrypt.")
    raw_message = input("MESSAGE: ")
    print("\n\nPlease enter the key to encrypt the message: ")
    key = input("KEY: ")
    key = hashlib.md5(base64.b64encode(key.encode())).hexdigest()
    enc = []
    for i in range(len(raw_message)):
        key_char = key[i % len(key)]
        enc.append(chr((ord(raw_message[i]) + ord(key_char)) % 256))
    encrypted = base64.urlsafe_b64encode("".join(enc).encode()).decode()
    print("--------------------------------------------------------------")
    print("The encrypted message is below:")
    print("\n\n##############################################################")
    print("##############################################################")
    print(f"\n{encrypted}\n")
    print("##############################################################")
    print("##############################################################\n\n")


"""
First takes encrypted message from stdin from user, then takes 'password' and decrypts the
ciphertext with the password.
Prints the plaintext message.
"""


def decrypt():
    print("--------------------------------------------------------------")
    print("Please enter the message to decrypt")
    encrypted = input("MESSAGE: ")
    try:
        encrypted = base64.urlsafe_b64decode(encrypted).decode()
    except ValueError:
        raise TypeError("Invalid base64 string")
    print("\n\nPlease enter the key to decrypt the message: ")
    key = input("KEY: ")
    key = hashlib.md5(base64.b64encode(key.encode())).hexdigest()
    dec = []
    for i in range(len(encrypted)):
        key_char = key[i % len(key)]
        dec.append(chr((256 + ord(encrypted[i]) - ord(key_char)) % 256))
    decrypted = "".join(dec)
    print("--------------------------------------------------------------")
    print("This is the message decrypted with the provided key")
    print("\n\n##############################################################")
    print("##############################################################")
    print(f"\n{decrypted}\n")
    print("##############################################################")
    print("##############################################################\n\n")


"""
Continuosly prints menu until user quits.
Calls appropriate function based on user input.
On error, informs user of error and returns to main menu.
"""
if __name__ == "__main__":
    exit = False
    while not exit:
        print("##############################################################")
        print("#                                                            #")
        print("#  Please enter the number of the operation you wish to do:  #")
        print("#  1. Encrypt a message                                      #")
        print("#  2. Decrypt a message(Must be valid base64 encoded string) #")
        print("#  3. Exit the program.                                      #")
        print("#                                                            #")
        print("##############################################################")
        try:
            choice = int(input("Your choice: "))
            if choice == 1:
                encrypt()
            elif choice == 2:
                decrypt()
            elif choice == 3:
                exit = True
                print("Exiting...")
            else:
                print(
                    "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                )
                print("     You entered an unknown operation. Please try again.")
                print(
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"
                )
        except TypeError:
            print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("   Invalid encrypted text was provided. Please try again.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
        except ValueError:
            print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" \tYou did not enter a number. Please try again.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

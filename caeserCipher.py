#This file is seperated into 2 parts on how to implement this cipher
#The first implementation involves scaling each letter to an uppercase,
#and using .find() to find the index of each key, encrypted or decrypted.
#The second implementation involes converting each character into its ASCII value,
#then shifting its ASCII value up for encryption, down for decryption.


# THIS IS METHOD 1
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 7

def caeser_encrypt(plain_text, key):
    cipher_text = ""
    upper_text = plain_text.upper()
    for letter in upper_text:
        if letter in upperAlphabet:
            index = upperAlphabet.find(letter)
            encrypted_letter = upperAlphabet[(index + key) % len(upperAlphabet)]
            cipher_text += encrypted_letter
        else:
            cipher_text += letter
    return cipher_text

def caeser_decrypt(cipher_text):
    plain_text = ""
    for char in cipher_text:
        index = upperAlphabet.find(char.upper())
        decrypted_letter = (index - key) % len(upperAlphabet)
        plain_text += upperAlphabet[decrypted_letter]
    return plain_text


#THIS IS METHOD 2

def charShift(char, key):
    if str(char).isupper():
        return chr((ord(char) - 65 + key) % 26 + 65)
    if str(char).islower():
        return chr((ord(char) - 97 + key) % 26 + 97)
    return char

def caeser_encrypt_ASCII(plain_text, key):
    cipher_text = ""
    for letter in plain_text:
        if letter.isalpha():
            cipher_char = charShift(letter, key)
            cipher_text += cipher_char
        else:
            cipher_text += letter
    return cipher_text


def caeser_decrypt_ASCII(plain_text, key):
    return caeser_encrypt_ASCII(plain_text, -key)

print(caeser_decrypt_ASCII("Edoov ythsoha", 3))

        
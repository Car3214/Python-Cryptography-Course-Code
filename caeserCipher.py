upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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

print(caeser_encrypt("hello there", -9))
        
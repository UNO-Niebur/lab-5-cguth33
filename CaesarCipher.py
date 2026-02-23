#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#Name:Carter Guthrie
#Date:2/22/26
#Assignment:Lab 5

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if alpha.find(letter) >= 0: # Check if it's a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # Keep numbers/punctuation as they are
            secret = secret + letter
    return secret

def decode(message, key):
    # Decoding is encoding with a negative shift
    return encode(message, -key)

def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))
    
    secret = encode(message, key)
    print("Encrypted:", secret)
    
    plaintext = decode(secret, key)
    print("Decrypted:", plaintext)

if __name__ == '__main__':
    main()
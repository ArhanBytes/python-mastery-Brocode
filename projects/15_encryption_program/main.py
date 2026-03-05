# ENCRYPTION GAME
import random
import string

def main():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars) # type casting of string to list
    key = chars.copy()
    random.shuffle(key)

    is_running = True
    # ENCRYPT
    while is_running:
        plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for char in plain_text:
            position = chars.index(char)
            cipher_text = cipher_text + key[position]

        print(f"Original Text: {plain_text}")
        print(f"Encrypted text: {cipher_text}")
        
        # DECRYPT
        cipher_text = input("Enter a message to decypt: ")
        plain_text = ""

        for char in cipher_text:
            position = key.index(char)
            plain_text = plain_text +  chars[position]

        print(f"Encrypted text: {cipher_text}")
        print(f"Original Text: {plain_text}")
if __name__ == "__main__":
    main()
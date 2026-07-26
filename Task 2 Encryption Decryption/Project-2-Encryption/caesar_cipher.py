def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_text += encrypted_char
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isupper():
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            decrypted_text += decrypted_char
        elif char.islower():
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("-" * 50)
    print("DecodeLabs - Project 2: Basic Encryption & Decryption")
    print("-" * 50)
    
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Enter 1 or 2: ")
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please run the program again.")
        return

    text = input("Enter the text: ")
    
    while True:
        try:
            shift_key = int(input("Enter the shift key (integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\n--- Results ---")
    if choice == '1':
        encrypted_message = encrypt(text, shift_key)
        print(f"Original Text : {text}")
        print(f"Shift Key     : {shift_key}")
        print(f"Encrypted Text: {encrypted_message}")
    elif choice == '2':
        decrypted_message = decrypt(text, shift_key)
        print(f"Ciphertext    : {text}")
        print(f"Shift Key     : {shift_key}")
        print(f"Decrypted Text: {decrypted_message}")
    
    print("-" * 50)

if __name__ == "__main__":
    main()
def caesar_cipher(text, key, mode):
    result = ""
    if mode.lower() == 'encrypt':
        for char in text:
            if char.isalpha():
                shift = key if char.islower() else key % 26
                start = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += char
    elif mode.lower() == 'decrypt':
        for char in text:
            if char.isalpha():
                shift = key if char.islower() else key % 26
                start = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - start - shift) % 26 + start)
            else:
                result += char
    return result

def main():
    mode = input("Do you want to encrypt or decrypt? ").strip()
    text = input("Enter the text: ").strip()
    key = int(input("Enter the key: ").strip())
    result = caesar_cipher(text, key, mode)
    
    print(f"Result: {result}")
    print(f"Length of the result: {len(result)}")

if __name__ == "__main__":
    main()

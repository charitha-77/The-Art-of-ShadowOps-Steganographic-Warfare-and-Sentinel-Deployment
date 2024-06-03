# program2.py

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
    filename = input("Enter the filename: ").strip()
    mode = input("Do you want to encrypt or decrypt? ").strip()
    key = int(input("Enter the key: ").strip())
    
    with open(filename, 'r') as file:
        text = file.read()
    
    result = caesar_cipher(text, key, mode)
    
    with open('output.txt', 'w') as output_file:
        output_file.write(result)
    
    print(f"Result has been written to 'output.txt'.")

if __name__ == "__main__":
    main()

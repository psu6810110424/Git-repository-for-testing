def caesar_cipher(s, k):
    result = ""
    k %= 26
    for char in s:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + k) % 26)
        else:
            result += char
    return result
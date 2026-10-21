def whisper_cipher(text: str, shift: int) -> str:
    new = ""
    for n in text:
        if 'a' <= n <= 'z':
            new += chr((ord(n) - ord('a') + shift) %26 + ord('a'))
        elif 'A' <= n <= 'Z':
            new += chr((ord(n) - ord('A') + shift) %26 + ord('A'))
        else:
            new += n
    return new


print(whisper_cipher("hello", 3))#"khoor"
print(whisper_cipher("Hello World!", 1))#"Ifmmp Xpsme!"
print(whisper_cipher("xyz", 3)) #abc
print(whisper_cipher("ABC123def", 5)) #"FGH123ijk"
print(whisper_cipher("", 10)) #""
print(whisper_cipher("abc", -3)) #xyz



##Using list

# def whisper_cipher(text: str, shift: int) -> str:
#     result = []

#     for ch in text:
#         if 'a' <= ch <= 'z':
#             result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
#         elif 'A' <= ch <= 'Z':
#             result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
#         else:
#             result.append(ch)

#     return "".join(result)


# ## withour ord function

# def whisper_cipher(text: str, shift: int) -> str:

#     alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
#     alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = ''

#     for char in text:

#         if char.islower():
#             result += alphabet_lower[(alphabet_lower.index(char) + shift) % 26]

#         elif char.isupper():
#             result += alphabet_lower[(alphabet_upper.index(char) + shift) % 26]
#         else:
#             result += char
#     return result
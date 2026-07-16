def echo_validator(text: str) -> bool:
    if not text:
        return False
    new = ""
    for c in text:
        if c.isalpha():
            new = new + c.lower()
    # print(new)
    # print( new[::-1])
    return new == new[::-1]


## new = "".join(c.lower() for c in text if c.isalpha())

print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("racecar"))

print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator("hello"))
print(echo_validator("Madam Im Adam"))
print(echo_validator(""))


## without isalpha

# def echo_validator(text: str) -> bool:
#     new = ""

#     for c in text:
#         if 'A' <= c <= 'Z':
#             new += chr(ord(c) + 32)
#         elif 'a' <= c <= 'z':
#             new += c

#     return new == new[::-1]
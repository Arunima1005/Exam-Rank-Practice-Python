def string_sculptor(text: str) -> str:
    flag = 0
    for i, s in enumerate(text):
        if s == " ":
            flag = 0
        if s.isalpha() and flag == 0:
            text = text[:i] + s.lower() +text[i+1:]
            flag = 1
        elif s.isalpha() and flag == 1:
            text = text[:i] + s.upper() +text[i+1:]
            flag = 0
    return text

print(string_sculptor("hello"))
print(string_sculptor("Hello World"))
print(string_sculptor("abc123def"))
print(string_sculptor("Python3.9!"))
print(string_sculptor(""))

# ### Usinf list
# def string_sculptor(text: str) -> str:
#     chars = list(text)
#     lower = True

#     for i, ch in enumerate(chars):
#         if ch == " ":
#             lower = True
#         elif ch.isalpha():
#             if lower:
#                 chars[i] = ch.lower()
#             else:
#                 chars[i] = ch.upper()
#             lower = not lower

#     return "".join(chars)


## another way without converting list

# def string_sculptor(text: str) -> str:
#     result = []
#     lower = True

#     for ch in text:
#         if ch == " ":
#             result.append(ch)
#             lower = True
#         elif ch.isalpha():
#             if lower:
#                 result.append(ch.lower())
#             else:
#                 result.append(ch.upper())
#             lower = not lower
#         else:
#             result.append(ch)

#     return "".join(result)
# Problem 10: Number Base Conversion
# Write a function to convert numbers between different bases.

# Support common bases: binary (2), octal (8), decimal (10), hexadecimal (16)
# Input: number as string, source base, target base
# Output: converted number as string
# Examples:
# "1010", base_from=2, base_to=10 → "10"
# "FF", base_from=16, base_to=10 → "255"
# "10", base_from=10, base_to=2 → "1010"


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    decimal = 0

    # for char in number:
    #     if char not in digits[:from_base]:
    #         return "ERROR"


    for n in number.upper():
        if n not in digits:
            return "ERROR"
        value = digits.index(n)
        if value >= from_base:
            return "ERROR"

        decimal = decimal * from_base + value
    if decimal == 0:
        return "0"
    result = "" 
    while decimal > 0:
        remainder = decimal % to_base
        result = digits[remainder] + result
        decimal =  decimal // to_base
    return result


print(number_base_converter("1010", 2, 10)) # 10
print(number_base_converter("FF", 16, 10)) # 255
print(number_base_converter("255", 10, 16)) # FF
print(number_base_converter("123", 10, 2)) # 1111011
print(number_base_converter("Z", 36, 10)) #35
print(number_base_converter("35", 10, 36)) #Z
print(number_base_converter("123", 1, 10)) #ERROR
print(number_base_converter("G", 16, 10)) #ERROR
print(number_base_converter("1A", 16, 10))      # 26

# number_base_converter("1010",2, 0)
# number_base_converter("FF", 16, 0)
# number_base_converter("Z", 36, 0)


###Using build-in function Int() to convert decimal

# def number_base_converter(number: str,
#                           from_base: int,
#                           to_base: int) -> str:
#     """
#     Converts a number from one base to another.
#     Support bases from 2 to 36 inclusive.
#     Use digits 0-9 and letters A-Z for values 10-35.
#     Return "ERROR" for invalid inputs
#     """
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     if not 2 <= from_base <= 36:
#         return "ERROR"
#     if not 2 <= to_base <= 36:
#         return "ERROR"
#     try:
#         decimal = int(number, from_base)
#     except ValueError:
#         return ("ERROR")
#     if decimal == 0:
#         return "0"
#     result: str = ""
#     while decimal > 0:
#         result = digits[decimal % to_base] + result
#         decimal //= to_base
#     return result

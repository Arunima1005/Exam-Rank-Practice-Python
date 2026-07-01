import string
def print_rangoli(size):
    # your code goes here
    alphabets = string.ascii_letters
    width = 4 * size - 3
    lines = []
    for i in range(size):
        letters = alphabets[i:size]
        # print(letters)
        row_letters = list(reversed(letters)) + list(letters[1:])
        # print(row_letters)
        row_line = "-".join(row_letters)
        lines.append(row_line.center(width, "-"))
    full_rangoli = lines[::-1] + lines[1:]
    # print(full_rangoli)
    print("\n".join(full_rangoli))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
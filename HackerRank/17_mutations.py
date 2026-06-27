def mutate_string(string, position, character):
    # return string[:5] + character + string[6:] -- another option
    l = list(string)
    l[position] = character
    return "".join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
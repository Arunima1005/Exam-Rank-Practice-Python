if __name__ == '__main__':
    s = input()
    words = s.split(" ")
    org_str = [(word[:1].upper() + word[1:]) for word in words]
    print(" ".join(org_str))
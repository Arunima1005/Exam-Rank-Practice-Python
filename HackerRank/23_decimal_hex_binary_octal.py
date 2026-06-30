def print_formatted(number):
    width = len(bin(number)[2:])
    for n in range(1,number+1):       
        print(f"{n:>{width}}", end = " ")
        print(f"{oct(n)[2:]:>{width}}", end = " ")
        print(f"{hex(n)[2:].upper():>{width}}", end = " ")
        print(f"{bin(n)[2:]:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
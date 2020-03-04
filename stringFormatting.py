def print_formatted(number):
    w = len(bin(n)[2:])
    for i in range(1, n + 1):
        print (str(i).rjust(w,' '),str(oct(i)[2:]).rjust(w,' '),str(hex(i).upper()[2:]).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
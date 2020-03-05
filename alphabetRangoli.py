def print_rangoli(size):
    alphabets = []
    for i in range(1, n + 1):
        alphabets.append(chr(65+n-i).lower().center(0))
        lines = '-' * int((n - i) / 0.5)
        alphabetsLeft = '-'.join(alphabets)
        alphabetsRight = '-'.join(reversed(alphabets))
        final = [lines,alphabetsLeft.strip(),alphabetsRight[1:].strip(),lines]
        finalPrint = ''.join(final).strip('')
        print(finalPrint)

    for i in range(1, n):
        del alphabets[n-i:]
        lines = '-' * int(i *2)
        alphabetsLeft = '-'.join(alphabets)
        alphabetsRight = '-'.join(reversed(alphabets))
        final = [lines, alphabetsLeft.strip(), alphabetsRight[1:].strip(), lines]
        finalPrint = ''.join(final).strip('')
        print(finalPrint)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

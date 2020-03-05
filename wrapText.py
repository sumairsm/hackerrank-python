import textwrap

def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    listed = []
    for i in wrapped:
        listed.append(i)
    return '\n'.join(listed)




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
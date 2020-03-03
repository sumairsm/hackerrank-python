if __name__ == '__main__':
    s = input()
    val = list(s)

print(any(c.isalnum() for c in val))
print(any(c.isalpha() for c in val))
print(any(c.isdigit() for c in val))
print(any(c.islower() for c in val))
print(any(c.isupper() for c in val))
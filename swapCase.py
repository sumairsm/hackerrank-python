def swap_case(s):
    createList = list(s)
    convertedList = []
    for i in range(len(createList)):
        if createList[i].isupper():
            convertedList.append(createList[i].lower())
        else:
            convertedList.append(createList[i].upper())

    return ''.join(convertedList)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
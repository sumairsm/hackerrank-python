if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    scores.sort(reverse=True)
    first = scores[0]
    for i in range(n):
        if first == scores[0]:
            scores.remove(first)
        else:
            continue
    print(scores[0])



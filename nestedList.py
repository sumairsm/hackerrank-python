if __name__ == '__main__':
    names = []
    scores = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        nameScores = list(zip(names, scores))

    scores.sort()
    last = scores[0]

    for j in range(len(scores)):
        if last == scores[0]:
            scores.remove(last)
        else:
            continue
    secondLowestScore = scores[0]
    secondLowestName = []
    for k in nameScores:
        if k[1] == secondLowestScore:
            secondLowestName.append(k[0])
        else:
            continue
    secondLowestName.sort()

    for names in secondLowestName:
        print(names)

""""
4
Rachel
-50
Mawer
-50
Sheen
-50
Shaheen
51
"""
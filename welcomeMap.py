n, m = map(int, input().split())
# 9, 27
for i in range(0, int((n-1)/2)):
    mid = len('.|.' * (i * 2 + 1))
    topPattern = ('-' * int(m/2-mid/2) + '.|.' * (i*2 + 1) + '-' * int(m/2-mid/2))
    print(topPattern)

print( '-'*int((m/2-3.5)) + 'WELCOME' + '-'*int((m/2-3.5)))

for j in range(0, int((n-1)/2)):
    sides = (3*j + 3)*2
    downPattern = ('-' * int(3*j + 3) + '.|.' * int((m-sides)/3)  + ('-' * int(3*j +3)))
    print(downPattern)

"""
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

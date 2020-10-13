b = [list(map(int,input().split())) for _ in range(2)]
c = [list(map(int,input().split())) for _ in range(3)]
from itertools import combinations
A = [i for i in range(9)]
ans = []
res = 0
ch = 0
na = 0
for v in combinations(A, 4):
    v = list(v)
    tmp = [0]*9
    for i in v:
        tmp[i] += 1
    chokudai = 0
    naoko = 0
    for i in range(9):
        if i<6:
            if tmp[i]==tmp[i+3]:
                chokudai += b[i//3][i%3]
            else:
                naoko += b[i//3][i%3]
        if i != 2 and i !=5 and i != 8:
            if tmp[i]==tmp[i+1]:
                chokudai += c[i//3][i%3]
            else:
                naoko += c[i//3][i%3]
        if chokudai-naoko > res:
            ch = chokudai
            na = naoko
    # ans.append((abs(chokudai-naoko),chokudai,naoko))
    # ans.sort()
    # if ans[0][0]<res:
    #     ch = ans[0][1]
    #     na = ans[0][2]
print(ch)
print(na)
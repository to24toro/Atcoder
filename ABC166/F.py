N,A,B,C = map(int,input().split())
import collections
dic = collections.defaultdict(int)
d = {'A':A,'B':B,'C':C}
c = {'A':max(A,B,C),'B':A+B+C-max(A,B,C)-min(A,B,C),'C':min(A,B,C)}
e = {'A':max(A,B,C),'B':A+B+C-max(A,B,C)-min(A,B,C),'C':min(A,B,C)}
for _ in range(N):
    s = input()
    if d[s[0]] == c['A']:
        dic['A'] += 1
        a = 'A'
    elif d[s[0]] == c['B']:
        dic['B'] += 1
        a = 'B'
    else:
        dic['C'] += 1
        a = 'C'
    if d[s[1]] == c['A']:
        dic['A'] += 1
        b = 'A'
    elif d[s[1]] == c['B']:
        dic['B'] += 1
        b= 'B'
    else:
        dic['C'] += 1
        b ='C'
    dic[a+b] += 1
ans = []
for _ in range(dic['A']):
    ans.append('A')
c['A']-=dic['A']
c['B']+=dic['AB']
c['C']+=dic['AC']
if c['B']-dic['B']>=0:
    
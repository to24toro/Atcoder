s = input()
t = input()
set_ = set()
for i in s:
    set_.add(i)
for i in t:
    if i not in set_:print(-1);exit()
dic = [[0]*26 for _ in range(len(s))]
tmp = [[] for _ in range(26)]
for i in range(len(s)):
    tmp[ord(s[i])-ord('a')].append(i)
import bisect
for i in range(len(s)):
    for nxt in set_:
        idx = bisect.bisect_right(tmp[ord(nxt)-ord('a')],i)

        if idx==len(tmp[ord(nxt)-ord('a')]):
            dic[i][ord(nxt)-ord('a')] = tmp[ord(nxt)-ord('a')][0] + len(s)-i
            # idx = tmp[ord(nxt)-ord('a')][0]+len(s)
        else:
            dic[i][ord(nxt)-ord('a')] = tmp[ord(nxt)-ord('a')][idx]-i
cnt = tmp[ord(t[0])-ord('a')][0]
for i in range(1,len(t)):
    cnt += dic[cnt%len(s)][ord(t[i])-ord('a')]
print(cnt+1)




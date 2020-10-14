set_ = set()
s = input()
k = int(input())
if k >len(s):print(0);exit()
cnt = 0
for i in range(len(s)-k+1):
    if s[i:i+k] not in set_:
        cnt += 1
        set_.add(s[i:i+k])
print(cnt)
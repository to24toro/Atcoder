s = input()
ans = [0]*6
for i in s:
    ans[int(ord(i)-ord('A'))]+=1
print(' '.join(map(str,ans)))
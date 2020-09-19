n = int(input())
cnt = 0
m = [1]*n
m[0] = 0
ans = 0
for i in range(2,n):
    tmp = i
    for j in range(i,n,i):
        m[j]+=1

for i in range(n):
    if m[i]%2==1:
        ans += 2*(m[i]//2)+1
    else:
        ans += m[i]
print(ans)
# ans = 0
# for i in range(1,n):
#     m = [0]*n
#     cnt = 1
#     res = 1
#     while i!=1:
#         tmp = spf[i]
#         m[spf[i]] += 1
#         i//= spf[i]
#         if spf[i]!=tmp:
#             res*=(cnt+1)
#         else:
#             cnt += 1
#     if res%2==1:
#         ans += 2*(res//2)+1
#     else:
#         ans += res



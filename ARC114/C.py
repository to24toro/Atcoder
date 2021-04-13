n,m = map(int,input().split())
mod = 998244353
ans = 0
# def helper(a):
#     A = [1]*(n+1)
#     for i in range(n):
#         A[i+1] = A[i]*a%mod
#     return A
# power = []

# for i in range(m+1):
#     power.append(helper(i))
# # print(power)
# #極大長方形の形でとく
# for h in range(1,m+1):
#     for size in range(1,n+1):
#         x = power[m-h+1][size]-power[m-h][size]
#         if size==n:
#             y = 1
#         else:
#             y = 0
#             y += (h-1)*power[m][n-size-1]%mod
#             y += (h-1)*power[m][n-size-1]%mod
#             if size<=n-2:
#                 z = (h-1)**2*power[m][n-size-2]%mod
#                 y += z*(n-1-size)%mod
#         ans += x*y%mod
# print(ans%mod)

def helper(a):
    A = [1]*(n+1)
    for i in range(n):
        A[i+1] = A[i]*a%mod
    return A
power = []
for i in range(m+1):
    power.append(helper(i))   

for h in range(1,m+1):
    for size in range(1,n+1):
        x = power[m-h+1][size]-power[m-h][size]
        if size==n:
            y = 1
        else:
            y = 0
            y += (h-1)*power[m][n-size-1]%mod
            y += (h-1)*power[m][n-size-1]%mod
            if size<=n-2:
                z = (h-1)**2*power[m][n-size-2]%mod
                y += z*(n-1-size)%mod
        ans += x*y%mod
print(ans%mod)

N = int(input())
A = list(map(int,input().split()))
# def helper(A):
#     v = min(A)
#     ans = set()
#     for a in A:
#         if a%v!=0:
#             ans.add(a%v)
#     ans.add(v)
#     return ans

# while len(A)>1:
#     A = helper(A)
# print(min(A))
def gcd(x,y):
    if y==0: return x
    return gcd(y,x%y)
ans = A[0]
for a in A:
    ans = gcd(ans,a)
print(ans)
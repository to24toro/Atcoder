n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
j =0
bf = -1
for i in range(n):
    if bf!=a[i]:j = 0
    if a[i]==b[i]:
        for k in range(j,n):
            if a[k]!=a[i] and b[k]!=a[i]:
                b[i],b[k] = b[k],b[i]
                break
        j = k
        if a[i]==b[i]:
            print('No');exit()
    bf = a[i]
print('Yes')
print(*b)
# ca = [0]*(n+1)
# cb = [0]*(n+1)
# for a,b in zip(A,B):
#     ca[a]+=1
#     cb[b]+=1
# idx =0
# cnt = 0
# for i in range(n+1):
#     if ca[i]>0 and cb[i]>0:
#         if ca[i]+cb[i]>cnt:
#             idx = i
#             cnt = ca[i]+cb[i]
# sa = 0
# sb = 0
# ea = 0
# eb = 0
# for i in range(n):
#     if A[i]==idx:
#         sa = i
#         break
# for i in range(n):    
#     if A[i]>idx:
#         ea = i
#         break

# for i in range(n):
#     if B[i]==idx:
#         sb = i
#         break
# for i in range(n):
#     if B[i]>idx:
#         eb = i
#         break
# C = [0]*n
# f =True
# for i in range(n):
#     C[(n+i+ea-sb)%n]=B[i]
# # print(C,sa,sb,ea,eb,idx)
# D = [0]*n
# for i in range(n):
#     D[(n+i+sa-eb)%n]=B[i]
# for i in range(n):
#     if A[i]==C[i]:
#         f= False
# if f:
#     print('Yes')
#     print(*C)
# else:
#     for i in range(n):
#         if A[i]==D[i]:
#             print('No');exit()
#     print('Yes')
#     print(*D)

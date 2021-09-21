n = int(input())
if n==0:
    print('Yes');exit()
while n%10==0:
    n//=10
l = len(str(n))
if l==1:
    print('Yes');exit()
n = str(n)
a = n[:l//2]
b = n[l//2+l%2:]
# print(a,b)
if a==b[::-1]:
    print('Yes')
else:
    print('No')
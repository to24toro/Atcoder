n = int(input())
if n==0:
    print('Yes');exit()
while n%10==0:
    n //=10
n = str(n)
l = len(n)
if l==1:print('Yes');exit()
a = n[:l//2]
if l%2:
    b = n[l//2+1:]
else:
    b = n[l//2:]
b = b[::-1]
if a==b:
    print('Yes')
else:
    print('No')

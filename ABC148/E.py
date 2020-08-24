n = int(input())
if n%2:print(0);exit()
two = 0
five = 0
val = 2
while val<=n:
    two+=n//val
    val *= 2
val = 5
while val<=n:
    five +=(n//val)//2
    val *=5
print(min(two,five))
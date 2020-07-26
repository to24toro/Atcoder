n = int(input())
A = list(map(int,input().split()))
stock =0
money = 1000
for i in range(n-1):
    if A[i]<A[i+1]:
        stock += money//A[i]
        money -= (money//A[i])*A[i]
        #買う
    elif A[i]>A[i+1]:
        money += stock*A[i]
        stock =0
        #うる
    else:
        continue
if stock >0:
    money += stock*A[-1]
print(money)

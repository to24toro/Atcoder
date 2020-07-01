N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if N==1: print(A[0] + B[0]);exit()
AS = [0]
BS = [0]
for i in range(N):
    AS.append(AS[-1]+A[i])
    BS.append(BS[-1]+B[i])
ans = 0
for i in range(N):
    val = AS[i+1]
    val += BS[-1]-BS[i]
    ans =max(ans,val)
print(ans)
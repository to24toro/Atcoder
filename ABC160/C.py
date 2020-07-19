k,n = map(int,input().split())
A = list(map(int,input().split()))
A = [0] +A+[k+A[0]]
diff = []
for i in range(1,len(A)):
    diff.append(A[i]-A[i-1])
print(k-max(diff))
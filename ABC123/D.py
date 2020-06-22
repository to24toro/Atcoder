import heapq
X,Y,Z,K = map(int,input().split())
K = min(K,X*Y*Z)
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))


A.sort(reverse = True)
B.sort(reverse = True)
C.sort(reverse = True)
set_ = set()
hq = [(-(A[0]+B[0]+C[0]),0,0,0)]
heapq.heapify(hq)
set_.add((0,0,0))
while K:
    val,i,j,k = heapq.heappop(hq)
    print(-val)
    K-=1
    if i+1<len(A) and (i+1,j,k) not in set_: 
        heapq.heappush(hq,(-(A[i+1]+B[j]+C[k]),i+1,j,k))
        set_.add((i+1,j,k))
    if j+1<len(B) and (i,j+1,k) not in set_: 
        heapq.heappush(hq,(-(A[i]+B[j+1]+C[k]),i,j+1,k))
        set_.add((i,j+1,k))
    if k+1<len(C) and (i,j,k+1) not in set_: 
        heapq.heappush(hq,(-(A[i]+B[j]+C[k+1]),i,j,k+1))
        set_.add((i,j,k+1))

# sum2 = []
# for a in A:
#     for b in B:
#         sum2.append(a+b)
# sum2.sort(reverse = True)
# sum2 = sum2[:K]
# idx = 0
# sum3 = []
# for c in C:
#     for s in sum2:
#         sum3.append(c+s)
# sum3.sort(reverse=True)
# for i in range(K):
#     print(sum3[i])
n = int(input())

A = []
for _ in range(n):
    x,y = map(int,input().split())
    A.append((x,y))

B = []
for _ in range(n):
    x,y = map(int,input().split())
    B.append((x,y))

from math import sqrt
if n<=2:
    da = sqrt((A[0][0]-A[1][0])**2+(A[0][1]-A[1][1])**2) 
    db = sqrt((B[0][0]-B[1][0])**2+(B[0][1]-B[1][1])**2)
    print(db/da);exit()
def vec(A, B):
    return (B[0] - A[0] , B[1] - A[1])
def det(A, B):
    return A[0] * B[1] - A[1] * B[0]
def convexHull(node):
	node.sort()
	chSize = 0
	N = len(node)
	ch = []
	for i in range(N):
		while chSize > 1:
			v_cur = vec(ch[-2], ch[-1])
			v_new = vec(ch[-2] , node[i])
			if det(v_cur, v_new) > 0:
				break
			chSize -= 1
			ch.pop()
		ch.append(node[i])
		chSize += 1
 
	t = chSize
	for i in range(N - 2, -1, -1):
		while chSize > t:
			v_cur = vec(ch[-2], ch[-1])
			v_new = vec(ch[-2] , node[i])
			if det(v_cur, v_new) > 0:
				break
			chSize -= 1
			ch.pop()
		ch.append(node[i])
		chSize += 1
 
	return ch[:-1]
A = convexHull(A)
B = convexHull(B)


A.append(A[0])
B.append(B[0])
da = 0
db = 0
for i in range(len(A)-1):
    da += sqrt((A[i][0]-A[i+1][0])**2+(A[i][1]-A[i+1][1])**2) 
    db += sqrt((B[i][0]-B[i+1][0])**2+(B[i][1]-B[i+1][1])**2) 


print(db/da)
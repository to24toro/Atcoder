n, a = map(int,input().split())

k = int(input())
B =[0] + list(map(lambda x:int(x),input().split()))

seq = [None]*(2*n+10)#seqをよぶんに用意してseq[n]は必ずloopに入っていることを利用する

p = 0
for i in range(2*n+10):
    seq[i] = a
    if i>n and a==seq[n]:
        p = i-n
        break
    a = B[a]
if k<=n:
    print(seq[k])
else:
    print(seq[(k-n)%p+n])

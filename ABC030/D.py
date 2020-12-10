n,a=map(int,input().split())
a-=1
k = int(input())
B = list(map(lambda x:int(x)-1,input().split()))
set_=set()
li = []
dic = {}
index = 0
while True:
    if B[a] in set_:
        loop = li[dic[B[a]]:]
        k-=len(li)
        # print(dic[B[a]],B[a],li)
        k = k%len(loop)
        print(loop[k-1]+1);exit()
        break
    set_.add(B[a])
    li.append(B[a])
    dic[B[a]] = index
    index += 1
    if index==k:
        print(B[a]+1);exit()
    a = B[a]


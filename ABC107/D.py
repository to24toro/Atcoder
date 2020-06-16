n = int(input())
a = list(map(int,input().split()))
a2  =sorted(set(a))
L = len(a2)
if n==1: print(a[0]);exit()
elif n ==2: print(a[1]);exit()
l,r = 0,L
while r-l>1:
    mid = a2[(l+r)//2]
    count = 0
    idx = 0
    B = [0]*(2*n+1)
    B[0]+=1
    cur = 0
    for i in range(n):
        if a[i]>mid:
            idx += 1
            cur += B[idx]+1
        else:
            idx -=1
            cur-=B[idx]-1
        B[idx] += 1
        count +=cur
    if count >=((n + 1) * n // 2 + 1) // 2:
        l = (l+r)//2
    else:
        r = (l+r)//2
print(a2[l])
            
#中央値の集合のうちx以上はいくつか
#a[l,r]のうちx以上を[r-l+1/2]こ以上含むのはいくつか
#x未満なら-1x以上で1としてしてa[l,r]で総和が0以上のものは？
#累積和に変換
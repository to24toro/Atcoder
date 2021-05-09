n = int(input())
A = list(map(int,input().split()))
from itertools import accumulate
from bisect import bisect_left
S = list(accumulate(A))
ans = float('inf')
for i in range(1,n-1):
    T = S[i]
    U = S[-1]
    idt = bisect_left(S,T//2+1)
    # if idt ==0:
    #     a = S[0]
    #     b = S[i]-S[0]
    # else:
    #     if S[idt]-S[i]//2<S[i]//2-S[idt-1]:
    #         idt = idt
    #     else:
    #         idt-=1
    #     a = S[idt]
    #     b = S[i]-S[idt]
    X = [(S[idt],S[i]-S[idt]),(S[idt-1],S[i]-S[idt-1])]
    idu = bisect_left(S,S[i]+(S[-1]-S[i+1])//2+1)
    # print(idu)
    # if idu ==i+1:
    #     c = S[i+1]-S[i]
    #     d = S[-1]-S[i+1]
    # else:
    #     # print(T[-1]+(U[-1]-T[-1])//2)
    #     # print(S[i]+(S[-1]-S[i+1])//2,idu)
    #     if S[idu]-(S[i]+(S[-1]-S[i])//2)<(S[i]+(S[-1]-S[i])//2)-S[idu-1]:
    #         idu = idu
    #     else:
    #         idu-=1
    #     c = S[idu]-S[i]
    #     d = S[-1]-S[idu]
    Y = [(S[idu]-S[i],S[-1]-S[idu]),(S[idu-1]-S[i],S[-1]-S[idu-1])]
    # print(a,b,c,d,S[:i+1],S[i+1:],S[i])
    for i in range(2):
        for j in range(2):
            l = [X[i][0],X[i][1],Y[j][0],Y[j][1]]
            if 0 in l:
                continue
            ans = min(ans,max(l)-min(l))

print(ans)

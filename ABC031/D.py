def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

k,n = map(int,input().split())
A = []
dic = {}
for _ in range(n):
    v,w = map(str,input().split())
    A.append((v,w))
for bit in range(3**k):
    bit = Base_10_to_n(bit,3)
    bit = bit.zfill(k)
    f = True
    dic = {}
    for v,w in A:
        for i in v:
            if not w:
                f = False
                break
            l = int(bit[int(i)-1])
            if i not in dic:
                dic[i]=w[:l+1]
            else:
                if dic[i]!=w[:l+1]:
                    f = False
                    break
            w = w[l+1:]
        if w:
            f = False
        if not f:
            break
    if f:
        for i in range(k):
            print(dic[str(i+1)])
        exit()

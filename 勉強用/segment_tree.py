class Segment:
    e = float('inf') #eは単位元
    num = 2**(n-1).bit_length()
    seg = [e]*2*num
    def __init__(val):
        n = len(val)
        for i in range(n):
            seg[i+num-1] = val[i]
        for i in range(num-2,-1,-1):
            seg[i] = segfunc(seg[2*i+1],seg[2*i+2])
    
    def update(k,x):
        k += num-1
        seg[k] = x
        while k >0:
            k = (k-1)//2
            seg[k] = segfunc(seg[2*k+1],seg[2*k+2])
    def query(p,q):
        if q <=p: return e
        p += num-1
        q += num-2
        res = e
        while q-p>1:
            if p&1==0:
                res = segfunc(res,seg[p])
            if q&1==1:
                res = segfunc(res,seg[q])
            p //=2
            q = (q-1)//2
        if p ==q:
            res = segfunc(res,seg[p])
        else:
            res = segfunc(segfunc(res,seg[p]),seg[q])
        return res
    
    def segfunc(x,y):
        return

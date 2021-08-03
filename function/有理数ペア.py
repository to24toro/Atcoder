def make_pair(A: list):
    import math
    import collections
    dic = collections.defaultdict(int)
    for x,y in A:
        if x==0 and y==0:
            dic[(0,0)] += 1
        elif x==0:
            dic[(0,1)] += 1
        elif y==0:
            dic[(1,0)] += 1
        else:
            x,y = x//math.gcd(x,y),y//math.gcd(x,y)
            if x*y<0:
                x,y = abs(x),-abs(y)
            else:
                x,y = abs(x),abs(y)
            dic[(x,y)] += 1
    return dic


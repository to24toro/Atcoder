h,w = map(int,input().split())
ans = float('inf')
for i in range(1,h):
    sa = i*w
    sb = (h-i)*int(w//2)
    sc = (h-i)*(w-int(w//2))
    sd = (h-i-int((h-i)//2))*w
    se = (int((h-i)//2))*w
    s_max1 = max(sa,sb,sc)
    s_min1 = min(sa,sb,sc)
    s_max2 = max(sa,sd,se)
    s_min2 = min(sa,sd,se)
    ans = min(ans,s_max1-s_min1,s_max2-s_min2)
for i in range(1,w):
    sa = i*h
    sb = (w-i)*int(h//2)
    sc = (w-i)*(h-int(h//2))
    sd = (w-i-int((w-i)//2))*h
    se = (int((w-i)//2))*h
    s_max1 = max(sa,sb,sc)
    s_min1 = min(sa,sb,sc)
    s_max2 = max(sa,sd,se)
    s_min2 = min(sa,sd,se)
    ans = min(ans,s_max1-s_min1,s_max2-s_min2)
print(ans)

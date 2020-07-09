a,b,c,d = map(int,input().split())
from math import ceil

print('Yes' if ceil(c/b)<=ceil(a/d) else 'No')
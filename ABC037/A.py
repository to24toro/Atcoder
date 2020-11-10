a,b,c = map(int,input().split())
a,b = min(a,b),max(a,b)
print(c//a+(c%a)//b)
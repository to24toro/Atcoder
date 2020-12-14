a,b,c,d,e,f = map(int,input().split())
c-=a
e-=a
d-=b
f-=b
print(abs(e*d-f*c)/2)
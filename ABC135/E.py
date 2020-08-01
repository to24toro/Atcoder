k = int(input())
x,y = map(int,input().split())
x,sx = abs(x), -1 if x<0 else 1
y,sy = abs(y), -1 if y<0 else 1
ans = [(x,y)]
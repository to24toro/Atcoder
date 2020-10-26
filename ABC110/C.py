s = input()
t = input()
ds = [0]*26
dt = [0]*26
for i in s:
    ds[ord(i)-ord('a')]+=1
for i in t:
    dt[ord(i)-ord('a')]+=1

ds.sort()
dt.sort()
if all(S==T for S,T in zip(ds,dt)):
    print('Yes')
else:
    print('No')
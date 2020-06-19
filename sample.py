import bisect
a = [1,2,3]
idx = bisect.bisect_left(a,4)
print(idx)
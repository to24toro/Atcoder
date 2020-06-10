N,M = map(int,input().split())
intervals = []
for _ in range(M):
    a,b = map(int,input().split())
    intervals.append([a,b])
intervals.sort()
ans = [intervals[0]]
for i in range(len(intervals)):
    if ans[-1][1]>intervals[i][0]:
        if ans[-1][1]>intervals[i][1]:
            ans[-1][1]=intervals[i][1]
        ans[-1][0] = intervals[i][0]
    else:
        ans.append(intervals[i])
print(len(ans))
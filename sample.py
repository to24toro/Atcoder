import collections
videos = [(9,14),(18,30),(0,10),(8,17),(13,25),(5,19)]
videos = [(0,15),(0,10),(14,25),(24,25)]
videos = [(0,1),(1,3)]
def get_minimum_videos(videos):
    videos.sort(key = lambda x:(x[0],-x[1]))
    index = 1
    ans = []
    ans.append(videos[0])
    while index<len(videos):
        tmp = ans[-1][1]
        j = index
        while index < len(videos) and videos[index][0]<=ans[-1][1]:
            if tmp<videos[index][1]:
                tmp = videos[index][1]
                j = index
            index += 1
        ans.append(videos[j])
        index += 1
    return ans
# print(get_minimum_videos(videos))
# print(1|1)
import itertools
from math import factorial
from collections import Counter
S = input()
arr = [str(i) for i in S]#入力文字をlistに変換


def factorial_arr(arr,s):#並び順から重複を覗くための関数
    count = Counter(arr)
    ans = 1
    for key,val in count.items():
        if key ==s:
            val-=1
        ans *= factorial(val)
    return ans

def helper(arr,idx,S,res):
    if idx >=len(S):
        return res
    count = Counter(arr)
    arr.sort()
    all_comb = factorial(len(arr)-1)
    set_ = set()
    #以下でidx番目の文字より前のパターンを全カウント
    for a in arr:
        if a in set_:
            continue
        if a==S[idx]:
            break
        else:
            set_.add(a)
            part_comb = factorial_arr(arr,a)
            res += all_comb//part_comb
    arr.remove(S[idx])
    return helper(arr,idx+1,S,res)

res = helper(arr,0,S,0)
print(res+1)
# def helper(n,length):
#     ans = []
#     cnt = 1
#     while cnt <=length:
#         n,res = n//cnt, n%cnt
#         cnt += 1
#         ans.append(res)
#     return ans[::-1]
# def remove(s,i):
#     return s[:i] + s[i+1:]
# print(factorial_arr(arr))
# ans = helper(2*factorial_arr(arr),4)
# ans = helper((681322104395516-1)*factorial_arr(arr)+1,20)
# ans = helper(factorial_arr(arr),3)
# ans = helper(0,3)
#(n-1)*factorial_arr(arr)
# for i in range(24):
#     ans = helper(i,4)
#     print(ans)
#     res = ''
#     tmp = s
#     for a in ans:
#         res += tmp[a]
#         tmp = remove(tmp,a)
#     print(res)
# res = ''
# for a in ans:
#     res += s[a]
#     s = remove(s,a)
# print(res)



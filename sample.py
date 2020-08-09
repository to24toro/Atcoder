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
print(get_minimum_videos(videos))
print((3>>2)&1)
n = int(input())
def dfs(s):
    if len(s)==n:
        print(s)
    else:
        dfs(s+'a')
        dfs(s+'b')
        dfs(s+'c')
dfs('')

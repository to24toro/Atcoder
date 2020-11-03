s = input()
p = 'WBWBWWBWBWBW'
piano = p + p + p + p
ind = piano.find(s)
ans = ['Do','Do#','Re','Re#','Mi','Fa','Fa#','So','So#','La','La#','Si']
print(ans[ind])
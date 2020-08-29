s  = input()
a = -1
b = -1
if s[0]==s[1] and len(s)>2:print('1 3');exit()
for i in range(2,len(s)):
    if s[i]==s[i-1]:
        print(str(i-1)+ ' '+ str(i+1))
        exit()
for i in range(2,len(s)):
    if s[i]==s[i-2]:
        print(str(i-1) + ' ' + str(i+1))
        exit()

print('-1 -1')
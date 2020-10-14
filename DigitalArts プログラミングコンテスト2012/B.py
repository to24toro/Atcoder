s = input()
if len(set(s)) != 1:
    print(s[1:]+s[0])
elif s == 'a' or s == 'z'*20:
    print('NO')
elif s[0] == 'a':
    print('b'+s[2:])
elif s[0] == 'z':
    print('ay'+s[1:])
elif len(s) == 1:
    print('a'+chr(ord(s)-1))
else:
    print(chr(ord(s[0])+1)+chr(ord(s[1])-1)+s[2:])
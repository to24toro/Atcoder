s = input()
if int(s[:2])>12 or s[:2]=='00':
    if int(s[2:])>12 or s[2:]=='00':
        print('NA')
    else:
        print('YYMM')
else:
    if int(s[2:])>12 or s[2:]=='00':
        print('MMYY')
    else:
        print('AMBIGUOUS')
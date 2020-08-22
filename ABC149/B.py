a,b,k = map(int,input().split())
if a>=k:
    print(str(a-k) + ' '+ str(b))
elif k-a<=b:
    print('0 ' + str(b-k+a))
else:
    print('0 0')
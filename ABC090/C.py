N,M  =map(int,input().split())

if N==1 and M==1: print(1);exit()
if N==1 and M==2: print(0);exit()
if N==2 and M==1: print(0);exit()
if N==1: print(M-2);exit()
if M==1:print(N-2);exit()
if N==2 or M==2:print(0);exit()
else: print((N-2)*(M-2))
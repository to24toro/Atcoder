import numpy as np
s=input()
t=input()
n=len(s)
m=len(t)
s1=np.array(list(map(int,s)))
s2=1-s1
t1=np.array(list(map(int,reversed(t))))
t2=1-t1
def conv(f,g):
  size=len(f)+len(g)-1
  size=1<<(size-1).bit_length()
  f=np.fft.rfft(f,size)
  g=np.fft.rfft(g,size)
  f*=g
  f=np.fft.irfft(f,size)
  return np.rint(f).astype(np.int32)
A=conv(s1,t2)+conv(s2,t1)
print(np.min(A[m-1:n]))
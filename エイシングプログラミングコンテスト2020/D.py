n = int(input())
x = input()
original_pop_count = x.count('1')
one_pop_count = original_pop_count-1
zero_pop_count = original_pop_count+1

one_mod = 0
zero_mod= 0
for b in x:
    if one_pop_count!=0:
        one_mod=(one_mod*2+int(b))%one_pop_count
    zero_mod=(zero_mod*2+int(b))%zero_pop_count
#予めf[i]を計算する
f = [0]*220000
pop_count = [0]*220000
for i in range(1,220000):
    pop_count[i]= pop_count[i//2] + i%2
    f[i] = f[i%pop_count[i]]+1
one_pow2 = [1]*220000
zero_pow2 = [1]*220000
for i in range(1,220000):
    if one_pop_count!=0:
        one_pow2[i] = one_pow2[i-1]*2%one_pop_count
    zero_pow2[i] = zero_pow2[i-1]*2%zero_pop_count


for i in range(n-1,-1,-1):
    if x[n-1-i]=='1':
        if one_pop_count!=0:
            nxt = one_mod
            nxt-=one_pow2[i]
            nxt%=one_pop_count
            print(f[nxt]+1)
        else:
            print(0)
    if x[n-1-i]=='0':
        nxt = zero_mod
        nxt+=zero_pow2[i]
        nxt%=zero_pop_count
        print(f[nxt]+1)
from internal_math import inv_gcd

def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0, m0 = 0, 1  # 初期値 x = 0 (mod 1)
    for i in range(n):
        assert m[i] >= 1

        #r1, m1は遷移に使う値
        r1, m1 = r[i] % m[i], m[i]

        #m0がm１以上になるようにする。
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0

        # m0がm1の倍数のとき gcdはm1、lcmはm0
        # 解が存在すれば何も変わらないので以降の手順はスキップ
        if m0 % m1 == 0:
            if r0 % m1 != r1: return [0, 0]
            continue

        #  拡張ユークリッドの互除法によりgcd(m0, m1)と m0 * im = gcd (mod m1) を満たす imを求める
        g, im = inv_gcd(m0, m1)

        # 解の存在条件の確認
        if (r1 - r0) % g: return [0, 0]

        """
        r0, m0の遷移
        コメントアウト部分はACLでの実装
        C++なのでlong longを超えないようにしている
        C++ はlcm(m0, m1)で割った余りが負になり得る
        """
        # u1 = m1 // g
        # x = (r1 - r0) // g % u1 * im % u1
        # r0 += x * m0
        u1 = m0 * m1 // g
        r0 += (r1 - r0) // g * m0 * im % u1
        m0 = u1
        #if r0 < 0: r0 += m0

    return [r0, m0]



r = [3, 4]
m = [5, 7]
print(crt(r, m))  # [18, 35]

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
def CRT(a,b,X,Y):#a=0(mod x),b=0(mod y)
    if y==1:
      return X
    g,c,d=extgcd(X,Y)
    if (b-a)%g!=0:
        return -1
    else:
        return a+X*(b-a)*c//g%(X*Y//g)


def ext_gcd(a,b):
    if b==0:
        return (1,0,a)
    x,y,g = ext_gcd(b,a%b)
    return (y,x-(a//b)*y,g)
def inv_gcd(a,b):
    x,y,g = ext_gcd(a,b)
    return (g,x%b)
# returns (x % lcm(M), lcm(M)),  (x = R[i] (mod M[i]))
def crt(R,M):
    N = len(R)
    r0 = 0
    m0 = 1
    for i in range(N):
        r1 = R[i]%M[i]
        m1 = M[i]
        if m0<m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0%m1 !=r1:
                return (0,0)
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g != 0:
            return (0, 0) # x nai
        x = ((((r1 - r0) // g) % u1) * im) % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return (r0, m0)
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func Scan() string {
	sc.Scan()
	return sc.Text()
}

func rScan() []rune {
	return []rune(Scan())
}

func iScan() int {
	n, _ := strconv.Atoi(Scan())
	return n
}

func fScan() float64 {
	n, _ := strconv.ParseFloat(Scan(), 64)
	return n
}

func SScan(n int) []string {
	a := make([]string, n)
	for i := 0; i < n; i++ {
		a[i] = Scan()
	}
	return a
}

func iSScan(n int) []int {
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = iScan()
	}
	return a
}

func mod(x, d int) int {
	x %= d
	if x < 0 {
		x += d
	}
	return x
}

func max(a ...int) int {
	x := -P3
	for i := 0; i < len(a); i++ {
		if x < a[i] {
			x = a[i]
		}
	}
	return x
}

func min(a ...int) int {
	x := P3
	for i := 0; i < len(a); i++ {
		if x > a[i] {
			x = a[i]
		}
	}
	return x
}

func sum(a []int) int {
	x := 0
	for _, v := range a {
		x += v
	}
	return x
}

func fsum(a []float64) float64 {
	var x float64 = 0
	for _, v := range a {
		x += v
	}
	return x
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func modinv(a, m int) int {
	b, u, v := m, 1, 0
	for {
		t := a / b
		a -= t * b
		u -= t * v
		a, b, u, v = b, a, v, u
		if b == 0 {
			break
		}
	}
	u %= m
	if u < 0 {
		u += m
	}
	return u
}

func bPrint(f bool, x string, y string) {
	if f {
		fmt.Println(x)
	} else {
		fmt.Println(y)
	}
}

func iSSPrint(x []int) {
	fmt.Println(strings.Trim(fmt.Sprint(x), "[]"))
}

func sorted(x []int, r bool) []int {
	y := make([]int, len(x))
	copy(y, x)
	if r {
		sort.Sort(sort.Reverse(sort.IntSlice(y)))
		return y
	}
	sort.Ints(y)
	return y
}

func initSlice(n, x int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = x
	}
	return ret
}

func last(a []int) int {
	if len(a) == 0 {
		return 0
	}
	return a[len(a)-1]
}

func factorial(n, m int) ([]int, []int) {
	f := make([]int, n+1)
	inv := make([]int, n+1)
	f[0] = 1
	inv[0] = 1
	for i := 1; i < n; i++ {
		f[i] = f[i-1] * i % m
		inv[i] = modinv(f[i], m)
	}
	return f, inv
}

var P1 int = 1000000007
var P2 int = 998244353
var P3 int = 1<<61 - 1
var BINF int = 1 << 60

func main() {
	buf := make([]byte, 0)
	sc.Buffer(buf, P1)
	sc.Split(bufio.ScanWords)
	n := iScan()
	k := iScan()
	a := iSScan(n)
	as := make([]int, n+1)
	for i := 0; i < n; i++ {
		as[i+1] = a[i] + as[i]
	}
	x := make([]int, 0, n*(n+1)/2)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n+1; j++ {
			x = append(x, as[j]-as[i])
		}
	}

	ans := 0
	for i := 42; i >= 0; i-- {
		y := make([]int, 0, len(x))
		for j := 0; j < len(x); j++ {
			if (x[j]>>i)&1 == 1 {
				y = append(y, x[j])
			}
		}
		if len(y) >= k {
			ans += 1 << uint(i)
			x = make([]int, len(y))
			copy(x, y)
		}
	}
	fmt.Println(ans)
}

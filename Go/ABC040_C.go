package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	initialBufSize = 10000
	maxBufSize     = 100000000
)

var sc *bufio.Scanner = func() *bufio.Scanner {
	sc := bufio.NewScanner(os.Stdin)
	buf := make([]byte, initialBufSize)
	sc.Buffer(buf, maxBufSize)
	sc.Split(bufio.ScanWords)
	return sc
}()

func scanString() string { sc.Scan(); return sc.Text() }
func scanInt() int       { n, _ := strconv.Atoi(scanString()); return n }

func scanInts(n int) []int {
	ns := make([]int, n)
	for i := 0; i < n; i++ {
		ns[i] = scanInt()
	}
	return ns
}

func abs(x int) int {
	if x < 0 {
		x = -x
	}
	return x
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	N := scanInt()
	a := scanInts(N)
	dp := make([]int, N)
	dp[0] = 0
	dp[1] = abs(a[0] - a[1])

	for i := 2; i < N; i++ {
		dp[i] = minInt(dp[i-2]+abs(a[i-2]-a[i]), dp[i-1]+abs(a[i-1]-a[i]))
	}
	fmt.Println(dp[N-1])
}

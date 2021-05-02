package main

import (
	"fmt"
	"math"
)

func main() {
	var N int
	var D, H float64
	fmt.Scan(&N, &D, &H)
	ans := 0.0
	s := 0.0
	for k := 0; k < N; k++ {
		var d, h float64
		fmt.Scan(&d, &h)
		tmp := (h - H) / (d - D)
		if tmp < H/D {
			s = h - tmp*d
			ans = math.Max(ans, s)
		}
	}
	fmt.Println(ans)
}

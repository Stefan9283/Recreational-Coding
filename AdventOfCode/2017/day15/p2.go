package main

func main() {

	// A := 65
	// B := 8921

	A := 783
	B := 325

	fA := 16807
	fB := 48271

	div := 2147483647

	total := 0

	for range 5_000_000 {
		A = (A * fA) % div
		for A&0b11 != 0 {
			A = (A * fA) % div
		}

		B = (B * fB) % div
		for B&0b111 != 0 {
			B = (B * fB) % div
		}

		r1 := A & 0b1111111111111111
		r2 := B & 0b1111111111111111
		if r1 == r2 {
			total++
		}
	}
	println(total)
}

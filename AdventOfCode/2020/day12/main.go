package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func intAbs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func part1() {
	file, _ := os.Open("in")
	scanner := bufio.NewScanner(file)

	x, y := 0, 0

	// E S W N
	// 0 1 2 3
	dir := 0

	for scanner.Scan() {
		line := scanner.Text()

		action := string(line[0])
		val, _ := strconv.Atoi(line[1:])

		if action == "N" {
			y += val
		}
		if action == "S" {
			y -= val
		}
		if action == "E" {
			x += val
		}
		if action == "W" {
			x -= val
		}
		if action == "F" {
			if dir == 0 { // E
				x += val
			}
			if dir == 1 { // S
				y -= val
			}
			if dir == 2 { // W
				x -= val
			}
			if dir == 3 { // N
				y += val
			}
		}
		if action == "L" {
			dir += 4 - val/90
			dir %= 4
		}
		if action == "R" {
			dir += val / 90
			dir %= 4
		}
		println(action, val, x, y)

	}

	println(intAbs(x) + intAbs(y))
}

func rotateDirection(xD int, yD int, degrees int) (int, int) {
	s := math.Sin(math.Pi * float64(degrees) / 180)
	c := math.Cos(math.Pi * float64(degrees) / 180)

	x0 := float64(xD)
	y0 := float64(yD)

	x := x0*c - y0*s
	y := x0*s + y0*c

	return int(math.Round(x)), int(math.Round(y))
}

func part2() {
	file, _ := os.Open("in")
	scanner := bufio.NewScanner(file)

	x, y := 0, 0
	wx, wy := 10, 1

	for scanner.Scan() {
		line := scanner.Text()

		action := string(line[0])
		val, _ := strconv.Atoi(line[1:])

		if action == "N" {
			wy += val
		} else if action == "S" {
			wy -= val
		} else if action == "E" {
			wx += val
		} else if action == "W" {
			wx -= val
		} else if action == "F" {
			x += val * wx
			y += val * wy
		} else if action == "L" {
			wx, wy = rotateDirection(wx, wy, val)
		} else if action == "R" {
			wx, wy = rotateDirection(wx, wy, -val)
		}
		fmt.Printf("%s %3d | @(%5d %5d) -> (%4d %4d)\n", action, val, x, y, wx, wy)
	}

	println(intAbs(x) + intAbs(y))
}

func main() {
	part2()
}

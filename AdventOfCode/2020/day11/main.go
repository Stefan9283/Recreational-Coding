package main

import (
	"bufio"
	"bytes"
	"os"
)

func areEqual(runes1 [][]int32, runes2 [][]int32) bool {
	for i := 0; i < len(runes1); i++ {
		for j := 0; j < len(runes1[i]); j++ {
			if runes1[i][j] != runes2[i][j] {
				return false
			}
		}
	}
	return true
}

func howManyNeighOccupied(i int32, j int32, map_ [][]int32) int32 {
	count := 0

	for i_ := max(i-1, 0); i_ <= min(i+1, int32(len(map_))-1); i_++ {
		for j_ := max(j-1, 0); j_ <= min(j+1, int32(len(map_[i]))-1); j_++ {
			if i_ == i && j_ == j {
				continue
			}
			if map_[i_][j_] == '#' {
				count++
			} else {
			}
		}
	}
	return int32(count)
}

func howManyNeighOccupied2(i int32, j int32, map_ [][]int32) int32 {
	count := int32(0)

	checker := func(map_ [][]int32, i int32, j int32, advance func(int32, int32) (int32, int32)) int32 {
		i_ := i
		j_ := j

		for {
			i_, j_ = advance(i_, j_)

			if i_ < 0 || j_ < 0 || i_ >= int32(len(map_)) || j_ >= int32(len(map_[i_])) {
				break
			}

			if map_[i_][j_] == 'L' {
				return 0
			}
			if map_[i_][j_] == '#' {
				return 1
			}
		}

		return 0
	}

	up := func(i int32, j int32) (int32, int32) {
		return i - 1, j
	}
	down := func(i int32, j int32) (int32, int32) {
		return i + 1, j
	}
	left := func(i int32, j int32) (int32, int32) {
		return i, j - 1
	}
	right := func(i int32, j int32) (int32, int32) {
		return i, j + 1
	}
	upLeft := func(i int32, j int32) (int32, int32) {
		return i - 1, j - 1
	}
	upRight := func(i int32, j int32) (int32, int32) {
		return i - 1, j + 1
	}
	downLeft := func(i int32, j int32) (int32, int32) {
		return i + 1, j - 1
	}
	downRight := func(i int32, j int32) (int32, int32) {
		return i + 1, j + 1
	}

	count += checker(map_, i, j, up)
	count += checker(map_, i, j, upRight)
	count += checker(map_, i, j, right)
	count += checker(map_, i, j, downRight)
	count += checker(map_, i, j, down)
	count += checker(map_, i, j, downLeft)
	count += checker(map_, i, j, left)
	count += checker(map_, i, j, upLeft)

	return count
}

// for debugging
func printMap(m [][]int32) {
	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			print(string(m[i][j]))
		}
		println()
	}
}

func occupiedCount(m [][]int32) int {
	count := 0
	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			if m[i][j] == '#' {
				count++
			}
		}
	}
	return count
}

func doIteration(init [][]int32, counter func(i int32, j int32, map_ [][]int32) int32, minToBecomeEmpty int32) [][]int32 {
	var map_ [][]int32

	for i := 0; i < len(init); i++ {
		var line []int32
		for j := 0; j < len(init[i]); j++ {
			if init[i][j] == '.' {
				line = append(line, '.')
				continue
			}
			count := counter(int32(i), int32(j), init)
			if init[i][j] == 'L' && count == 0 {
				line = append(line, '#')
			} else if init[i][j] == '#' && count >= minToBecomeEmpty {
				line = append(line, 'L')
			} else {
				line = append(line, init[i][j])
			}

		}
		map_ = append(map_, line)
	}

	return map_
}

func runPart(counter func(i int32, j int32, map_ [][]int32) int32, minToBecomeEmpty int32) {
	file, _ := os.Open("in")
	scanner := bufio.NewScanner(file)

	var map_ [][]rune
	for scanner.Scan() {
		line := scanner.Text()
		var line_ []int32
		for _, c := range line {
			line_ = append(line_, c)
		}
		map_ = append(map_, bytes.Runes([]byte(line)))
	}

	for i := 0; i >= 0; i++ {
		newMap := doIteration(map_, counter, minToBecomeEmpty)
		if areEqual(map_, newMap) {
			break
		}
		map_ = newMap
	}

	println(occupiedCount(map_))
}

func main() {
	runPart(howManyNeighOccupied, 4)
	runPart(howManyNeighOccupied2, 5)
}

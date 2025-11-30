package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
	"strings"
)

func part1() {
	file, _ := os.Open("in")
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	earliest, _ := strconv.Atoi(scanner.Text())

	var schedule []int
	scanner.Scan()

	for _, tok := range strings.Split(scanner.Text(), ",") {
		if tok != "x" {
			val, _ := strconv.Atoi(tok)
			schedule = append(schedule, val)
		}
	}

	minimum := math.MaxInt
	result := 0
	for _, val := range schedule {
		maybeNewMin := (earliest/val)*val + val
		if maybeNewMin < minimum {
			minimum = maybeNewMin
			result = (maybeNewMin - earliest) * val
		}
	}
	println(result)
}

func part2() { // too slow
	file, _ := os.Open("in")
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	_, _ = strconv.Atoi(scanner.Text())

	var schedule []int
	var timeOffset []int
	scanner.Scan()

	maxLeap := 0
	iMaxLeap := -1
	minLeap := math.MaxInt
	iMinLeap := -1

	offset := 0
	for _, tok := range strings.Split(scanner.Text(), ",") {
		if tok != "x" {
			val, _ := strconv.Atoi(tok)
			timeOffset = append(timeOffset, offset)

			if maxLeap < val {
				maxLeap = val
				iMaxLeap = len(schedule)
			}
			if minLeap > val {
				minLeap = val
				iMinLeap = len(schedule)
			}
			schedule = append(schedule, val)
		}
		offset++
	}

	for delay := (100000000000000 / maxLeap) * maxLeap; ; delay += maxLeap {
		ok := true
		for i, ID := range schedule {
			if (delay-(timeOffset[iMaxLeap]-timeOffset[i]))%ID != 0 {
				ok = false
				break
			}
		}
		if ok {
			println(delay - (timeOffset[iMaxLeap] - timeOffset[iMinLeap]))
			break
		}
	}
}

func lcm(nums []int) int {
	lcm := 1

	lastDiv := 2
	for {
		used := true
		allOne := true

		used = false
		for i, num := range nums {
			if num != 1 {
				allOne = false
			}
			if num%lastDiv == 0 {
				used = true
				nums[i] = num / lastDiv
			}

		}

		if used {
			lcm *= lastDiv
		} else {
			lastDiv++
		}

		if allOne {
			break
		}
	}

	return lcm
}

func part2_() {
	file, _ := os.Open("in")
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	_, _ = strconv.Atoi(scanner.Text())

}

func main() {
	part2_()
}

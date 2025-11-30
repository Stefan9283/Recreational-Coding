package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func solve(lastTurn int) {
	file, _ := os.Open("in")
	scanner := bufio.NewScanner(file)
	scanner.Scan()

	var nums []int

	for _, num := range strings.Split(scanner.Text(), ",") {
		val, _ := strconv.Atoi(num)
		nums = append(nums, val)
	}

	last := map[int]int{}

	for i := 0; i < len(nums)-1; i++ {
		last[nums[i]] = i + 1
	}

	lastVal := nums[len(nums)-1]
	for i := len(nums) + 1; i <= lastTurn; i++ {
		pos, ok := last[lastVal]

		if !ok {
			last[lastVal] = i - 1
			lastVal = 0
			//println(i, "-", 0)
		} else {
			say := i - 1 - pos
			//println(i, "+", say)
			last[lastVal] = i - 1
			lastVal = say
		}
	}
	println(lastVal)

}

func main() {
	solve(2020)
	solve(30000000)
}

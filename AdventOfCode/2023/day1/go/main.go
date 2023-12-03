package main

import (
	"io/ioutil"
	"strings"
)

func part1() {
	var input, err = ioutil.ReadFile("in")
	if err != nil {
		print("Error reading from file")
		return
	}

	var digits = map[string]int{
		"0": 0,
		"1": 1,
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
	}

	var lines = strings.Split(string(input), "\n")
	var sum = 0
	for _, line := range lines {
		var fst = -1
		var last = -1
		for i, _ := range line {
			for key, val := range digits {
				if strings.HasPrefix(line[i:], key) {
					if fst == -1 {
						fst = val
					}
					last = val
				}
			}
		}
		sum += last + fst*10
	}
	println(sum)
}

func part2() {
	var input, err = ioutil.ReadFile("in")
	if err != nil {
		print("Error reading from file")
		return
	}

	var digits = map[string]int{
		"zero":  0,
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
		"0":     0,
		"1":     1,
		"2":     2,
		"3":     3,
		"4":     4,
		"5":     5,
		"6":     6,
		"7":     7,
		"8":     8,
		"9":     9,
	}

	var lines = strings.Split(string(input), "\n")
	var sum = 0
	for _, line := range lines {
		var fst = -1
		var last = -1
		for i, _ := range line {
			//print(i, "-", c, " ")
			for key, val := range digits {
				//println(key, val)
				if strings.HasPrefix(line[i:], key) {
					if fst == -1 {
						fst = val
					}
					last = val
				}
			}
		}
		sum += last + fst*10
		//println(fst, last, line)
	}
	println(sum)
}

func main() {
	part1()
	part2()
}

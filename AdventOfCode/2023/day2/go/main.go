package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

func part1() {
	var content, err = ioutil.ReadFile("in")

	if err != nil {
		println(err)
		return
	}

	lines := strings.Split(string(content), "\n")

	var config = map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}

	sum := 0

	for _, line := range lines {
		game_id, err := strconv.Atoi(strings.Split(strings.Split(line, ": ")[0], " ")[1])

		if err != nil {
			println(err)
			return
		}

		ok := true
		for _, game_set := range strings.Split(strings.Split(line, ": ")[1], "; ") {
			var extracted = map[string]int{
				"red":   0,
				"green": 0,
				"blue":  0,
			}

			for _, pair := range strings.Split(game_set, ", ") {

				toks := strings.Split(pair, " ")

				count, err := strconv.Atoi(toks[0])

				if err != nil {
					println(err)
					return
				}

				color := toks[1]

				extracted[color] += count

			}

			for color, count := range config {
				if count < extracted[color] {
					ok = false
				}
			}
		}
		if ok == true {
			sum += game_id
		}
	}

	println(sum)
}

func part2() {
	var content, err = ioutil.ReadFile("in")

	if err != nil {
		println(err)
		return
	}

	lines := strings.Split(string(content), "\n")

	sum := 0

	for _, line := range lines {
		if err != nil {
			println(err)
			return
		}

		var min_per_color = map[string]int{
			"red":   0,
			"green": 0,
			"blue":  0,
		}

		for _, game_set := range strings.Split(strings.Split(line, ": ")[1], "; ") {
			var extracted = map[string]int{
				"red":   0,
				"green": 0,
				"blue":  0,
			}
			for _, pair := range strings.Split(game_set, ", ") {

				toks := strings.Split(pair, " ")

				count, err := strconv.Atoi(toks[0])

				if err != nil {
					println(err)
					return
				}

				color := toks[1]

				extracted[color] += count
			}

			for color, count := range extracted {
				min_per_color[color] = max(count, min_per_color[color])
			}
		}

		sum += min_per_color["red"] *
			min_per_color["green"] *
			min_per_color["blue"]
	}

	println(sum)
}

func main() {
	part1()
	part2()
}

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"reflect"
	"strconv"
	"strings"
)

func doIter(move string, programs *[]rune) {
	switch move[0] {
	case 's':
		//spin sX
		x, _ := strconv.Atoi(move[1:])
		a := (*programs)[len(*programs)-x:]
		b := (*programs)[:len(*programs)-x]
		(*programs) = append(a, b...)

	case 'x':
		//exchange x/y
		pos := strings.Split(move[1:], "/")
		x, _ := strconv.Atoi(pos[0])
		y, _ := strconv.Atoi(pos[1])
		(*programs)[x], (*programs)[y] = (*programs)[y], (*programs)[x]

	case 'p':
		//partner a/b
		idxA, idxB := -1, -1
		a := rune(move[1])
		b := rune(move[3])
		for i, p := range *programs {
			if p == a {
				idxA = i
			} else if p == b {
				idxB = i
			}
		}
		if idxA != -1 && idxB != -1 {
			(*programs)[idxA], (*programs)[idxB] = (*programs)[idxB], (*programs)[idxA]
		}
	}
}

func processMovesUntilCycle(danceMoves string) (int, []string) {
	programs := []rune("abcdefghijklmnop")
	initial := []rune("abcdefghijklmnop")
	moves := strings.Split(danceMoves, ",")
	iters := 0

	// answer := []rune("fbidepghmjklcnoa")

	steps := []string{}

	steps = append(steps, string(initial))

	for {
		// println(iters, string(programs))
		for _, move := range moves {
			doIter(move, &programs)
			// fmt.Println(string(programs))
		}
		steps = append(steps, string(programs))
		// if reflect.DeepEqual(programs, answer) {
		// fmt.Println("found at", iters)
		// }
		iters++
		if reflect.DeepEqual(programs, initial) {
			return iters, steps
		}
	}
}

func doNIters(danceMoves string, N int) []rune {
	programs := []rune("abcdefghijklmnop")
	moves := strings.Split(danceMoves, ",")
	for _ = range N {
		for _, move := range moves {
			doIter(move, &programs)
		}
	}
	return programs
}

func main() {
	file, err := os.Open("input.in")
	if err != nil {
		log.Fatalf("failed to open")
	}

	scanner := bufio.NewScanner(file)
	var danceMoves string

	for scanner.Scan() {
		danceMoves = scanner.Text()
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	cycle_at, steps := processMovesUntilCycle(danceMoves)
	how_many_more := 1000000000 % cycle_at
	how_many_cycle := 1000000000 / cycle_at
	fmt.Println(cycle_at, how_many_cycle, how_many_more)

	// final := doNIters(danceMoves, how_many_more)

	// for i := range steps {
	// 	fmt.Println(i, string(steps[i]))
	// }

	final := steps[how_many_more]
	fmt.Println(string(final))

	file.Close()
}

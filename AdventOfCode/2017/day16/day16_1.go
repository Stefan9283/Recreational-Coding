package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func processMovesUntilCycle(danceMoves string) []rune {
	programs := []rune("abcdefghijklmnop")
	moves := strings.Split(danceMoves, ",")

	for _, move := range moves {
		switch move[0] {
		case 's':
			//spin sX
			x, _ := strconv.Atoi(move[1:])
			a := programs[len(programs)-x:]
			b := programs[:len(programs)-x]
			a1 := string(a)
			b1 := string(b)
			fmt.Println("Spin a: ", a1, " b: ", b1)
			programs = append(a, b...)

		case 'x':
			//exchange x/y
			pos := strings.Split(move[1:], "/")
			x, _ := strconv.Atoi(pos[0])
			y, _ := strconv.Atoi(pos[1])
			programs[x], programs[y] = programs[y], programs[x]

		case 'p':
			//partner a/b
			idxA, idxB := -1, -1
			a := rune(move[1])
			b := rune(move[3])
			for i, p := range programs {
				if p == a {
					idxA = i
				} else if p == b {
					idxB = i
				}

			}
			if idxA != -1 && idxB != -1 {
				programs[idxA], programs[idxB] = programs[idxB], programs[idxA]
			}

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
	// scanner.Split(bufio.ScanLines)
	var danceMoves string

	for scanner.Scan() {
		danceMoves = scanner.Text()

	}

	fmt.Println(danceMoves)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	programs := processMovesUntilCycle(danceMoves)
	fmt.Println(string(programs))

	file.Close()

}

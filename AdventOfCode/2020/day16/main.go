package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	fst int
	snd int
}

func (r Range) contains(num int) bool {
	return r.fst <= num && num <= r.snd
}

func (r Range) String() string {
	return fmt.Sprintf("(%d %d)", r.fst, r.snd)
}

func removeFromArray(s string, l []string) []string {
	for i := len(l) - 1; i >= 0; i-- {
		if l[i] == s {
			l = append(l[:i], l[i+1:]...)
		}
	}
	return l
}

func main() {
	f, _ := os.Open("in")
	scanner := bufio.NewScanner(f)

	fields := map[string][]Range{}
	tickets := [][]int{}

	for { // read props ranges
		scanner.Scan()
		line := scanner.Text()
		if line == "" {
			break
		}
		tok := strings.Split(line, ": ")
		fieldName := tok[0]

		for _, rng := range strings.Split(tok[1], " or ") {
			tok := strings.Split(rng, "-")
			fst, _ := strconv.Atoi(tok[0])
			snd, _ := strconv.Atoi(tok[1])
			//println(fieldName, fst, snd)
			fields[fieldName] = append(fields[fieldName], Range{
				fst, snd,
			})
		}

	}

	// skip my ticket
	myTicket := []int{}
	scanner.Scan()
	scanner.Scan()
	for _, tok := range strings.Split(scanner.Text(), ",") {
		val, _ := strconv.Atoi(tok)
		myTicket = append(myTicket, val)
	}
	scanner.Scan()
	scanner.Scan()

	// nearby tickets

	result := 0
	for scanner.Scan() {
		ticket := []int{}
		nums := strings.Split(scanner.Text(), ",")
		validTicket := true
		for _, num_ := range nums {
			num, _ := strconv.Atoi(num_)
			ticket = append(ticket, num)

			valid := false
			for fieldName := range fields {
				for _, rng := range fields[fieldName] {
					if rng.contains(num) {
						valid = true
						goto fieldCheckDone
					}
				}
			}

		fieldCheckDone:
			if !valid {
				result += num
			}
			validTicket = validTicket && valid
		}

		if validTicket {
			tickets = append(tickets, ticket)
		}
	}
	println(result) // part1

	potentialFields := [][]string{}

	for _ = range tickets[0] {
		potentialFields = append(potentialFields, []string{})
	}

	for i := range tickets[0] {
		for name, rngs := range fields {
			goodRange := true
			for _, t := range tickets {
				ok := false
				for _, rng := range rngs {
					ok = ok || rng.contains(t[i])
				}
				goodRange = goodRange && ok
			}
			if goodRange {
				potentialFields[i] = append(potentialFields[i], name)
			}
		}
	}

	for _ = range potentialFields {
		for i, field := range potentialFields {
			if len(field) == 1 {
				for j := range potentialFields {
					if i == j {
						continue
					}
					if len(potentialFields) != 1 {
						potentialFields[j] = removeFromArray(field[0], potentialFields[j])
					}
				}
			}
		}
	}
	result = 1
	for i, rng := range potentialFields {
		if strings.Contains(rng[0], "departure") {
			result *= myTicket[i]
		}
	}
	println(result) // part 2

}

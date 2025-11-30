package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

// part1

func emptyArray(n int) []bool {
	var a []bool
	for i := 0; i < n; i++ {
		a = append(a, false)
	}
	return a
}

func extend3D(m [][][]bool) [][][]bool {
	var newM [][][]bool

	//fmt.Println("extend3D", len(m), len(m[0]), len(m[0][0]))
	var emptyLayer [][]bool
	for i := 0; i < len(m[0])+2; i++ {
		emptyLayer = append(emptyLayer, []bool{})
		for j := 0; j < len(m[0][0])+2; j++ {
			emptyLayer[len(emptyLayer)-1] = append(emptyLayer[len(emptyLayer)-1], false)
		}
	}

	newM = append(newM, emptyLayer)

	for _, layer := range m {
		var newLayer [][]bool

		newLayer = append(newLayer, emptyArray(len(emptyLayer[0])))

		for _, line := range layer {
			newLine := []bool{}
			newLine = append(newLine, false)
			for _, val := range line {
				newLine = append(newLine, val)
			}
			newLine = append(newLine, false)
			newLayer = append(newLayer, newLine)
		}

		newLayer = append(newLayer, emptyArray(len(emptyLayer[0])))

		newM = append(newM, newLayer)
	}

	newM = append(newM, emptyLayer)

	return newM
}

func countActiveNeighbours3D(i int, j int, k int, m [][][]bool) int {
	count := 0

	//fmt.Println("checking", i, j, k, "in", m)

	for i_ := max(i-1, 0); i_ <= min(i+1, len(m)-1); i_++ {
		for j_ := max(j-1, 0); j_ <= min(j+1, len(m[i])-1); j_++ {
			for k_ := max(k-1, 0); k_ <= min(k+1, len(m[i][j])-1); k_++ {
				if i_ == i && j_ == j && k_ == k {
					continue
				}
				//fmt.Println(i_, j_, k_)
				if m[i_][j_][k_] {
					count++
				}
			}
		}
	}
	//fmt.Println(count)
	return count
}

func countActive3D(m [][][]bool) int {
	count := 0

	//fmt.Println("checking", i, j, k, "in", m)

	for i_ := 0; i_ <= len(m)-1; i_++ {
		for j_ := 0; j_ <= len(m[i_])-1; j_++ {
			for k_ := 0; k_ <= len(m[i_][j_])-1; k_++ {
				if m[i_][j_][k_] {
					count++
				}
			}
		}
	}
	//fmt.Println(count)
	return count
}

func doCycle3D(m [][][]bool) [][][]bool {
	m_ := [][][]bool{}
	for i := range m {
		m_ = append(m_, [][]bool{})
		for j := range m[i] {
			m_[i] = append(m_[i], []bool{})
			for _ = range m[i][j] {
				m_[i][j] = append(m_[i][j], false)
			}
		}
	}

	for i := range m {
		for j := range m[i] {
			for k := range m[i][j] {
				active := countActiveNeighbours3D(i, j, k, m)

				fmt.Println(i, j, k, active)

				m_[i][j][k] = false
				if m[i][j][k] {
					if active == 2 || active == 3 {
						m_[i][j][k] = true
					}
				} else {
					if active == 3 {
						m_[i][j][k] = true
					}
				}
			}
		}
	}
	return m_
	//return extend3D(m_)
}

func part1() {

	var m [][][]bool

	f, _ := os.Open("in")
	scanner := bufio.NewScanner(f)

	{
		var layer [][]bool
		for scanner.Scan() {
			layer = append(layer, []bool{})
			line := scanner.Text()
			for _, c := range line {
				if c == '#' {
					layer[len(layer)-1] = append(layer[len(layer)-1], true)
				} else {
					layer[len(layer)-1] = append(layer[len(layer)-1], false)
				}
			}
		}
		m = append(m, layer)
	}

	for i := 0; i < 6; i++ {
		m = extend3D(m)
		m = doCycle3D(m)

		j, _ := json.MarshalIndent(m, "", "   ")
		fmt.Println(
			strings.Replace(
				strings.Replace(
					strings.Replace(
						strings.Replace(
							strings.Replace(
								strings.Replace(string(j),
									"false", ".", -1),
								"true", "#", -1,
							),
							"[\n         ", "[", -1,
						),
						"\n      ]", "]", -1,
					),
					"\n         ", " ", -1),
				", ", "", -1,
			),
		)
		//fmt.Println(m)
		println(countActive3D(m))
	}

}

// part2

func extend4D(m [][][][]bool) [][][][]bool {
	var newM [][][][]bool

	//fmt.Println("extend3D", len(m), len(m[0]), len(m[0][0]))
	var emptyLayer [][][]bool
	for i := 0; i < len(m[0])+2; i++ {
		emptyLayer = append(emptyLayer, [][]bool{})
		for j := 0; j < len(m[0][0])+2; j++ {
			emptyLayer[i] = append(emptyLayer[i], []bool{})
			for k := 0; k < len(m[0][0][0])+2; k++ {
				emptyLayer[i][j] = append(emptyLayer[i][j], false)
			}
		}
	}

	newM = append(newM, emptyLayer)

	for _, layer := range m {
		newM = append(newM, extend3D(layer))
	}

	newM = append(newM, emptyLayer)

	return newM
}

func countActiveNeighbours4D(i int, j int, k int, l int, m [][][][]bool) int {
	count := 0

	//fmt.Println("checking", i, j, k, "in", m)

	for i_ := max(i-1, 0); i_ <= min(i+1, len(m)-1); i_++ {
		for j_ := max(j-1, 0); j_ <= min(j+1, len(m[i])-1); j_++ {
			for k_ := max(k-1, 0); k_ <= min(k+1, len(m[i][j])-1); k_++ {
				for l_ := max(l-1, 0); l_ <= min(l+1, len(m[i][j][k])-1); l_++ {
					if i_ == i && j_ == j && k_ == k && l_ == l {
						continue
					}
					//fmt.Println(i_, j_, k_)
					if m[i_][j_][k_][l_] {
						count++
					}
				}
			}
		}
	}
	//fmt.Println(count)
	return count
}

func countActive4D(m [][][][]bool) int {
	count := 0

	//fmt.Println("checking", i, j, k, "in", m)

	for i_ := 0; i_ <= len(m)-1; i_++ {
		for j_ := 0; j_ <= len(m[i_])-1; j_++ {
			for k_ := 0; k_ <= len(m[i_][j_])-1; k_++ {
				for l_ := 0; l_ <= len(m[i_][j_][k_])-1; l_++ {
					if m[i_][j_][k_][l_] {
						count++
					}
				}
			}
		}
	}
	//fmt.Println(count)
	return count
}

func doCycle4D(m [][][][]bool) [][][][]bool {
	m_ := [][][][]bool{}
	for i := range m {
		m_ = append(m_, [][][]bool{})
		for j := range m[i] {
			m_[i] = append(m_[i], [][]bool{})
			for k := range m[i][j] {
				m_[i][j] = append(m_[i][j], []bool{})
				for _ = range m[i][j][k] {
					m_[i][j][k] = append(m_[i][j][k], false)
				}
			}
		}
	}

	for i := range m {
		for j := range m[i] {
			for k := range m[i][j] {
				for l := range m[i][j][k] {
					active := countActiveNeighbours4D(i, j, k, l, m)

					fmt.Println(i, j, k, active)

					m_[i][j][k][l] = false
					if m[i][j][k][l] {
						if active == 2 || active == 3 {
							m_[i][j][k][l] = true
						}
					} else {
						if active == 3 {
							m_[i][j][k][l] = true
						}
					}
				}
			}
		}
	}
	return m_
	//return extend3D(m_)
}

func part2() {

	var m [][][][]bool

	f, _ := os.Open("in")
	scanner := bufio.NewScanner(f)

	{
		var layer [][]bool
		for scanner.Scan() {
			layer = append(layer, []bool{})
			line := scanner.Text()
			for _, c := range line {
				if c == '#' {
					layer[len(layer)-1] = append(layer[len(layer)-1], true)
				} else {
					layer[len(layer)-1] = append(layer[len(layer)-1], false)
				}
			}
		}
		m = append(m, [][][]bool{})
		m[0] = append(m[0], layer)
	}

	for i := 0; i < 6; i++ {
		m = extend4D(m)
		m = doCycle4D(m)

		j, _ := json.MarshalIndent(m, "", "   ")
		fmt.Println(
			strings.Replace(
				strings.Replace(
					strings.Replace(
						strings.Replace(
							strings.Replace(
								strings.Replace(string(j),
									"false", ".", -1),
								"true", "#", -1,
							),
							"[\n         ", "[", -1,
						),
						"\n      ]", "]", -1,
					),
					"\n         ", " ", -1),
				", ", "", -1,
			),
		)
		//fmt.Println(m)
		println(countActive4D(m))
	}

}

func main() {
	//part1()
	part2()
}

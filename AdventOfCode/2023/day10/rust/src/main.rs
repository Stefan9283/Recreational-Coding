use std::{cell::RefCell, collections::HashMap, fs, rc::Rc, thread::current};

#[derive(Debug)]
struct Node {
    next: Vec<(usize, usize)>,
}

fn part1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    // println!("{content}");

    let lines = content
        .split("\n")
        .map(|x| x.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let mut nodes: HashMap<(usize, usize), Node> = HashMap::new();

    let mut start: (usize, usize) = (0, 0);

    for (i, line) in lines.iter().enumerate() {
        for (j, c) in line.iter().enumerate() {
            if *c != '.' {
                // print!("{c}");
                let mut node = Node { next: vec![] };
                if *c == '|' {
                    if i != 0 {
                        node.next.push((i - 1, j));
                    }
                    node.next.push((i + 1, j));
                } else if *c == '-' {
                    if j != 0 {
                        node.next.push((i, j - 1));
                    }
                    node.next.push((i, j + 1));
                } else if *c == '7' {
                    if j != 0 {
                        node.next.push((i, j - 1));
                    }
                    node.next.push((i + 1, j));
                } else if *c == 'J' {
                    if j != 0 {
                        node.next.push((i, j - 1));
                    }
                    if i != 0 {
                        node.next.push((i - 1, j));
                    }
                } else if *c == 'F' {
                    node.next.push((i, j + 1));
                    node.next.push((i + 1, j));
                } else if *c == 'L' {
                    node.next.push((i, j + 1));
                    if i != 0 {
                        node.next.push((i - 1, j));
                    }
                } else if *c == 'S' {
                    if j != line.len() - 1 {
                        let right = lines.get(i).unwrap().get(j + 1).unwrap();
                        if vec!['J', '-', '7'].contains(right) {
                            node.next.push((i, j + 1));
                        }
                    }

                    if j != 0 {
                        let left = lines.get(i).unwrap().get(j - 1).unwrap();
                        if vec!['-', 'F', 'L'].contains(left) {
                            node.next.push((i, j - 1));
                        }
                    }

                    if i != 0 {
                        let top = lines.get(i - 1).unwrap().get(j).unwrap();
                        if vec!['|', 'F', '7'].contains(top) {
                            node.next.push((i - 1, j));
                        }
                    }

                    if i != lines.len() - 1 {
                        let bottom = lines.get(i + 1).unwrap().get(j).unwrap();
                        if vec!['|', 'L', 'J'].contains(bottom) {
                            node.next.push((i + 1, j));
                        }
                    }
                    start = (i, j);
                }
                nodes.insert((i, j), node);
            } else {
                // print!(" ")
            }
        }
        // println!();
    }

    // println!("{:?}", start);
    // for n in &nodes {
    //     println!(" - {:?}", n);
    // }

    let mut current = start;
    let mut length = 0;
    let mut visited: Vec<(usize, usize)> = vec![];
    loop {
        visited.push(current);

        length += 1;

        let current_node = nodes.get(&current).unwrap();

        // println!("{:?}", current);

        let n1 = current_node.next.get(0).unwrap();
        let n2 = current_node.next.get(1).unwrap();

        if !visited.contains(&n1) {
            // println!("{:?} {:?}", n1, visited);
            current = n1.clone();
            continue;
        } else if !visited.contains(&n2) {
            // println!("{:?} {:?}", n2, visited);
            current = n2.clone();
            continue;
        }

        break;
    }

    // println!("{:?}", visited);
    println!("{:?}", length / 2);
}

fn explore(map: &mut Vec<Vec<char>>, i: i32, j: i32) {
    if i < 0 || j < 0 || i >= map.len() as i32 || j >= map[0].len() as i32 || map[i as usize][j as usize] != ' ' {
        return
    }
    
    map[i as usize][j as usize] = 'O'; 
    explore(map, i + 1, j);
    explore(map, i - 1, j);
    explore(map, i, j - 1);
    explore(map, i, j + 1);
}
fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    // println!("{content}");

    let lines = content
        .split("\n")
        .map(|x| x.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let mut nodes: HashMap<(usize, usize), Node> = HashMap::new();

    let mut start: (usize, usize) = (0, 0);

    for (i, line) in lines.iter().enumerate() {
        for (j, c) in line.iter().enumerate() {
            if *c != '.' {
                // print!("{c}");
                let mut node = Node { next: vec![] };
                if *c == '|' {
                    if i != 0 {
                        node.next.push((i - 1, j));
                    }
                    node.next.push((i + 1, j));
                } else if *c == '-' {
                    if j != 0 {
                        node.next.push((i, j - 1));
                    }
                    node.next.push((i, j + 1));
                } else if *c == '7' {
                    if j != 0 {
                        node.next.push((i, j - 1));
                    }
                    node.next.push((i + 1, j));
                } else if *c == 'J' {
                    if j != 0 {
                        node.next.push((i, j - 1));
                    }
                    if i != 0 {
                        node.next.push((i - 1, j));
                    }
                } else if *c == 'F' {
                    node.next.push((i, j + 1));
                    node.next.push((i + 1, j));
                } else if *c == 'L' {
                    node.next.push((i, j + 1));
                    if i != 0 {
                        node.next.push((i - 1, j));
                    }
                } else if *c == 'S' {
                    if j != line.len() - 1 {
                        let right = lines.get(i).unwrap().get(j + 1).unwrap();
                        if vec!['J', '-', '7'].contains(right) {
                            node.next.push((i, j + 1));
                        }
                    }

                    if j != 0 {
                        let left = lines.get(i).unwrap().get(j - 1).unwrap();
                        if vec!['-', 'F', 'L'].contains(left) {
                            node.next.push((i, j - 1));
                        }
                    }

                    if i != 0 {
                        let top = lines.get(i - 1).unwrap().get(j).unwrap();
                        if vec!['|', 'F', '7'].contains(top) {
                            node.next.push((i - 1, j));
                        }
                    }

                    if i != lines.len() - 1 {
                        let bottom = lines.get(i + 1).unwrap().get(j).unwrap();
                        if vec!['|', 'L', 'J'].contains(bottom) {
                            node.next.push((i + 1, j));
                        }
                    }
                    start = (i, j);
                }
                nodes.insert((i, j), node);
            } else {
                // print!(" ")
            }
        }
        // println!();
    }

    // println!("{:?}", start);
    // for n in &nodes {
    //     println!(" - {:?}", n);
    // }

    let mut current = start;
    let mut visited: Vec<(usize, usize)> = vec![];
    loop {
        visited.push(current);

        let current_node = nodes.get(&current).unwrap();

        // println!("{:?}", current);

        let n1 = current_node.next.get(0).unwrap();
        let n2 = current_node.next.get(1).unwrap();

        if !visited.contains(&n1) {
            // println!("{:?} {:?}", n1, visited);
            current = n1.clone();
            continue;
        } else if !visited.contains(&n2) {
            // println!("{:?} {:?}", n2, visited);
            current = n2.clone();
            continue;
        }

        break;
    }

    let mut map: Vec<Vec<char>> = vec![];
    for _ in 0..lines.len() * 2 {
        let mut line = vec![];
        for _ in 0..lines.get(0).unwrap().len() * 2 {
            line.push(' '); // no pipe
        }
        map.push(line);
    }



    for e in &visited {
        map[e.0 * 2][e.1 * 2] = lines[e.0][e.1];
        match lines[e.0][e.1] {
            '-' => {
                map[e.0 * 2][e.1 * 2 - 1] = '*';
                map[e.0 * 2][e.1 * 2 + 1] = '*';
            },
            '|' => {
                map[e.0 * 2 - 1][e.1 * 2] = '*';
                map[e.0 * 2 + 1][e.1 * 2] = '*';
            },
            '7' => {
                map[e.0 * 2 + 1][e.1 * 2] = '*';
                map[e.0 * 2][e.1 * 2 - 1] = '*';
            },
            'F' => {
                map[e.0 * 2 + 1][e.1 * 2] = '*';
                map[e.0 * 2][e.1 * 2 + 1] = '*';
            },
            'J' => {
                map[e.0 * 2 - 1][e.1 * 2] = '*';
                map[e.0 * 2][e.1 * 2 - 1] = '*';
            },
            'L' => {
                map[e.0 * 2 - 1][e.1 * 2] = '*';
                map[e.0 * 2][e.1 * 2 + 1] = '*';
            },
            _ => {

            }
        }
    }





   
    for i in 0..lines.len() * 2 {
        explore(&mut map, i as i32, 0 as i32);
        explore(&mut map, i as i32, (lines[0].len() * 2 - 1) as i32);
    }

    for j in 0..lines[0].len() * 2 {
        explore(&mut map, 0 as i32, j as i32);
        explore(&mut map, (lines.len() * 2 - 1) as i32, j as i32);
    }


    for line in &map {
        print!("[");
        for c in line {
            print!("{}", c);
        }
        println!("]");
    }


    println!();

    let mut answer = 0;
    for (i, line) in map.iter().enumerate() {
        // println!("{:?}", line);
        if i % 2 == 1 {
            continue;
        }
        print!("[");
        for (j, e) in line.iter().enumerate() {
            if j % 2 == 1 {
                continue;
            }
            
            if *e == ' ' {
                answer += 1;
            }

            print!("{}", e);
        }
        println!("]");
    }

    println!("{answer}");



}


fn main() {
    // part1();
    part2();
}

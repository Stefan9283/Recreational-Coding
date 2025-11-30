use std::{borrow::BorrowMut, collections::HashMap, fs};

enum Direction {
    NORTH,
    WEST,
    SOUTH,
    EAST,
}

fn shift_north(map: &mut Vec<Vec<char>>) {
    loop {
        let mut changed = false;
        for i in (0..map.len() - 1).rev() {
            for j in 0..map[i].len() {
                let c = map[i + 1][j];
                let c1 = map[i][j];
                if c == 'O' && c1 == '.' {
                    changed = true;
                    map[i + 1][j] = '.';
                    map[i][j] = 'O';
                }
            }
        }
        if !changed {
            break;
        }
    }
}

fn shift_south(map: &mut Vec<Vec<char>>) {
    loop {
        let mut changed = false;
        for i in (1..map.len()).rev() {
            for j in 0..map[i].len() {
                let c = map[i][j];
                let c1 = map[i - 1][j];
                if c == '.' && c1 == 'O' {
                    changed = true;
                    map[i][j] = 'O';
                    map[i - 1][j] = '.';
                }
            }
        }
        if !changed {
            break;
        }
    }
}

fn shift_west(map: &mut Vec<Vec<char>>) {
    loop {
        let mut changed = false;
        for i in 0..map.len() {
            for j in 0..map[i].len() - 1 {
                let c = map[i][j];
                let c2 = map[i][j + 1];
                if c == '.' && c2 == 'O' {
                    changed = true;
                    map[i][j] = 'O';
                    map[i][j + 1] = '.';
                }
            }
        }
        if !changed {
            break;
        }
    }
}

fn shift_east(map: &mut Vec<Vec<char>>) {
    loop {
        let mut changed = false;
        for i in 0..map.len() {
            for j in (1..map[i].len()).rev() {
                let c = map[i][j - 1];
                let c2 = map[i][j];
                if c == 'O' && c2 == '.' {
                    changed = true;
                    map[i][j] = 'O';
                    map[i][j - 1] = '.';
                }
            }
        }
        if !changed {
            break;
        }
    }
}

fn shift(map: &mut Vec<Vec<char>>, direction: Direction) {
    match direction {
        Direction::NORTH => {
            shift_north(map);
        }
        Direction::WEST => {
            shift_west(map);
        }
        Direction::SOUTH => {
            shift_south(map);
        }
        Direction::EAST => {
            shift_east(map);
        }
    }
}

fn compute_strain(map: &Vec<Vec<char>>) -> u32 {
    let mut res: u32 = 0;
    for (i, line) in map.iter().enumerate() {
        for c in line {
            if *c == 'O' {
                res += (map.len() - 1 - i) as u32 + 1;
            }
        }
    }
    res
}

fn part1(file: &str) {
    let content = fs::read_to_string(file).expect("Should be able to read the input from file");
    let mut lines = content
        .split("\n")
        .map(|x| x.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    shift_north(lines.borrow_mut());

    let res = compute_strain(&lines);
    println!("{res}")
}

fn part2(file: &str) {
    let content = fs::read_to_string(file).expect("Should be able to read the input from file");
    let mut lines = content
        .split("\n")
        .map(|x| x.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let mut s: HashMap<Vec<Vec<char>>, i64> = HashMap::new();

    for i in 1..1000000000 {
        if s.contains_key(&lines) {
            let current = s.get(&lines).unwrap();
            let cycle_len = s.len() as i64 + 1 - current;
            let more_cycles = (1000000000 - i) / cycle_len * cycle_len;
            let checkpoint = more_cycles + i;
            for _ in checkpoint..1000000001 {
                shift(lines.borrow_mut(), Direction::NORTH);
                shift(lines.borrow_mut(), Direction::WEST);
                shift(lines.borrow_mut(), Direction::SOUTH);
                shift(lines.borrow_mut(), Direction::EAST);
            }

            break;
        }

        let prev = lines.clone();

        shift(lines.borrow_mut(), Direction::NORTH);
        shift(lines.borrow_mut(), Direction::WEST);
        shift(lines.borrow_mut(), Direction::SOUTH);
        shift(lines.borrow_mut(), Direction::EAST);

        s.insert(prev.clone(), i);
    }

    let res = compute_strain(&lines);
    println!("{res}")
}

fn main() {
    part1("in");
    part2("in");
}

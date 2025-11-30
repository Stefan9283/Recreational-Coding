use std::collections::{HashMap, VecDeque, HashSet};
use std::fs;
use std::str::FromStr;

#[derive(Debug, Hash, PartialEq, Eq, Clone, Copy)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

#[derive(Debug)]
struct Matrix2D<T> {
    v: Vec<Vec<T>>,
}

fn main() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content
        .split("\n")
        .map(|x| x.chars().map(|i| i.to_digit(10).unwrap()).collect())
        .collect::<Vec<Vec<u32>>>();

    let mut stack = VecDeque::new();
    stack.push_back((Direction::Left, 1, (0, 0), 0));
    let mut visited: HashSet<(Direction, i32, (i32, i32), u32)> = HashSet::new();

    let mut min = u32::MAX;

    while !stack.is_empty() {
        let (dir, dir_count, pos, mut loss) = stack.pop_back().unwrap();
        
        if visited.contains(&(dir, dir_count, pos, loss)) {
            continue;
        }

        if loss > min {
            continue;
        }

        if pos == (lines.len() as i32 - 1, lines[0].len() as i32 - 1) {
            println!("{}", min);
            min = min.min(loss);
        }

        visited.insert((dir, dir_count, pos, loss));
        loss += lines[pos.0 as usize][pos.1 as usize];
        let neigh = get_neighbours(&dir, &pos, (lines.len() as i32, lines[0].len() as i32));
        // println!("{:?} {:?}", (dir, dir_count, pos, loss), neigh);
        for dir_ in neigh.keys() {
            let mut count = 0;
            if dir == *dir_ {
                count = dir_count + 1;
            }
            if count > 3 {
                continue;
            }
            stack.push_back((*dir_, count, *neigh.get(dir_).unwrap(), loss))
        }
    }

    println!("{min}");

    // for line in lines {
    //     println!("{:?}", line);
    // }
}

fn get_neighbours(
    dir: &Direction,
    pos: &(i32, i32),
    max: (i32, i32),
) -> HashMap<Direction, (i32, i32)> {
    let mut neigh = HashMap::new();

    if !matches!(dir, Direction::Up) && pos.0 != 0 {
        neigh.insert(Direction::Up, (pos.0 - 1, pos.1));
    }
    if !matches!(dir, Direction::Down) && pos.0 != max.0 - 1 {
        neigh.insert(Direction::Down, (pos.0 + 1, pos.1));
    }
    if !matches!(dir, Direction::Left) && pos.1 != 0 {
        neigh.insert(Direction::Left, (pos.0, pos.1 - 1));
    }
    if !matches!(dir, Direction::Right) && pos.1 != max.1 - 1 {
        neigh.insert(Direction::Right, (pos.0, pos.1 + 1));
    }
    return neigh;
}

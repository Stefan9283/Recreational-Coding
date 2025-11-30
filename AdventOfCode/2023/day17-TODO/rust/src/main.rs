use std::collections::{HashMap, VecDeque, HashSet, BinaryHeap};
use std::fs;

#[derive(Debug, Hash, PartialEq, Eq, Clone, Copy)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn main() {
    let content = fs::read_to_string("in0").expect("Should be able to read the input from file");
    let lines = content
        .split("\n")
        .map(|x| x.chars().map(|i| i.to_digit(10).unwrap()).collect())
        .collect::<Vec<Vec<u32>>>();

    let mut min_loss = u32::MAX;

    let mut stack = VecDeque::new();
    stack.push_back((0, Direction::Left, 1, HashSet::new(), (0, 0)));

    while !stack.is_empty() {

        // stack.make_contiguous().sort_by(|x1, x2| {
        //     x1.0.cmp(&x2.0)
        // });

        let (mut loss, dir, dir_count, visited, pos) = stack.pop_front().unwrap();

        if visited.contains(&pos) {
            continue
        }


        let mut new_visited = visited.clone();
        new_visited.insert(pos);

        // println!("{} {:?}", stack.len(), stack);
        // println!("{} {} {:?} {:?}", loss, visited.len(), pos, new_visited);

        if loss >= min_loss {
            continue;
        }

        if pos == (lines.len() as i32 - 1, lines[0].len() as i32 - 1) {
            println!("{}", min_loss);
            min_loss = min_loss.min(loss);
            continue
        }

        let neigh = get_neighbours(&pos, (lines.len() as i32, lines[0].len() as i32));
        // println!("{:?} {:?}", (dir, dir_count, pos, loss), neigh);
        for (dir_, pos_) in neigh {
            let mut count = 0;
            if dir == dir_ {
                count = dir_count + 1;
            }
            if count > 3 {
                continue;
            }

            let new_loss = loss + lines[pos_.0 as usize][pos_.1 as usize];

            stack.push_back((new_loss, dir_, count, new_visited.clone(), pos_));
        }
    }

    println!("{min_loss}");
}

fn get_neighbours(
    pos: &(i32, i32),
    max: (i32, i32),
) -> Vec<(Direction, (i32, i32))> {
    let mut neigh = Vec::new();

    if pos.0 != max.0 - 1 {
        neigh.push((Direction::Down, (pos.0 + 1, pos.1)));
    }

    if pos.1 != max.1 - 1 {
        neigh.push((Direction::Right, (pos.0, pos.1 + 1)));
    }

    if pos.0 != 0 {
        neigh.push((Direction::Up, (pos.0 - 1, pos.1)));
    }

    if pos.1 != 0 {
        neigh.push((Direction::Left, (pos.0, pos.1 - 1)));
    }

    return neigh;
}

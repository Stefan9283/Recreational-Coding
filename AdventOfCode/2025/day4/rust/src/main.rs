use std::{fs::File, io::{BufRead, BufReader}};


fn is_position_inside_grid(i: i32, j: i32, maxi: usize, maxj: usize) -> bool {
    if i < 0 { return false }
    if j < 0 { return false }
    if i >= maxi as i32 { return false }
    if j >= maxj as i32 { return false }
    return true
}


fn count_neighbours(i: usize, j :usize, map: &Vec<Vec<char>>) -> usize {
    let mut count: usize = 0;

    for offx in 0..3 {
        for offy in 0..3 {
            let i_ = i as i32 - 1 + offx;
            let j_ = j as i32 - 1 + offy;
            if is_position_inside_grid(i_, j_, map.len(), map[0].len()) {
                if offx == 1 && offy == 1 { continue; }
                if map[i_ as usize][j_ as usize] == '@' {
                    count += 1;
                }
            }
        }
    }

    return count;
}


fn part1() {
    let file = File::open("in").unwrap();
    let reader = BufReader::new(file);

    let mut map: Vec<Vec<char>> = vec![]; 

    for line in reader.lines() {
        let mut row: Vec<char> = Vec::new();
        for c in line.unwrap().chars() {
            row.push(c);
        }
        map.push(row);
    }

    let mut sum = 0;

    for i in 0..map.len() {
        for j in 0..map[0].len() {
            if map[i][j] != '@' {  continue; }

            let count = count_neighbours(i, j, &map);

            if count < 4 {
                sum += 1;
            }
        }
    }

    println!("Part 1 answer {sum}");
}




fn part2() {
    let file = File::open("in").unwrap();
    let reader = BufReader::new(file);

    let mut map: Vec<Vec<char>> = vec![]; 

    for line in reader.lines() {
        let mut row: Vec<char> = Vec::new();
        for c in line.unwrap().chars() {
            row.push(c);
        }
        map.push(row);
    }

    let mut sum = 0;

    loop {

        let mut removed = 0;

        for i in 0..map.len() {
            for j in 0..map[0].len() {
                if map[i][j] != '@' {  continue; }

                let count = count_neighbours(i, j, &map);

                if count < 4 {
                    sum += 1;
                    map[i][j] = '.';
                    removed += 1
                }
            }
        }

        if removed == 0 { 
            break;
        }
    }
    println!("Part 2 answer {sum}");
}



fn main() {
    part1();
    part2();
}

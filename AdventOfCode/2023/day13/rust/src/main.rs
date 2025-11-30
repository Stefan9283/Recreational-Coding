use std::fs;

fn mirror_test(map: &Vec<Vec<char>>, idx: usize) -> bool {
    let mut i = 0;

    loop {
        if idx < i || idx + i + 1 >= map.len() {
            break;
        }

        if map[idx - i] != map[idx + 1 + i] {
            return false;
        }

        i += 1;
    }

    return true;
}

fn part1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let matrices = content.split("\n\n").collect::<Vec<&str>>();
    let mut res = 0;
    for matrix in matrices {
        let lines = matrix
            .split("\n")
            .map(|s| s.chars().collect::<Vec<char>>())
            .collect::<Vec<Vec<char>>>();
        let mut lines_ortho: Vec<_> = vec![];

        println!("//////////////////////////////");
        for line in &lines {
            println!("{:?}", line)
        }

        for col in 0..lines[0].len() {
            lines_ortho.push(vec![]);
            for line in 0..lines.len() {
                lines_ortho[col].push(lines[line][col]);
            }
        }

        println!("");

        for col in &lines_ortho {
            println!("{:?}", col)
        }

        for line in 0..lines.len() - 1 {
            if mirror_test(&lines, line) {
                println!("line {:?}", line);
                res += (line + 1) * 100;
            }
        }

        for col in 0..lines_ortho.len() - 1 {
            if mirror_test(&lines_ortho, col) {
                println!("col {:?}", col);
                res += col + 1;
            }
        }
    }
    println!("{res}");
}










fn mirror_diff(map: &Vec<Vec<char>>, idx: usize) -> i32 {
    let mut i = 0;

    let mut diffs = 0;

    loop {
        if idx < i || idx + i + 1 >= map.len() {
            break;
        }

        for j in 0..map[0].len() {
            if map[idx - i][j] != map[idx + 1 + i][j] {
                diffs += 1;
            }
        }

        i += 1;
    }

    return diffs;
}

fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let matrices = content.split("\n\n").collect::<Vec<&str>>();
    let mut res = 0;
    for matrix in matrices {
        let lines = matrix
            .split("\n")
            .map(|s| s.chars().collect::<Vec<char>>())
            .collect::<Vec<Vec<char>>>();
        let mut lines_ortho: Vec<_> = vec![];

        println!("//////////////////////////////");
        for line in &lines {
            println!("{:?}", line)
        }

        for col in 0..lines[0].len() {
            lines_ortho.push(vec![]);
            for line in 0..lines.len() {
                lines_ortho[col].push(lines[line][col]);
            }
        }

        println!("");

        for col in &lines_ortho {
            println!("{:?}", col)
        }

        for line in 0..lines.len() - 1 {
            if mirror_diff(&lines, line) == 1 {
                println!("line {:?}", line);
                res += (line + 1) * 100;
            }
        }

        for col in 0..lines_ortho.len() - 1 {
            if mirror_diff(&lines_ortho, col) == 1 {
                println!("col {:?}", col);
                res += col + 1;
            }
        }
    }
    println!("{res}");
}





fn main() {
    part1();
    part2()
}
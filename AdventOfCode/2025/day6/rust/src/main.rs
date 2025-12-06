use std::{fs::{File, read}, io::{BufRead, BufReader}};


fn trim_whitespaces(s: String) -> String {
    let mut tmp = s;
    loop {
        if tmp.find("  ").is_none() {
            return tmp;
        }
        tmp = tmp.trim().replace("  ", " ");
    }
}

fn part1() {
    let file = File::open("in").expect("file should exist");
    let reader = BufReader::new(file);

    let lines: Vec<Vec<String>> = reader.lines().into_iter().map(|x| {
        return trim_whitespaces(x.unwrap()).split(" ").map(|y| { return y.to_string(); }).collect::<Vec<String>>();
    }).collect();

    let operators_line = &lines[lines.len() - 1];
    let operands_lines = &lines[..lines.len() - 1];

    let mut total: i128 = 0;
    for idx in 0..operators_line.len() {
        let op = &operators_line[idx];
        if op == "*" {
            let mut column_res: i128 = 1;
            operands_lines.iter().for_each(|x| {
                column_res *= x[idx].parse::<i128>().unwrap()
            });
            total += column_res;
        } else {
            let mut column_res: i128 = 0;
            operands_lines.iter().for_each(|x| {
                column_res += x[idx].parse::<i128>().unwrap()
            });
            total += column_res;
        }
    }

    println!("Part 1 answer: {total}")
}



fn parse_columns(lines: Vec<String>) -> Vec<Vec<i128>> {
    let operators_line = &lines[lines.len()-1];
    let operands_line = &lines[..lines.len()-1];

    // get spaces count between all operators
    let mut spaces: Vec<usize> = operators_line.split(|x| {
        return x == '*' || x == '+'
    }).map(|x| {
        return x.len();
    }).collect::<Vec<usize>>();
    spaces.remove(0);
    {
        // only for the last elem 
        let len = spaces.len();
        spaces[len - 1] += 1;
    }

    // println!("{:?}", operands_line);

    // split columns elems based on spaces between operators
    let mut current_start = 0;
    let mut matrix = vec![];
    for num_of_spaces in spaces {
        let mut column: Vec<String> = vec![];
        for line in operands_line {
            let elem = &line[current_start..current_start+num_of_spaces];
            column.push(elem.to_string());
        }

        current_start += num_of_spaces + 1;

        matrix.push(column);
    }

    // println!("{:?}", matrix);

    // transpose elements on a column
    let mut transposed_matrix: Vec<Vec<i128>> = vec![];
    for idx in 0..matrix.len() {
        let mut transposed_column = vec![];
        let column = &matrix[idx];
        for idx_in_column in 0..column[0].len() {
            let mut num = String::new();
            for idx_of_elem_in_column in 0..column.len() {
                let c: char = column[idx_of_elem_in_column].chars().nth(idx_in_column).unwrap();
                num += &c.to_string();
            }
            transposed_column.push(num.trim().parse::<i128>().unwrap());
        }
        transposed_matrix.push(transposed_column);
    }

    return transposed_matrix;
}

fn part2() {
    let file = File::open("in").expect("file should exist");
    let reader = BufReader::new(file);

    let lines: Vec<String> = reader.lines().into_iter().map(|x| {
        return x.unwrap()
    }).collect();

    let operators = lines[lines.len()-1].clone().chars().filter(|x| { return *x != ' '; }).collect::<Vec<char>>();
    let columns = parse_columns(lines);

    println!("{:?}", operators);
    println!("{:?}", columns);

    let mut total: i128 = 0;
    for (col_idx, op) in operators.iter().enumerate() {
        if *op == '*' {
            let mut column_res: i128 = 1;
            columns[col_idx].iter().for_each(|x| {
                column_res *= x;
            });
            total += column_res;
        } else {
            let mut column_res: i128 = 0;
            columns[col_idx].iter().for_each(|x| {
                column_res += x;
            });
            total += column_res;
        }
    }

    println!("Part 2 answer: {total}")
}

fn main() {
    // part1();
    part2();
}

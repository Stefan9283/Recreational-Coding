use std::collections::HashMap;
use std::str::FromStr;
use std::fs;

fn is_digit(ch: char) -> bool {
    vec!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'].contains(&ch)
}
fn is_symbol(ch: char) -> bool {
    if is_digit(ch) {
        return false;
    }
    return ch != '.';
}
fn has_symbol_nearby(
    line: usize,
    start: usize,
    end: usize,
    lines: &Vec<&str>,
) -> Option<(usize, usize)> {
    if line != 0 {
        for i in start..end + 1 {
            if is_symbol(lines[line - 1][i..].chars().next().unwrap()) {
                return Some((line - 1, i));
            }
        }
    }

    if line != lines.len() - 1 {
        for i in start..end + 1 {
            if is_symbol(lines[line + 1][i..].chars().next().unwrap()) {
                return Some((line + 1, i));
            }
        }
    }

    if start != 0 {
        if line != 0 {
            if is_symbol(lines[line - 1][start - 1..].chars().next().unwrap()) {
                return Some((line - 1, start - 1));
            }
        }

        if is_symbol(lines[line][start - 1..].chars().next().unwrap()) {
            return Some((line, start - 1));
        }

        if line != lines.len() - 1 {
            if is_symbol(lines[line + 1][start - 1..].chars().next().unwrap()) {
                return Some((line + 1, start - 1));
            }
        }
    }

    if end != lines[line].len() - 1 {
        if line != 0 {
            if is_symbol(lines[line - 1][end + 1..].chars().next().unwrap()) {
                return Some((line - 1, end + 1));
            }
        }

        if is_symbol(lines[line][end + 1..].chars().next().unwrap()) {
            return Some((line, end + 1));
        }

        if line != lines.len() - 1 {
            if is_symbol(lines[line + 1][end + 1..].chars().next().unwrap()) {
                return Some((line + 1, end + 1));
            }
        }
    }

    return None;
}

fn part1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let mut start_num: i32 = -1;
    let mut end_num: i32 = -1;
    let mut sum = 0;
    for (i, line) in lines.iter().enumerate() {
        for (j, ch) in line.chars().enumerate() {
            // println!("{i} {j} {ch}");
            if is_digit(ch) {
                if start_num == -1 {
                    start_num = j as i32;
                    end_num = j as i32;
                } else {
                    end_num = j as i32;
                }

                if j == line.len() - 1 {
                    if has_symbol_nearby(i, start_num as usize, end_num as usize, &lines).is_some() {
                        // print!(
                        //     "{i} {start_num}-{end_num} {} | ",
                        //     &line[start_num as usize..end_num as usize + 1]
                        // );
                        let num =
                            i32::from_str(&line[start_num as usize..end_num as usize + 1]).unwrap();
                        // println!("{num}");
                        sum += num;
                    }
                    start_num = -1;
                    end_num = -1;
                }
            } else {
                if start_num != -1 && end_num != -1 {
                    // println!("{}", line[start_num as usize..end_num as usize + 1]);
                    if has_symbol_nearby(i, start_num as usize, end_num as usize, &lines).is_some() {
                        // print!(
                        //     "{i} {start_num}-{end_num} {} | ",
                        //     &line[start_num as usize..end_num as usize + 1]
                        // );
                        let num =
                            i32::from_str(&line[start_num as usize..end_num as usize + 1]).unwrap();
                        // println!("{num}");
                        sum += num;
                    }
                    start_num = -1;
                    end_num = -1;
                }
            }
        }
    }
    println!("{sum}");
}

fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let mut start_num: i32 = -1;
    let mut end_num: i32 = -1;
    let mut gears: HashMap<(usize, usize), Vec<u32>> = HashMap::new();
    for (i, line) in lines.iter().enumerate() {
        for (j, ch) in line.chars().enumerate() {
            if is_digit(ch) {
                if start_num == -1 {
                    start_num = j as i32;
                    end_num = j as i32;
                } else {
                    end_num = j as i32;
                }

                if j == line.len() - 1 {
                    match has_symbol_nearby(i, start_num as usize, end_num as usize, &lines) {
                        Some((x, y)) => {
                            if lines.get(x).unwrap().chars().nth(y).unwrap() == '*' {
                                if !gears.contains_key(&(x, y)) {
                                    gears.insert((x, y), vec![]);
                                }
                                let num = u32::from_str(&line[start_num as usize..end_num as usize + 1]).unwrap();
                                gears.get_mut(&(x, y)).expect("").push(num);
                            }
                            
                        },
                        None => {}
                    }
                    start_num = -1;
                    end_num = -1;
                }
            } else {
                if start_num != -1 && end_num != -1 {
                    match has_symbol_nearby(i, start_num as usize, end_num as usize, &lines) {
                        Some((x, y)) => {
                            if lines.get(x).unwrap().chars().nth(y).unwrap() == '*' {
                                if !gears.contains_key(&(x, y)) {
                                    gears.insert((x, y), vec![]);
                                }
                                let num = u32::from_str(&line[start_num as usize..end_num as usize + 1]).unwrap();
                                gears.get_mut(&(x, y)).expect("").push(num);
                            }
                            
                        },
                        None => {}
                    }
                    start_num = -1;
                    end_num = -1;
                }
            }
        }
    }
    
    let mut sum = 0;
    for (_, v) in gears {
        if v.len() == 2 {
            sum += v[0] * v[1];
        }
    }
    println!("{sum}")
}

fn main() {
    part1();
    part2();
}

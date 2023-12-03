use std::collections::HashMap;
use std::fs;
use std::str::FromStr;

fn part1() {
    let contents = fs::read_to_string("in")
        .expect("Should have been able to read the file");

    let mut sum: i32 = 0;
    for line in contents.split("\n").collect::<Vec<_>>() {
        let mut fst = 0;
        let mut last = 0;
        for i in 0..line.len() {
            if vec!["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].contains(&line.get(i..i + 1).unwrap())  {
                fst = i32::from_str(line.get(i..i+1).unwrap()).unwrap();
                break;
            }
        }
        for i in (0..line.len()).rev() {
            if vec!["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].contains(&line.get(i..i + 1).unwrap())  {
                last = i32::from_str(line.get(i..i+1).unwrap()).unwrap();
                break;
            }
        }
        sum += fst * 10 + last;
    }
    println!("{}", sum)
}


fn part2() {
    let contents = fs::read_to_string("in")
        .expect("Should have been able to read the file");

    let mut digits_as_strings = HashMap::new();
    digits_as_strings.insert("zero", 0);
    digits_as_strings.insert("one", 1);
    digits_as_strings.insert("two", 2);
    digits_as_strings.insert("three", 3);
    digits_as_strings.insert("four", 4);
    digits_as_strings.insert("five", 5);
    digits_as_strings.insert("six", 6);
    digits_as_strings.insert("seven", 7);
    digits_as_strings.insert("eight", 8);
    digits_as_strings.insert("nine", 9);

    let digits = vec!["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    let mut sum: i32 = 0;
    for line in contents.split("\n").collect::<Vec<_>>() {
        let mut fst = 0;
        let mut last = 0;
        let mut pos_fst: i32 = (line.len() + 1) as i32;
        let mut pos_last: i32 = -1;

        for i in 0..line.len() {
            if digits.contains(&line.get(i..i + 1).unwrap())  {
                fst = i32::from_str(line.get(i..i+1).unwrap()).unwrap();
                pos_fst = i as i32;
                break;
            }
        }
        for i in (0..line.len()).rev() {
            if digits.contains(&line.get(i..i + 1).unwrap())  {
                last = i32::from_str(line.get(i..i+1).unwrap()).unwrap();
                pos_last = i as i32;
                break;
            }
        }

        for s in digits_as_strings.keys() {
            let fst_res = line.find(s);
            let lst_res = line.rfind(s);
            if !fst_res.is_none() {
                let idx = fst_res.unwrap() as i32;
                if idx < pos_fst {
                    pos_fst = idx;
                    fst = *digits_as_strings.get(s).unwrap();
                }
            }
            if !lst_res.is_none() {
                let idx = lst_res.unwrap() as i32;
                if idx > pos_last {
                    pos_last = idx;
                    last = *digits_as_strings.get(s).unwrap();
                }
            }
        }

        sum += fst * 10 + last;
    }
    println!("{}", sum)
}

fn main() {
    part1();
    part2();
}
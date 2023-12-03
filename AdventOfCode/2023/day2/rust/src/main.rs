use std::str::FromStr;
use std::{fs, borrow::BorrowMut};
use std::cmp::max;
use std::collections::HashMap;

fn part1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines: Vec<_> = content.split("\n").map(|x| {String::from(x)}).collect();

    let mut sum = 0;

    let mut config: HashMap<&str, i32> = HashMap::new();
    config.insert("red", 12);
    config.insert("green", 13);
    config.insert("blue", 14);

    for mut game in lines.into_iter().borrow_mut() {
        let [fst, last]: [&str; 2] = game.split(": ").collect::<Vec<&str>>().try_into().unwrap();

        let game_id = u32::from_str(fst.split(" ").collect::<Vec<_>>()[1]).unwrap();

        let mut ok = true;
        for set in last.split("; ") {
            let mut extracted_count: HashMap<&str, i32> = HashMap::new();
            extracted_count.insert("red", 0);
            extracted_count.insert("green", 0);
            extracted_count.insert("blue", 0);
            for extracted in set.split(", ") {
                let [count_s, color]: [&str; 2] = extracted.split(" ").collect::<Vec<&str>>().try_into().unwrap();
                let count = i32::from_str(count_s).unwrap();
                extracted_count.insert(color, extracted_count.get(color).unwrap() + count);
            }

            for color in ["red", "green", "blue"] {
                if extracted_count[color] > config[color] {
                    ok = false;
                    break;
                }
            }
        }
        if ok {
           sum += game_id
        }
    }
    println!("{sum}");
}

fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines: Vec<_> = content.split("\n").map(|x| {String::from(x)}).collect();

    let mut sum = 0;

    for mut game in lines.into_iter().borrow_mut() {
        let [fst, last]: [&str; 2] = game.split(": ").collect::<Vec<&str>>().try_into().unwrap();

        let mut min_set_count: HashMap<&str, i32> = HashMap::new();
        min_set_count.insert("red", 0);
        min_set_count.insert("green", 0);
        min_set_count.insert("blue", 0);

        for set in last.split("; ") {
            let mut extracted_count: HashMap<&str, i32> = HashMap::new();
            extracted_count.insert("red", 0);
            extracted_count.insert("green", 0);
            extracted_count.insert("blue", 0);
            for extracted in set.split(", ") {
                let [count_s, color]: [&str; 2] = extracted.split(" ").collect::<Vec<&str>>().try_into().unwrap();
                let count = i32::from_str(count_s).unwrap();
                extracted_count.insert(color, extracted_count.get(color).unwrap() + count);
            }

            for color in ["red", "green", "blue"] {
                min_set_count.insert(color,max(
                    *min_set_count.get(color).unwrap(),
                    *extracted_count.get(color).unwrap()
                ));
            }
        }
        sum += min_set_count["red"] * min_set_count["green"] * min_set_count["blue"];
    }

    println!("{sum}");
}

fn main() {
    part1();
    part2();
}

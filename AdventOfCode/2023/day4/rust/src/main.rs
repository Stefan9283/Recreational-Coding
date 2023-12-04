use std::fs;
use std::str::FromStr;
use std::cmp::min;

fn part1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let mut sum = 0;
    for line in lines {
        let card_and_rest = line.split(": ").collect::<Vec<&str>>();
        let won_and_selected = card_and_rest
            .get(1)
            .unwrap()
            .split(" | ")
            .collect::<Vec<&str>>();
        let won = won_and_selected
            .get(0)
            .unwrap()
            .split(" ")
            .filter(|x| x.to_string() != "")
            .map(|x| u32::from_str(x).unwrap())
            .collect::<Vec<u32>>();
        let selected = won_and_selected
            .get(1)
            .unwrap()
            .split(" ")
            .filter(|x| x.to_string() != "")
            .map(|x| u32::from_str(x).unwrap())
            .collect::<Vec<u32>>();

        let mut card_points = 0;
        for e in selected {
            if won.contains(&e) {
                card_points += 1;
            }
        }
        if card_points != 0 {
            sum += (2 as i32).pow(card_points - 1);
        }
    }
    println!("{sum}")
}

fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let mut multipliers = vec![];
    for _ in 0..lines.len() {
        multipliers.push(1)
    }
    
    let mut idx = 0; 
    for line in lines.iter() {
        let card_and_rest = line.split(": ").collect::<Vec<&str>>();
        let won_and_selected = card_and_rest
            .get(1)
            .unwrap()
            .split(" | ")
            .collect::<Vec<&str>>();
        let won = won_and_selected
            .get(0)
            .unwrap()
            .split(" ")
            .filter(|x| x.to_string() != "")
            .map(|x| u32::from_str(x).unwrap())
            .collect::<Vec<u32>>();
        let selected = won_and_selected
            .get(1)
            .unwrap()
            .split(" ")
            .filter(|x| x.to_string() != "")
            .map(|x| u32::from_str(x).unwrap())
            .collect::<Vec<u32>>();

        let mut scratchcards: usize = 0;
        for e in selected {
            if won.contains(&e) {
                scratchcards += 1;
            }
        }

        for i in (idx + 1)..min(idx + 1 + scratchcards, lines.len()) {
            multipliers[i] += multipliers[idx];
        }
        idx += 1;
    }
    let mut sum = 0;
    for (_, e) in multipliers.iter().enumerate() {
        sum += e;
    }
    println!("{:?}", sum)
}

fn main() {
    part1();
    part2();
}

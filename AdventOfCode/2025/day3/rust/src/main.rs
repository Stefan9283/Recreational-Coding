use std::{fs::File, io::{BufRead, BufReader}};


fn part1() {
    let file = File::open("in").unwrap();
    let buf = BufReader::new(file);

    let mut sum = 0;

    for line in buf.lines() {
        let content = line.unwrap();
        println!("{:?}", content);
    
        let mut largest_idx: i32 = -1;
        let mut largest_digit = '0';
        for i in (0..content.len()-1).rev() {
            let letter = content.chars().nth(i).unwrap();
            if letter >= largest_digit {
                largest_digit = letter;
                largest_idx = i as i32;
            }
        }

        let mut snd_largest_idx: i32 = -1;
        let mut snd_largest_digit = '0';
        for i in (largest_idx as usize+1..content.len()).rev() {
            let letter = content.chars().nth(i).unwrap();
            if letter > snd_largest_digit {
                snd_largest_digit = letter;
                snd_largest_idx = i as i32;
                println!("{:?} {snd_largest_idx} -> {:?} {i}", snd_largest_digit, letter)
            }
        }

        println!("{largest_idx} {largest_digit}");
        println!("{snd_largest_idx} {snd_largest_digit}");

        {
            let mut num_as_str = String::new();
            num_as_str += &largest_digit.to_string();
            num_as_str += &snd_largest_digit.to_string();
            sum += num_as_str.parse::<i32>().unwrap();
        }
    }


    println!("Part 1 answer: {sum}");

}


fn find_largest_recursively(result: & mut i64, current_joltage: String, bank: &String, idx: usize) {
    // println!("~{:?}- {}", current_joltage, idx);

    if current_joltage.len() == 12 {
        // println!("-{:?}- {}", current_joltage, idx);
        let joltage = current_joltage.parse::<i64>().unwrap();
        *result = (*result).max(joltage);
        return;
    }

    if idx >= bank.len() {
        // println!("_{:?}- {}", current_joltage, idx);
        return;
    }

    {
        // to prune some of the calls assume that the remaining digits are all 9. Would that case result in a number larger than "result"?
        let mut hypotetical_max_joltage = current_joltage.clone();
        for _ in current_joltage.len()..12 {
            hypotetical_max_joltage += "9";
        }
        let num = hypotetical_max_joltage.parse::<i64>().unwrap();
        if num < *result {
            return;
        }
    }


    {
        let mut new_joltage = current_joltage.clone();
        new_joltage += &bank.chars().nth(idx).unwrap().to_string();
        find_largest_recursively(result, new_joltage, bank, idx+1);
    }
    {
        find_largest_recursively(result, current_joltage, bank, idx+1);
    }

}


fn part2() {let file = File::open("in").unwrap();
    let buf = BufReader::new(file);

    let mut sum: i64 = 0;

    for line in buf.lines() {
        let content = line.unwrap();
        println!("{:?}", content);

        let mut num_as_str = String::new();

        let mut start_idx = 0;
        for i in 0..12 {
            // println!("- {i}");
            let mut largest_idx = 0;
            let mut largest_char = '0';
            for i in (start_idx..content.len() - (12 - 1 - i)).rev() {
            let current_char = content.chars().nth(i).unwrap();
                if current_char >= largest_char {
                    // println!(" {largest_idx} {:?} -> {i} {:?}", largest_char, current_char);
                    largest_idx = i;
                    largest_char = current_char;
                }
            }
            start_idx = largest_idx + 1;

            num_as_str += &largest_char.to_string();
        }

        println!("{:?}", num_as_str);

        sum += num_as_str.parse::<i64>().unwrap();
    }

    println!("Part 2 answer: {sum}");}

fn main() {
    // part1();
    part2();
}

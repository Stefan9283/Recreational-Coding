use std::fs;
use std::str::FromStr;


fn has2sum(list: Vec<u64>, sum: u64) -> bool {
    for i in 0..list.len() {
        for j in 0..list.len() {
            if i != j && list[i] + list[j] == sum {
                return true;
            }
        }
    }
    return false;
}

fn readInput(path: String) -> Vec<u64> {
    return fs::read_to_string("in")
        .expect("Should be able to read the file")
        .split("\n")
        .into_iter()
        .map(|num|
            u64::from_str(num)
                .expect("Should contain unsigned integers")
        )
        .collect();
}


fn part1() {
    let preamble_len: usize = 25;
    let contents: Vec<_> = readInput("in".to_string());

    for i in preamble_len..contents.len() {
        if !has2sum(Vec::from(&contents[i - preamble_len..i]), contents[i]) {
            println!("Invalid index {} at index {}", contents[i], i);
        }
    }
}


fn part2() {
    let preamble_len: usize = 25;
    let contents: Vec<_> = readInput("in".to_string());

    let mut invalid_idx: usize = 0;
    for i in preamble_len..contents.len() {
        if !has2sum(Vec::from(&contents[i - preamble_len..i]), contents[i]) {
            println!("Invalid index {} at index {}", contents[i], i);
            invalid_idx = i;
        }
    }

    let invalid_num = contents[invalid_idx];
    for start in 0..contents.len() {
        for len in 2..contents.len() - 2 {
            if start + len >= contents.len() {
                break;
            }
            let subarray = &contents[start..start + len];
            let sum: u64 = subarray.iter().sum();
            if sum == invalid_num {
                let min = subarray.iter().min().expect("Array should contain at least an element");
                let max = subarray.iter().max().expect("Array should contain at least an element");
                println!("Subarray {:?} of length {} sums up to invalid number {}", Vec::from(subarray), subarray.len(), invalid_num);
                println!("min and max values are ({}, {})", min, max);
                println!("min + max = {}", min + max);
            }
        }
    }
}

fn main() {
    part1();
    part2();
}

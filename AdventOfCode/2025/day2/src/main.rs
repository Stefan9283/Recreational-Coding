use std::{collections::HashSet, fs::File, io::{BufRead, BufReader}};

// part 1

fn is_valid(num: i128) -> bool {
    let s = num.to_string();
    if s.len() % 2 == 1 {
        return true;
    }

    let fst = s.get(..s.len()/2).unwrap();
    let snd = s.get(s.len()/2..).unwrap();
    return fst != snd;
}

fn next_invalid(num: i128) -> i128 {
    let s = num.to_string();
    if s.len() % 2 == 1 {
        let mut new_s = String::new();
        new_s += "1";
        for _ in 0..s.len() {
            new_s += "0";
        }
        return next_invalid(new_s.parse::<i128>().unwrap());
    }

    let fst = s.get(..s.len()/2).unwrap();
    let snd = s.get(s.len()/2..).unwrap();

    let fst_i = fst.parse::<i128>().unwrap();
    let snd_i = snd.parse::<i128>().unwrap();

    if fst_i > snd_i {
        let mut new_s = String::new();
        new_s += fst;
        new_s += fst;
        return new_s.parse::<i128>().unwrap();
    } else {
        let mut new_s = String::new();
        let half = (fst_i + 1).to_string();
        new_s += &half;
        new_s += &half;
        return new_s.parse::<i128>().unwrap();
    }
}


fn part1() {
    let file = File::open("in").unwrap();
    let buffered = BufReader::new(file);
    let input = buffered.lines().nth(0).unwrap().unwrap();

    let mut sum: i128 = 0;

    for ele in input.split(",") {
        let minmax: Vec<&str> = ele.split("-").collect();
        
        let min = minmax[0].parse::<i128>().unwrap();
        let max = minmax[1].parse::<i128>().unwrap();

        let mut inv = min;


        if is_valid(inv) {
            inv = next_invalid(inv)
        }

        println!(" {min} - {max}");

        loop {            
            if inv > max {
                break;
            } else {
                println!(" + {inv}");
                sum += inv
            }

            inv += 1;

            inv = next_invalid(inv);
        }
    }

    print!("Part 1 answer: {}", sum);
}


// part 2

fn recursively_generate_nums(sum: &mut i128, current_group: String, group_max_len: usize, num_of_groups: usize, min: i128, max: i128, added_nums: &mut HashSet<i128>) {
    // println!("{sum} \"{current_group}\" {group_max_len} {num_of_groups}");

    if group_max_len == current_group.len() {
        let mut num_as_string = String::new();
        for _ in 0..num_of_groups {
            num_as_string += &current_group;
        }
        let num = num_as_string.parse::<i128>().unwrap();
        if num >= min && num <= max && !added_nums.contains(&num) {
            // println!("{num}");
            *sum += num;
            added_nums.insert(num);
        }
        return;
    }

    for i in 0..10 {

        if i == 0 && current_group.len() == 0 {
            continue;
        }

        let mut modified_group = current_group.clone();
        modified_group += &i.to_string();
        recursively_generate_nums(sum, modified_group, group_max_len, num_of_groups, min, max, added_nums);
    }
}

fn part2() {
    let file = File::open("in").unwrap();
    let buffered = BufReader::new(file);
    let input = buffered.lines().nth(0).unwrap().unwrap();

    let mut sum: i128 = 0;

    for ele in input.split(",") {
        let minmax: Vec<&str> = ele.split("-").collect();
        
        let min = minmax[0].parse::<i128>().unwrap();
        let max = minmax[1].parse::<i128>().unwrap();

        // println!("{min} -> {max}");

        let mut added_nums: HashSet<i128> = HashSet::new();
        for num_len in min.to_string().len()..max.to_string().len()+1 {
            for group_size in 1..num_len {
                if num_len % group_size != 0 {
                    continue;
                }
                recursively_generate_nums(&mut sum, String::new(), group_size, num_len / group_size, min, max, &mut added_nums);
            }
        }

        // let mut added: Vec<i128> = added_nums.into_iter().collect();
        // added.sort();
        // println!("{:?}", added);
    }
    print!("Part 2 answer: {}", sum);
}

fn main() {
    // part1();
    part2();
}

use std::{fs::File, io::{BufRead, BufReader}};


#[derive(Debug, Clone, Copy)]
struct InclusiveRange {
    fst: i128,
    snd: i128
}

fn part1() {
    let file = File::open("in").expect("file should exist");
    let reader = BufReader::new(file);

    let mut ranges: Vec<InclusiveRange> = vec![];
    let mut lines_iter = reader.lines();
    loop {
        let content = lines_iter.next().unwrap().unwrap();
        if content == "" {
            break;
        }
        let nums:Vec<&str> = content.split("-").collect();
        ranges.push(InclusiveRange { fst: nums[0].parse::<i128>().unwrap(), snd: nums[1].parse::<i128>().unwrap() });
    }

    let mut total = 0;
    loop {
        let current = lines_iter.next(); 
        match current {
            None => break,
            Some(ref line) => {
                let content = current.unwrap().unwrap();
                let num = content.parse::<i128>().unwrap();
                for range in &ranges {
                    if range.fst <= num && num <= range.snd {
                        println!("{:?} {num}", range);
                        total += 1;
                        break;
                    }
                }
            }
        }
    }

    println!("Part 1 result: {total}");
}

fn part2() {
    let file = File::open("in").expect("file should exist");
    let reader = BufReader::new(file);

    let mut ranges: Vec<InclusiveRange> = vec![];
    let mut lines_iter = reader.lines();
    loop {
        let content = lines_iter.next().unwrap().unwrap();
        if content == "" {
            break;
        }
        let nums:Vec<&str> = content.split("-").collect();
        ranges.push(InclusiveRange { fst: nums[0].parse::<i128>().unwrap(), snd: nums[1].parse::<i128>().unwrap() });
    }


    


    // merge overlapping ranges

    let mut merged_ranges: Vec<InclusiveRange> = vec![];
    loop {
        ranges.sort_by(|a, b| {
            
            if a.fst != b.snd {
                return a.fst.cmp(&b.fst)
            }

            let len1 = a.snd - a.fst;
            let len2 = b.snd - b.fst;
            
            return len1.cmp(&len2)
        });

        let mut idx = 1;
        let mut range = ranges[0].clone();
        
        loop {
            if idx == ranges.len() {
                merged_ranges.push(range);
                break;
            }

            let range2 = &ranges[idx];
            idx += 1;

            if range.fst <= range2.fst && range2.fst <= range.snd {
                if range.fst <= range2.snd && range2.snd <= range.snd {
                    println!("Range {:?} contains {:?}. Skipping...", range, range2);
                    continue
                } else {
                    let new_range = InclusiveRange { fst: range.fst, snd: range2.snd };
                    println!("There is some overlap between ranges {:?} and {:?}. Meriging them into {:?}", range, range2, new_range);
                    range = new_range;
                }
            } else {
                merged_ranges.push(range);
                println!("No overlap between {:?} and {:?}", range, range2);
                range = *range2;

            }
        }

        if merged_ranges.len() == ranges.len() {
            println!("Nothing was merged this round");
            break;
        }
        println!("Merges were done. Trying another iteration...");

        ranges = merged_ranges;
        merged_ranges = vec![];
    }

    let mut total: i128 = 0;
    for range in merged_ranges {
        total += range.snd - range.fst + 1;
    }

    println!("Part 2 answer {:?}", total);
}

fn main() {
    // part1()
    part2()
}

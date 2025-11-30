use std::borrow::BorrowMut;
use std::cell::RefCell;
use std::collections::VecDeque;
use std::fs;
use std::rc::Rc;
use std::str::FromStr;

fn valid_configuration_bad(to_be_checked: &[char], damaged: &[i32]) -> bool {
    let mut damaged_ = vec![];
    let mut current = 0;
    for c in to_be_checked {
        match c {
            '.' => {
                if current != 0 {
                    damaged_.push(current);
                    current = 0;
                }
            }
            '#' => {
                current += 1;
            }
            _ => {}
        }
    }
    if current != 0 {
        damaged_.push(current);
    }

    return damaged == damaged_;
}

fn part1_sol_bad() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let mut total = 0;

    for line in lines {
        let toks = line.split(" ").collect::<Vec<&str>>();

        let springs = toks[0].chars().collect::<Vec<char>>();
        let damaged = toks[1]
            .split(",")
            .map(|x| i32::from_str(x).unwrap())
            .collect::<Vec<i32>>();

        let mut deq: VecDeque<(Vec<char>, i32)> = VecDeque::new();
        deq.push_back((springs.clone(), 0));
        let mut valid = 0;
        let mut tested: i128 = 0;
        while !deq.is_empty() {
            let (springs_, idx) = deq.pop_front().unwrap();
            if idx as usize == springs_.len() {
                if valid_configuration_bad(springs_.as_slice(), damaged.as_slice()) {
                    // println!("- {:?}", springs_);
                    valid += 1;
                }
                tested += 1;
            } else if springs_[idx as usize] == '?' {
                let mut s1 = springs_.clone();
                let mut s2 = springs_.clone();
                s1[idx as usize] = '#';
                s2[idx as usize] = '.';
                deq.push_back((s1, idx + 1));
                deq.push_back((s2, idx + 1));
            } else {
                deq.push_back((springs_.clone(), idx + 1));
            }
        }

        total += valid;

        // println!("{:?} {:?} {}", springs, damaged, valid);
        // print!("{tested}, ");
    }
    println!("{total}")
}

// some pruning - still bad

fn is_final(damage: &Vec<i32>, target_damage: &Vec<i32>) -> bool {
    let nonzero: Vec<&i32> = damage.iter().filter(|x| **x != 0).collect();
    if nonzero.len() != target_damage.len() {
        return false;
    }
    for i in 0..nonzero.len() {
        if *nonzero[i] != target_damage[i] {
            return false;
        }
    }

    return true;
}

fn worth_exploring(damage: &Vec<i32>, target_damage: &Vec<i32>) -> bool {
    let nonzero: Vec<&i32> = damage.iter().filter(|x| **x != 0).collect();
    // .collect::<Vec<i32>>();

    // println!("{:?}", (damage, target_damage));

    if nonzero.len() > target_damage.len() {
        return false;
    }
    for i in 0..nonzero.len() {
        if *nonzero[i] > target_damage[i] {
            return false;
        }
    }

    return true;
}

fn get_options(springs: Vec<char>, damaged: Vec<i32>) -> i32 {
    // current springs
    // idx in springs
    // current damage
    let mut deq: VecDeque<(Vec<char>, i32, Vec<i32>)> = VecDeque::new();
    deq.push_back((springs.clone(), 0, vec![0]));
    let mut valid = 0;
    let mut tested: i128 = 0;
    while !deq.is_empty() {
        let (springs_, idx, curr_dmg) = deq.pop_front().unwrap();
        // println!("{:?}", (&springs_, idx, &curr_dmg));

        if idx as usize == springs_.len() {
            if is_final(&curr_dmg, &damaged) {
                // println!("-- {:?}", (springs_, &curr_dmg, &damaged));
                valid += 1;
            }
        } else if springs_[idx as usize] == '?' {
            let mut s1 = springs_.clone();
            let mut s2 = springs_.clone();
            s1[idx as usize] = '#';
            s2[idx as usize] = '.';

            let mut curr_dmg1 = curr_dmg.clone();
            curr_dmg1[curr_dmg.len() - 1] += 1;

            let mut curr_dmg2 = curr_dmg.clone();
            curr_dmg2.push(0);

            if worth_exploring(&curr_dmg1, &damaged) {
                deq.push_back((s1, idx + 1, curr_dmg1));
            }

            if worth_exploring(&curr_dmg2, &damaged) {
                deq.push_back((s2, idx + 1, curr_dmg2));
            }
        } else if springs_[idx as usize] == '.' {
            let mut curr_dmg2 = curr_dmg.clone();
            curr_dmg2 = curr_dmg2.into_iter().filter(|x| *x != 0).collect();
            curr_dmg2.push(0);

            if worth_exploring(&curr_dmg2, &damaged) {
                deq.push_back((springs_, idx + 1, curr_dmg2));
            }
        } else if springs_[idx as usize] == '#' {
            let mut curr_dmg1 = curr_dmg.clone();
            curr_dmg1[curr_dmg.len() - 1] += 1;

            if worth_exploring(&curr_dmg1, &damaged) {
                deq.push_back((springs_, idx + 1, curr_dmg1));
            }
        }
    }

    return valid;
}

fn sol2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    {
        let mut total = 0;
        for line in &lines {
            let toks = line.split(" ").collect::<Vec<&str>>();

            let springs = toks[0].chars().collect::<Vec<char>>();
            let damaged = toks[1]
                .split(",")
                .map(|x| i32::from_str(x).unwrap())
                .collect::<Vec<i32>>();

            let result = get_options(springs, damaged);

            // println!("{:?}", (line, result));

            total += result;
        }
        println!("{total}");
    }

    {
        let mut total = 0;
        for line in &lines {
            let toks = line.split(" ").collect::<Vec<&str>>();

            let springs = toks[0].chars().collect::<Vec<char>>();
            let damaged = toks[1]
                .split(",")
                .map(|x| i32::from_str(x).unwrap())
                .collect::<Vec<i32>>();


            let mut springs_ = springs.clone();
            let mut damaged_ = damaged.clone();
            for _ in 0..4 {
                springs_.push('?');
                for c in &springs {
                    springs_.push(*c);
                }
                for i in &damaged {
                    damaged_.push(*i);
                }
            }


            println!("{:?}\n   {:?}", (springs, damaged), (&springs_, &damaged_));


            total += get_options(springs_, damaged_);
        }
        println!("{total}");
    }
}




// dynamic programming

// ????.#...#... 4,1,1 - 16 
// ????.#...#...?????.#...#...?????.#...#...?????.#...#...?????.#...#... 4,1,1,4,1,1,4,1,1,4,1,1,4,1,1
// 



fn main() {

}


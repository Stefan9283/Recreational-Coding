use std::cmp::min;
use std::collections::LinkedList;
use std::fs;
use std::str::FromStr;

#[derive(Clone)]
#[derive(Debug)]
struct Group {
    sum: i32,
    qe: i128, // product,
    count: i32
}

impl Default for Group {
    fn default() -> Self {
        Group{ sum: 0, qe: 1, count: 0 }
    }
}


fn main() {
    let mut weights: Vec<i32> = fs::read_to_string("in").unwrap().split("\n")
        .map(|s| { i32::from_str(s).unwrap() }).collect();
    // weights.reverse();
    // println!("{:?}", weights);

    let target_sum = weights.iter().sum::<i32>() / 3;

    let mut stack: LinkedList<(Vec<Group>, Vec<i32>)> = Default::default();
    stack.push_back((vec![Default::default(), Default::default(), Default::default()], weights));

    let mut min_qe = i128::MAX;
    let mut min_count = i128::MAX;

    while !stack.is_empty() {
        let (mut groups, mut remaining): (Vec<Group>, Vec<i32>) = stack.pop_back().unwrap();
        // println!("groups {:?}, remaining {:?}", groups, remaining);

        if min_count < groups[0].count as i128 {
            continue
        }

        if remaining.len() != 0 {
            let last = remaining.pop().unwrap();
            for i in 0..3 {
                let mut groups_ = groups.clone();

                groups_[i].count += 1;
                groups_[i].qe *= last as i128;
                groups_[i].sum += last;

                if groups_[i].sum > target_sum {
                    continue
                }

                groups_.sort_by(|a,b| { a.count.cmp(&b.count) });

                if min_count < groups_[0].count as i128 {
                    continue
                }

                stack.push_back((groups_, remaining.clone()));
            }
        } else {
            let mut valid = true;
            for i in 0..3 {
                valid &= groups[i].sum == target_sum;
            }
            if valid {
                if groups[0].count <= groups[1].count || groups[0].count <= groups[2].count {
                    if min_count >= groups[0].count as i128 {
                        min_count = groups[0].count as i128;
                        min_qe = min(groups[0].qe, min_qe);
                        println!("{:?} {} {}", groups, min_qe, min_count)
                    }
                }
            }
        }
    }

    println!("Min QE = {}", min_qe);
}

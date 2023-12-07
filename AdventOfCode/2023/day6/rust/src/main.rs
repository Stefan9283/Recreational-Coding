use std::fs;
use std::str::FromStr;
fn part1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();
    let time = lines.get(0).unwrap().split(" ").into_iter().filter(|x| {x.to_string() != "Time:".to_string() && x.to_string() != "".to_string()}).map(|x| {i32::from_str(x).unwrap()}).collect::<Vec<i32>>();
    let dist = lines.get(1).unwrap().split(" ").into_iter().filter(|x| {x.to_string() != "Distance:".to_string() && x.to_string() != "".to_string()}).map(|x| {i32::from_str(x).unwrap()}).collect::<Vec<i32>>();

    let mut res = 1;
    for (i, t) in time.iter().enumerate() {
        let mut ways_count = 0;
        for dt in 0..*t as usize {
            let velocity = dt as i32;
            let max_dist = (t - dt as i32) * velocity;
            if max_dist > *dist.get(i).unwrap() {
                ways_count += 1;
                // println!("{dt} {max_dist}");
            }
        }
        // println!("--- {} {}", i, ways_count);
        res *= ways_count;
    }
    // println!("{:?} {:?}", time, dist);
    println!("{}", res);
}

fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();
    let time = i64::from_str(lines.get(0).unwrap().split(" ").into_iter().filter(|x| {x.to_string() != "Time:".to_string() && x.to_string() != "".to_string()}).collect::<Vec<&str>>().connect("").as_str()).unwrap();
    let dist = i64::from_str(lines.get(1).unwrap().split(" ").into_iter().filter(|x| {x.to_string() != "Distance:".to_string() && x.to_string() != "".to_string()}).collect::<Vec<&str>>().connect("").as_str()).unwrap();

    let mut ways_count = 0;
    for dt in 0..time as usize {
        let velocity = dt as i64;
        let max_dist = (time - dt as i64) * velocity;
        if max_dist > dist {
            ways_count += 1;
            // println!("{dt} {max_dist}");
        }
    }
    // println!("--- {} {}", i, ways_count);
    let res = ways_count;
    println!("{res}")
}

fn main() {
    part1();
    part2();
}
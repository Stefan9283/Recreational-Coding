use std::fs;
use std::str::FromStr;

fn main() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let mut history: Vec<Vec<i32>> = Vec::new();
    for line in content.split("\n") {
        history.push(
            line.split(" ").map(|v| {
                i32::from_str(v).unwrap()
            }).collect::<Vec<i32>>())
    }

    let mut sum1 = 0;
    let mut sum2 = 0;

    for v in &history {
        let mut sequences: Vec<Vec<i32>> = Vec::new();
        sequences.push(v.to_vec());

        while !sequences.get(sequences.len() - 1).unwrap().iter().all(|x| *x == 0) {
            let mut new_seq = Vec::new();
            let last_seq = sequences.get(sequences.len() - 1).unwrap();
            for i in 0..last_seq.len()-1 {
                new_seq.push(
                    last_seq.get(i + 1).unwrap() - last_seq.get(i).unwrap()
                )
            }
            sequences.push(new_seq);
        }

        // print!("{:?} {:?} ", v, sequences);
        
        let mut last = 0;
        let mut frst = 0;
        for i in 1..sequences.len() {
            let line = sequences.get(sequences.len() - 1 - i).unwrap();
            last = last + line.get(line.len() - 1).unwrap();
            frst = line.get(0).unwrap() - frst; 
        }

        // println!("{frst} {last}");
        
        sum1 += last;
        sum2 += frst;
    }

    println!("{}", sum1);
    println!("{}", sum2);
}

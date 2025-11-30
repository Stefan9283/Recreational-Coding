use std::{fs, collections::HashMap};

fn part1() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let steps = lines.get(0).unwrap();

    let mut map = HashMap::new();

    for line in &lines[2..] {
        let toks = line.split(" = ").collect::<Vec<&str>>();
        let src = toks[0];
        let left_right = toks[1][1..toks[1].len() - 1].split(", ").collect::<Vec<&str>>();
        map.insert(src, left_right);
    }

    let mut current = "AAA";
    let mut idx = 0;
    let mut count = 0;

    while current != "ZZZ" {

        if steps.as_bytes()[idx] == b'L' {
            current = map.get(current).unwrap()[0];
        } else if steps.as_bytes()[idx] == b'R' {
            current = map.get(current).unwrap()[1];
        } else {
            panic!("Unknown direction")
        }

        idx += 1;
        if idx == steps.len() {
            idx = 0;
        }

        count += 1;
    }
    println!("{count}")
}

fn inv(a: i128, m: i128) -> i128 {
    let m0 = m;
    let mut m = m;
    let mut a = a;
    let mut t: i128;
    let mut q: i128;
    let mut x0 = 0;
    let mut x1 = 1;

    if m == 1 {
        return 0;
    }

    // Apply extended Euclid Algorithm
    while a > 1 {
        // q is quotient
        println!("aaa {:?} {:?}", a, m);
        q = a / m;

        t = m;

        // m is remainder now, process same as
        // euclid's algo
        m = a % m;
        a = t;

        t = x0;

        x0 = x1 - q * x0;

        x1 = t;
    }

    // Make x1 positive
    if x1 < 0 {
        x1 += m0;
    }

    x1
}

fn findMinX(num: Vec<i32>, rem: Vec<i32>) -> i128 {
    // Compute product of all numbers
    let prod = num.iter().fold(1, |acc: i128, &x| acc * x as i128 );

    // Apply above formula
    let result = num.into_iter().enumerate().fold(0, |acc, (i, x)| {
        let pp = prod / x as i128;
        println!("{:?} | {:?} | {:?} {:?} {:?}",
                 prod, x,
                 pp,
                 pp % x as i128,
                 pp / x as i128
        );
        acc + (rem[i] as i128) * inv(pp, x as i128) * pp
    });

    result % prod
}


fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let steps = lines.get(0).unwrap();

    let mut map = HashMap::new();

    let mut start_positions: Vec<&str> = Vec::new();

    for line in &lines[2..] {
        let tokens = line.split(" = ").collect::<Vec<&str>>();
        let src = tokens[0];
        let left_right = tokens[1][1..tokens[1].len() - 1].split(", ").collect::<Vec<&str>>();
        if src.ends_with("A") {
            start_positions.push(src)
        }
        map.insert(src, left_right);
    }


    let mut rem = vec![];
    let mut num = vec![];

    for i in 0..start_positions.len() {
        println!("-------------------------- {:?}", start_positions.get(i).unwrap());
        let mut known_states: Vec<(i32, &str)> = vec![]; // TODO keep track of known states

        let mut current = start_positions.get(i).unwrap().clone();
        let mut step_idx: i32 = 0;
        
        let mut cycle_start = -1;

        loop {
            known_states.push((step_idx, current.clone()));

            let direction = steps.as_bytes()[step_idx as usize];
            if direction == b'L' {
                current = map.get(current).unwrap()[0];
            } else if direction == b'R' {
                current = map.get(current).unwrap()[1];
            } else {
                panic!("Unknown direction. Now next node could be found for direction \"{:?}\" after node \"{:?}\"",  current, direction)
            }

            step_idx += 1;

            if step_idx == steps.len() as i32 {
                step_idx = 0
            }

            if known_states.contains(&(step_idx, current)) {
                // TODO
                cycle_start = known_states.iter().position(|&x| { return x.eq(&(step_idx, current)) }).unwrap() as i32;
                // cycle_start = *known_states.get(&(current, step_idx)).unwrap();
                break
            }
        }

        // println!("{:?}", known_states);
        // println!("dest={:?} cycle between indices {}..{}", known_states[known_states.len() - 1], cycle_start, cycle_start + known_states.len() as i32 - cycle_start);
        println!("cycle between indices {}..{}", cycle_start, known_states.len() as i32 - cycle_start);

        rem.push(cycle_start);
        num.push(known_states.len() as i32 - cycle_start);
    }

    // X % m1 = a1
    // X % m2 = a2
    // X % m3 = a3
    // X % m4 = a4
    // X % m5 = a5

    // X = sum (M ai Mi Mi^-1) for i in 1..5

    println!("{:?} {:?}", rem, num);
    let minX = findMinX(num, rem);
    println!("{:?}", minX);

    // TODO
    // Chinese Remainder Theorem

    // LR

    // 11A = (11B, XXX)
    // 11B = (XXX, 11Z)
    // 11Z = (11B, XXX)
    // 22A = (22B, XXX)
    // 22B = (22C, 22C)
    // 22C = (22Z, 22Z)
    // 22Z = (22B, 22B)
    // XXX = (XXX, XXX)
    // Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

    // Step 0: You are at 11A and 22A.
    // Step 1: You choose all of the left paths, leading you to 11B and 22B.
    // Step 2: You choose all of the right paths, leading you to 11Z and 22C.
    // Step 3: You choose all of the left paths, leading you to 11B and 22Z.
    // Step 4: You choose all of the right paths, leading you to 11Z and 22B.
    // Step 5: You choose all of the left paths, leading you to 11B and 22C.
    // Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
    // So, in this example, you end up entirely on nodes that end in Z after 6 steps.

    /*
    
        11A -> 11Z 2
        22B -> 11Z 3

        x = 0 mod 2
        x = 0 mod 3

        N = 2 * 3 = 6
        m1 = N / 2 = 3
        m2 = N / 3 = 2
    
    */







}


fn part2_bad() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let lines = content.split("\n").collect::<Vec<&str>>();

    let steps = lines.get(0).unwrap();

    let mut map = HashMap::new();

    let mut current: Vec<&str> = Vec::new();

    for line in &lines[2..] {
        let toks = line.split(" = ").collect::<Vec<&str>>();
        let src = toks[0];
        let left_right = toks[1][1..toks[1].len() - 1].split(", ").collect::<Vec<&str>>();
        if src.ends_with("A") {
            current.push(src)
        }
        map.insert(src, left_right);
    }

    println!("{:?}", current);



    let mut idx = 0;
    let mut count: i128 = 0;

    loop {
        let mut zs = 0;
        for curr in &current {
            // println!("{:?} {}", curr, curr.ends_with('Z'));
            if curr.ends_with('Z') {
                zs += 1;
            }
        }

        // println!("{:?} {}", current, zs);


        if zs == current.len() {
            break
        }

        
        for curr in &mut current {
            // println!("{} {} {:?} {:?}", idx, char::from(steps.as_bytes()[idx]), current, map.get(current).unwrap());
            if steps.as_bytes()[idx] == b'L' {
                *curr = map.get(curr).unwrap()[0];
            } else if steps.as_bytes()[idx] == b'R' {
                *curr = map.get(curr).unwrap()[1];
            } else {
                panic!("Unknown direction")
            }
        }

        idx += 1;
        if idx == steps.len() {
            idx = 0;
        }

        count += 1;

    }

    println!("{count}")

}

fn main() {
    // part1();
    part2();
}
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

fn part2() {
    let content = fs::read_to_string("in2").expect("Should be able to read the input from file");
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

    // stop_string, cycle_start, cycle_len, stop_pos_in_cycle
    let mut vals: Vec<(&str, i128, i128, i128)> = Vec::new();

    for i in 0..start_positions.len() {
        println!("-------------------------- {:?}", start_positions.get(i).unwrap());
        let mut known_states: HashMap<(&str, i32), i128> = HashMap::new(); // TODO keep track of known states

        let mut current = start_positions.get(i).unwrap().clone();
        let mut step_idx: i32 = 0;
        
        let mut iter_idx = 0;

        let mut cycle_start = -1; 

        let mut cycle_stop = "";
        let mut cycle_stop_idx: i128 = -1;

        loop {
            // println!("{:?} {step_idx}", current);
          
            known_states.insert((current.clone(), step_idx), iter_idx);

            if steps.as_bytes()[step_idx as usize] == b'L' {
                current = map.get(current).unwrap()[0];
            } else if steps.as_bytes()[step_idx as usize] == b'R' {
                current = map.get(current).unwrap()[1];
            } else {
                panic!("Unknown direction")
            }

            step_idx += 1;

            if step_idx == steps.len() as i32 {
                step_idx = 0
            }

            if known_states.contains_key(&(current, step_idx)) {
                // println!("{:?} {step_idx}", current);
                // known_states.insert((current.clone(), step_idx), step);
                cycle_start = *known_states.get(&(current, step_idx)).unwrap();
                // println!("{:?}", known_states);
                // println!("{cycle_start}");
                break
            }


            if current.ends_with('Z') {
                cycle_stop = current;
                cycle_stop_idx = iter_idx;
            }


            iter_idx += 1;
        }

        // println!("{:?}", known_states);


        println!("{:?}", known_states);
        println!("dest={:?} cycle between indices {}..{}", cycle_stop, cycle_start, cycle_start + known_states.len() as i128 - cycle_start);


        // TODO exista mai multi pasi in ciclu cu Z pe ultima pozitie. Push tuturor.
        // Exemplu:
        // {
        //     ("22A", 0): 0, 
        //     ("22B", 1): 1,
        //     ("22C", 0): 2, 
        //     ("22Z", 1): 3, <--
        //     ("22B", 0): 4, 
        //     ("22C", 1): 5, 
        //     ("22Z", 0): 6, <--
        // }
        vals.push((cycle_stop, cycle_start, known_states.len() as i128 - cycle_start, cycle_stop_idx));
    }

    println!("{:?}", vals);

    // X % m1 = a1
    // X % m2 = a2
    // X % m3 = a3
    // X % m4 = a4
    // X % m5 = a5
    

    // X = sum (M ai Mi Mi^-1) for i in 1..5


    // TODO
    // Chinese Remainder Theorem

    







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
use std::fs;

fn part1() {
    let contents = fs::read_to_string("in")
        .expect("Should have been able to read the file");
    let instr: Vec<_> = contents.split("\n").collect();
    let mut acc: i32 = 0;
    let mut pc: i32 = 0;

    let mut visited = vec![false; instr.len()];


    while visited[pc as usize] != true {
        let elem = instr[pc as usize];
        visited[pc as usize] = true;
        let tokens: Vec<_> = elem.split(" ").collect();
        if tokens[0] == "nop" {
            pc += 1;
        } else if tokens[0] == "acc" {
            acc += tokens[1].parse::<i32>().unwrap();
            pc += 1;
        } else if tokens[0] == "jmp" {
            pc += tokens[1].parse::<i32>().unwrap();
        }
    }
    println!("{}", acc)
}



fn change_i(i: u32) -> Result<i32, String> {
    let contents = fs::read_to_string("in")
        .expect("Should have been able to read the file");
    let instr: Vec<_> = contents.split("\n").collect();
    let mut acc: i32 = 0;
    let mut pc: i32 = 0;

    let mut visited = vec![false; instr.len()];

    loop {
        if pc >= instr.len() as i32 {
            return Ok(acc);
        }
        if visited[pc as usize] == true {
            return Err("loop detected".to_string());
        }


        let elem = instr[pc as usize];
        // println!("{}", elem);
        visited[pc as usize] = true;
        let mut tokens: Vec<_> = elem.split(" ").collect();

        if pc == i as i32 {
            if tokens[0] == "nop" {
                tokens[0] = "jmp"
            } else if tokens[0] == "jmp" {
                tokens[0] = "nop"
            }
        }

        if tokens[0] == "nop" {
            pc += 1;
        } else if tokens[0] == "acc" {
            acc += tokens[1].parse::<i32>().unwrap();
            pc += 1;
        } else if tokens[0] == "jmp" {
            pc += tokens[1].parse::<i32>().unwrap();
        }
    }
}

fn part2() {
    let contents = fs::read_to_string("in")
        .expect("Should have been able to read the file");
    let instr: Vec<_> = contents.split("\n").collect();
    for i in 0..instr.len() {
        match change_i(i as u32) {
            Ok(res) => println!("{}", res),
            _ => {}
        }
    }
}

fn main() {
    part1();
    part2();
}

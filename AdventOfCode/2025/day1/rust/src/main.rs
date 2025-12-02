use std::io::BufReader;
use std::fs::File;
use std::io::BufRead;

fn part1() -> Result<(), Box<dyn std::error::Error>> {
    let file = File::open("in")?;
    let reader = BufReader::new(file);

    let mut current: i32 = 50;
    let mut counter: i32 = 0;

    for line_result in reader.lines() {
        let line = line_result?;
        let line: &str = line.trim();  // Remove leading and trailing whitespace
        
        let val: i32 = line.get(1..).unwrap().parse().unwrap(); 

        let rotation = line.chars().into_iter().nth(0).unwrap();

        if rotation == 'L' {
            current -= val
        } else {
            current += val
        }

        current %= 100;
        if current < 0 {
            current += 100
        }

        if current == 0 {
            counter += 1
        }
    }

    println!("Part 1 answer: {}", counter);

    Ok(())
}

fn part2() -> Result<(), Box<dyn std::error::Error>> {
    let file = File::open("in")?;
    let reader = BufReader::new(file);

    let mut current: i32 = 50;
    let mut counter: i32 = 0;

    let mut prev_current: i32 = 50;

    for line_result in reader.lines() {
        let line = line_result?;
        let line: &str = line.trim();  // Remove leading and trailing whitespace
        
        let mut val: i32 = line.get(1..).unwrap().parse().unwrap(); 

        let rotation = line.chars().into_iter().nth(0).unwrap();

        counter += val / 100;

        val %= 100;

        if val == 0 {
            continue;
        }

        prev_current = current;

        if rotation == 'L' {
            current -= val
        } else {
            current += val
        }

        if current < 0 {
            current += 100;
            if prev_current != 0 {
                counter += 1 
            }
        } else if current >= 100 {
            counter += 1 
        } else if current == 0 {
            counter += 1
        }
        current %= 100;

    }

    println!("Part 2 answer: {counter}");

    Ok(())
}

fn main() {
    // let _ = part1();
    let _ = part2();
}

use std::fs;
use std::str::FromStr;

fn compute_hash(s: &str) -> u8 {
    let mut hash: u32 = 0;
    for c in s.chars() {
        hash += c as u32;
        hash *= 17;
        hash %= 256;
    }
    return hash as u8;
}

#[derive(Debug)]
struct Pair<'a> {
    key: &'a str,
    value: i32,
}

fn main() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let tokens = content.split(",").collect::<Vec<&str>>();

    {
        // part 1
        let mut res: usize = 0;
        for tok in &tokens {
            res += compute_hash(tok) as usize
        }
        println!("{:?}", res);
    }
    {
        // part 2
        let mut boxes: Vec<Vec<Pair>> = vec![];
        for _ in 0..256 {
            boxes.push(vec![]);
        }
        for tok in &tokens {
            println!("{:?}", tok);
            if tok.contains("=") {
                let keyval = tok.split("=").collect::<Vec<&str>>();
                let hash = compute_hash(keyval[0]) as usize;
                
                match boxes[hash].iter().position(|x| x.key == keyval[0]) {
                    Some(idx) => {
                        boxes[hash][idx].value = i32::from_str(keyval[1]).unwrap();
                    }
                    None => {
                        boxes[hash].push(Pair {
                            key: keyval[0],
                            value: i32::from_str(keyval[1]).unwrap(),
                        })
                    }
                }

               
            } else if tok.ends_with("-") {
                let key = tok.replace("-", "");
                let hash = compute_hash(key.as_str()) as usize;

                match boxes[hash].iter().position(|x| x.key == key.as_str()) {
                    Some(idx) => {
                        let _ = boxes[hash].remove(idx);
                    }
                    None => {}
                }
            }

            for (i, boxx) in boxes.iter().enumerate() {
                if boxx.len() != 0 {
                    println!("Box {i}: {:?}", boxx)
                }
            }
            println!("");
        }

        let mut res = 0;
        for (ib, b) in boxes.iter().enumerate() {
            for (ip, pair) in b.iter().enumerate() {
                res += (ib + 1) * (ip + 1) * pair.value as usize;
                println!(
                    "{:?}: {} (box {}) * slot {} * {} focal len",
                    pair.key,
                    ib + 1,
                    ib,
                    ip + 1,
                    pair.value
                );
            }
        }
        println!("{res}")
    }
}

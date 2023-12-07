use std::cmp::Ordering;
use std::collections::HashMap;
use std::fs;
use std::str::FromStr;

// part 1

fn hand_to_ints1(hand: &str) -> Vec<i32> {
    hand.as_bytes().into_iter().map(|x| {
        if x.is_ascii_digit() {
            return i32::from_str((x - 48).to_string().as_str()).unwrap()
        }
        if *x == b'T' {
            return 10;
        }
        if *x == b'J' {
            return 11;
        }
        if *x == b'Q' {
            return 12;
        }
        if *x == b'K' {
            return 13;
        }
        if *x == b'A' {
            return 14;
        }
        panic!("Invalid card type")
    }).collect::<Vec<i32>>()
}

fn get_hand_type1(hand: &str) -> i32 {
    let chars = hand.chars();
    let mut count: HashMap<char, i32> = HashMap::new();
    for c in chars {
        count.insert(c, count.get(&c).unwrap_or_else(|| {&0}) + 1) ;
    }

    let mut pairs = 0; 
    let mut threes = false;
    for v in count.values() {
        if *v == 5 {
            return 6;
        } 
        if *v == 4 {
            return 5;
        }
        if *v == 3 {
            threes = true;
        }
        if *v == 2 {
            pairs += 1;
        }
    }


    if threes == true {
        if pairs == 1 {
            return 4;
        } 
        return 3; 
    }

    if pairs == 2 {
        return 2; 
    } else if pairs == 1 {
        return 1;
    }

    return 0; 
}

fn hands_comparator1(a: &(&str, i32), b: &(&str, i32)) -> Ordering {
    let t1 = get_hand_type1(a.0);
    let t2 = get_hand_type1(b.0);

    // println!("{:?} {}", a, t1);
    // println!("{:?} {}", b, t2);

    if t1 == t2 {
        let v1 = hand_to_ints1(a.0);
        let v2 = hand_to_ints1(b.0);
        // println!("{:?} {:?}", v1, v2);
        return v1.cmp(&v2);
    }

    return t1.cmp(&t2);
}

fn part1() {
    let content = fs::read_to_string("in0").expect("Should be able to read the input from file");
    let mut hands = content.split("\n").map(|x| { 
            let toks = x.split(" ").collect::<Vec<&str>>();
            return (
                *toks.get(0).unwrap(),
                i32::from_str(toks.get(1).unwrap()).unwrap()
            ) 
        }).collect::<Vec<(&str, i32)>>();

    hands.sort_by(hands_comparator1);

    let mut sum = 0;
    for (i, (_, bid)) in hands.iter().enumerate() {
        sum += (i + 1) as i32 * bid;
    }
    println!("{sum}")
}

// part 2

fn hand_to_ints2(hand: &str) -> Vec<i32> {
    hand.as_bytes().into_iter().map(|x| {
        if x.is_ascii_digit() {
            return i32::from_str((x - 48).to_string().as_str()).unwrap()
        }
        if *x == b'T' {
            return 10;
        }
        if *x == b'J' {
            return 1;
        }
        if *x == b'Q' {
            return 12;
        }
        if *x == b'K' {
            return 13;
        }
        if *x == b'A' {
            return 14;
        }
        panic!("Invalid card type")
    }).collect::<Vec<i32>>()
}

fn get_hand_type2(hand: &str) -> i32 {
    let chars = hand.chars();
    let mut count: HashMap<char, i32> = HashMap::new();
    for c in chars {
        count.insert(c, count.get(&c).unwrap_or_else(|| {&0}) + 1) ;
    }

    let mut pairs = 0; 
    let mut threes = false;
    let mut fours = false;
    for (c, v) in &count {
        if *c == 'J' {
            continue;
        }
        if *v == 5 {
            return 6;
        } 
        if *v == 4 {
            fours = true
        }
        if *v == 3 {
            threes = true;
        }
        if *v == 2 {
            pairs += 1;
        }
    }



    let mut js = 0;
    
    {
        let js_ = count.get(&'J'); 
        if js_.is_some() {
            js = *js_.unwrap();
        }
    }


    if fours == true {
        if js == 1 {
            return 6;
        }
        return 5;
    }

    if threes == true {
        if js == 2 {
            return 6;
        }
        if js == 1 {
            return 5;
        }

        if pairs == 1 {
            return 4;
        } 
        return 3; 
    }

    if pairs == 2 {
        if js == 1 {
            return 4;
        }
        return 2; 
    }
    
    if pairs == 1 {
        if js == 3 {
            return 6;
        }
        if js == 2 {
            return 5
        }
        if js == 1 {
            return 3;
        }
        return 1;
    }


    if js == 5 {
        return 6
    }
    if js == 4 {
        return 6;
    }
    if js == 3 {
        return 5;
    }
    if js == 2 {
        return 3;
    }
    if js == 1 {
        return 1;
    }

    return 0; 
}

fn hands_comparator2(a: &(&str, i32), b: &(&str, i32)) -> Ordering {
    let t1 = get_hand_type2(a.0);
    let t2 = get_hand_type2(b.0);

    // print!("{:?} {} vs {:?} {}", a, t1, b, t2);

    if t1 == t2 {
        let v1 = hand_to_ints2(a.0);
        let v2 = hand_to_ints2(b.0);
        // println!("{:?} {:?}", v1, v2);
        return v1.cmp(&v2);
    }
    // println!();

    return t1.cmp(&t2);
}


fn part2() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    let mut hands = content.split("\n").map(|x| { 
            let toks = x.split(" ").collect::<Vec<&str>>();
            return (
                *toks.get(0).unwrap(),
                i32::from_str(toks.get(1).unwrap()).unwrap()
            ) 
        }).collect::<Vec<(&str, i32)>>();

    hands.sort_by(hands_comparator2);

    // for hand in &hands {
    //     print!("[{:?} {}] ", hand.0, get_hand_type2(hand.0));
    // }
    // println!("{:?}", hands);

    let mut sum = 0;
    for (i, (_, bid)) in hands.iter().enumerate() {
        sum += (i + 1) as i32 * bid;
    }
    // println!("{} {}", 242595916 < sum, sum < 243267483 /*243481607*/)
    println!("{sum}")
}



fn main() {
    part1();
    part2();
}
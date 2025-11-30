use std::fs;

fn main() {
    let content = fs::read_to_string("in").expect("Should be able to read the input from file");
    println!("{content}");
}

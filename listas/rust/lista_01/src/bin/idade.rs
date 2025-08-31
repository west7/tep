use std::io::{Read, stdin};

fn main() {
    let mut s = String::new();
    stdin().read_to_string(&mut s).unwrap();
    let mut ns: Vec<i32> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();
    ns.sort();
    println!("{}", ns[1]);
}

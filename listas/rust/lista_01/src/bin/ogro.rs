use std::io::{Read, stdin};
use std::convert::TryInto;

fn main() {
    let mut s = String::new();
    stdin().read_to_string(&mut s).unwrap();
    let ns: Vec<i32> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();
    let [e, d] = ns[..2].try_into().unwrap();
    if e > d {
        println!("{}", e + d);
    } else {
        println!("{}", 2 * (d - e));
    }
}

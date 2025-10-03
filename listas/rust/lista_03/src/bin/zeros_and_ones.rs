use std::io::stdin;

fn main() {
    let mut s = String::new();
    let n = stdin().read_line(&mut s).unwrap();
    stdin().read_line(&mut s).unwrap();
    let mut ns = s.split_whitespace()
    .map(|x| x.trim().)
}

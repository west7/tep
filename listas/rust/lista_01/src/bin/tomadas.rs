use std::io::stdin;

type int = u128;

fn main() {
    let mut sum: int = 0; 
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    for st in s.split(' ') {
        sum += st.trim().parse::<int>().unwrap();
    }
    sum -= 3;
    println!("{sum}");
}
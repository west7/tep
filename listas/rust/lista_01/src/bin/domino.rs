use std::io::stdin;

use u128 as int;

fn main() {
    let mut s = String::new();
    stdin().read_line(&mut s).unwrap();
    let n: int = s.trim().parse().unwrap();

    let mut res: int = 0;
    for i in 1..=(n+1) {
        res += i;
    }
    
    //let res = ((n + 1) * (n + 2)) / 2;
    println!("{res}");    
}

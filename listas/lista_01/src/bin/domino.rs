use std::io::stdin;

fn main() {
    let mut s = String::new();
    stdin().read_line(&mut s).expect("Falha ao ler entrada");
    let n: u16 = s.trim().parse().expect("A entrada deve ser um número");

    let res = ((n + 1) * (n + 2)) / 2;
    println!("{res}");    
}

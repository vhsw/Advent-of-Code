use std::fs;

fn main() {
    let data = fs::read_to_string("day_17/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> String {
    let ([a, b, c], program) = parse_input(data);
    execute(a, b, c, &program)
        .iter()
        .map(|i| i.to_string())
        .collect::<Vec<_>>()
        .join(",")
}
fn part_2(data: &str) -> isize {
    let ([_, b, c], program) = parse_input(data);
    let mut offset: usize = 0;
    let mut solved_part = 0;
    while program.len() >= 7 && offset < program.len() - 7 {
        let mul = 0o10_isize.pow(offset.try_into().unwrap());
        for i in 0o100_000..0o1_000_000 {
            let a = (mul * i) + solved_part;
            let res: Vec<isize> = execute(a, b, c, &program);
            if res.len() == offset + 6 && res[..offset + 1] == program[..offset + 1] {
                solved_part += a & (0o7 * mul);
                offset += 1;
                break;
            }
        }
    }
    for i in 0..0o10_000_000 {
        let mul = 0o10_isize.pow((offset).try_into().unwrap());
        let a = (mul * i) + solved_part;
        if execute(a, b, c, &program) == program {
            return a;
        }
    }
    unreachable!();
}
fn parse_input(data: &str) -> ([isize; 3], Vec<isize>) {
    let (registers, program) = data.split_once("\n\n").unwrap();
    (
        registers
            .lines()
            .map(|l| l.split_once(": ").unwrap().1.parse().unwrap())
            .collect::<Vec<_>>()
            .try_into()
            .unwrap(),
        program
            .split_once(": ")
            .unwrap()
            .1
            .trim()
            .split(',')
            .map(|s| s.parse().unwrap())
            .collect(),
    )
}
fn execute(a: isize, b: isize, c: isize, program: &[isize]) -> Vec<isize> {
    let mut a = a;
    let mut b = b;
    let mut c = c;
    let mut ip = 0;
    let mut output = Vec::new();
    while ip < program.len() - 1 {
        let literal = program[ip + 1];
        let combo = match literal {
            0..4 => literal,
            4 => a,
            5 => b,
            6 => c,
            _ => unreachable!(),
        };
        match program[ip] {
            0 => {
                // adv
                a /= 2_isize.pow(combo.try_into().unwrap());
                ip += 2;
            }
            1 => {
                // blx
                b ^= literal;
                ip += 2;
            }
            2 => {
                // bst
                b = combo % 8;
                ip += 2;
            }
            3 => {
                // jnz
                if a == 0 {
                    ip += 2;
                } else {
                    ip = literal as usize;
                }
            }
            4 => {
                // bxc
                b ^= c;
                ip += 2;
            }
            5 => {
                // out
                output.push(combo % 8);
                ip += 2;
            }
            6 => {
                // bdv
                b = a / 2_isize.pow(combo.try_into().unwrap());
                ip += 2;
            }
            7 => {
                // cdv
                c = a / 2_isize.pow(combo.try_into().unwrap());
                ip += 2;
            }
            _ => unreachable!(),
        }
    }
    output
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), "4,6,3,5,6,3,5,2,1,0");
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&quine_example()), 117440);
    }
    fn example() -> String {
        String::from(
            "
            Register A: 729
            Register B: 0
            Register C: 0

            Program: 0,1,5,4,3,0
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn quine_example() -> String {
        String::from(
            "
            Register A: 2024
            Register B: 0
            Register C: 0

            Program: 0,3,5,4,3,0
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

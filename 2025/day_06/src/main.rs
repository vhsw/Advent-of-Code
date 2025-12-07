use std::fs;

fn main() {
    let data = fs::read_to_string("day_06/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> u64 {
    parse_input(data)
        .iter()
        .map(|(op, values)| match op {
            '+' => parse_tb_lr(values).sum::<u64>(),
            '*' => parse_tb_lr(values).product::<u64>(),
            _ => panic!(),
        })
        .sum()
}
fn part_2(data: &str) -> u64 {
    parse_input(data)
        .iter()
        .map(|(op, values)| match op {
            '+' => parse_rl_tb(values).iter().sum::<u64>(),
            '*' => parse_rl_tb(values).iter().product::<u64>(),
            _ => panic!(),
        })
        .sum()
}
fn parse_tb_lr(values: &[String]) -> impl Iterator<Item = u64> {
    values.iter().map(|v| v.trim().parse::<u64>().unwrap())
}
fn parse_rl_tb(values: &[String]) -> Vec<u64> {
    let mut result: Vec<u64> = Vec::new();
    let max_len = values.iter().map(|v| v.len()).max().unwrap();
    for col in 0..max_len {
        let mut num = String::new();
        for row in 0..values.len() {
            num += &(*values[row].as_bytes().get(col).unwrap_or(&(' ' as u8)) as char).to_string();
        }
        result.push(num.trim().parse::<u64>().unwrap())
    }
    result
}
fn parse_input(data: &str) -> Vec<(char, Vec<String>)> {
    let mut digits: Vec<&str> = data.lines().collect();
    let ops = digits.split_off(digits.len() - 1)[0];
    let mut op = '\0';
    let mut offset = 0;
    let mut size = 0;
    let mut result = Vec::new();
    for c in ops.chars() {
        match c {
            '+' | '*' => {
                if size > 0 {
                    let values = Vec::from_iter(
                        digits
                            .iter()
                            .map(|s| s[offset..offset + size - 1].to_string()),
                    );
                    result.push((op, values));
                }
                op = c;
                offset += size;
                size = 1;
            }
            ' ' => {
                size += 1;
            }
            _ => panic!("{c}"),
        }
    }
    let values = Vec::from_iter(digits.iter().map(|s| s[offset..].to_string()));
    result.push((op, values));
    result
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 4277556);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 3263827);
    }
    fn example() -> String {
        String::from(
            "
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
            ",
        )
        .trim()
        .lines()
        .map(|line| line.to_string() + "\n")
        .collect()
    }
}

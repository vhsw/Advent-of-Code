use std::fs;

fn main() {
    let data = fs::read_to_string("day_03/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> u64 {
    parse_input(data).iter().map(|bank| max(bank, 2)).sum()
}
fn part_2(data: &str) -> u64 {
    parse_input(data).iter().map(|bank| max(bank, 12)).sum()
}
fn max(bank: &[u64], n_digits: u32) -> u64 {
    if n_digits == 0 || n_digits as usize > bank.len() {
        panic!()
    }
    if n_digits == 1 {
        return *bank.iter().max().unwrap();
    }
    let max_value = bank
        .iter()
        .take(bank.len() - n_digits as usize + 1)
        .max()
        .unwrap();
    let max_index = bank.iter().position(|x| x == max_value).unwrap();
    let tail = &bank[max_index + 1..];
    max_value * 10_u64.pow(n_digits - 1) + max(tail, n_digits - 1)
}
fn parse_input(data: &str) -> Vec<Vec<u64>> {
    let mut result = Vec::new();
    for line in data.lines() {
        let bank = line
            .chars()
            .map(|c| c.to_digit(10).unwrap().into())
            .collect();
        result.push(bank);
    }
    result
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 357);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 3121910778619);
    }
    fn example() -> String {
        String::from(
            "
            987654321111111
            811111111111119
            234234234234278
            818181911112111
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

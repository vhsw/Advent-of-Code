use std::collections::HashMap;
use std::fs;

fn main() {
    let data = fs::read_to_string("day_19/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let (patterns, designs) = parse_input(data);
    designs.iter().filter(|d| is_possible(d, &patterns)).count()
}
fn part_2(data: &str) -> usize {
    let (patterns, designs) = parse_input(data);
    let mut memo = HashMap::new();
    designs
        .iter()
        .map(|d| count_arrangements(d, &patterns, &mut memo))
        .sum()
}
fn parse_input(data: &str) -> (Vec<String>, Vec<String>) {
    let (patterns, designs) = data.split_once("\n\n").unwrap();
    (
        patterns.split(", ").map(|s| s.to_string()).collect(),
        designs.trim().split('\n').map(|s| s.to_string()).collect(),
    )
}
fn is_possible(design: &str, patterns: &[String]) -> bool {
    if design.is_empty() {
        return true;
    }
    for pattern in patterns.iter() {
        if design.starts_with(pattern) && is_possible(&design[pattern.len()..], patterns) {
            return true;
        }
    }
    false
}
fn count_arrangements(
    design: &str,
    patterns: &[String],
    memo: &mut HashMap<String, usize>,
) -> usize {
    if design.is_empty() {
        return 1;
    }
    if let Some(&count) = memo.get(design) {
        return count;
    }
    let mut count = 0;
    for pattern in patterns.iter() {
        if design.starts_with(pattern) {
            count += count_arrangements(&design[pattern.len()..], patterns, memo);
        }
    }
    memo.insert(design.to_string(), count);
    count
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 6);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 16);
    }
    fn example() -> String {
        String::from(
            "
            r, wr, b, g, bwu, rb, gb, br

            brwrr
            bggr
            gbbr
            rrbgbr
            ubwu
            bwurrg
            brgr
            bbrgwb
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

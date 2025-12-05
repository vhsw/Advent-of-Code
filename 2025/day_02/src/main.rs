use std::cmp;
use std::collections::HashSet;
use std::fs;
fn main() {
    let data = fs::read_to_string("day_02/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}

fn part_1(data: &str) -> u64 {
    let ranges = parse_input(data);
    ranges
        .iter()
        .map(|(lower, upper)| find_repeat_once(lower, upper))
        .sum()
}
fn part_2(data: &str) -> u64 {
    let ranges = parse_input(data);
    ranges
        .iter()
        .map(|(lower, upper)| find_repeat_multiple(lower, upper))
        .sum()
}
fn find_repeat_once(lower: &str, upper: &str) -> u64 {
    let size = cmp::max(lower.len() / 2, 1);
    let mut part_id: u64 = lower[0..size].parse().unwrap();
    let start: u64 = lower.parse().unwrap();
    let end: u64 = upper.parse().unwrap();
    let mut sum = 0;
    loop {
        let id: u64 = (part_id.to_string() + &part_id.to_string())
            .parse()
            .unwrap();
        if id >= start && id <= end {
            sum += id;
        }
        if id > end {
            break;
        }
        part_id += 1;
    }
    sum
}
fn find_repeat_multiple(lower: &str, upper: &str) -> u64 {
    let start: u64 = lower.parse().unwrap();
    let end: u64 = upper.parse().unwrap();
    let mut result = HashSet::new();
    for id in start..end + 1 {
        let str_id = id.to_string();
        for size in 1..(str_id.len() / 2) + 1 {
            if (str_id.len() % size) != 0 {
                continue;
            }
            let repeats = str_id.len() / size;
            let part = &str_id[0..size];
            if part.repeat(repeats) == str_id {
                result.insert(id);
            }
        }
    }
    result.iter().sum()
}
fn parse_input(data: &str) -> Vec<(&str, &str)> {
    let mut result = Vec::new();
    for range in data.split(',') {
        let vec: Vec<&str> = range.split('-').collect();
        result.push((vec[0], vec[1].trim()))
    }
    result
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 1227775554);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 4174379265);
    }
    fn example() -> String {
        String::from(
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

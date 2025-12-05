use std::{cmp::max, fs};

fn main() {
    let data = fs::read_to_string("day_05/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let (ranges, ids) = parse_input(data);
    ids.iter()
        .filter(|id| {
            ranges
                .iter()
                .any(|(lower, upper)| lower <= id && id <= &upper)
        })
        .count()
}
fn part_2(data: &str) -> u64 {
    let (mut ranges, _) = parse_input(data);
    ranges.sort();

    let mut merged_ranges = Vec::new();
    merged_ranges.push(ranges[0]);
    for range in ranges {
        let last_index = merged_ranges.len() - 1;
        let current_end = merged_ranges.get_mut(last_index).unwrap();
        if range.0 <= current_end.1 {
            current_end.1 = max(current_end.1, range.1);
            continue;
        }
        merged_ranges.push(range);
    }
    merged_ranges
        .iter()
        .map(|(lower, upper)| upper - lower + 1)
        .sum()
}
fn parse_input(data: &str) -> (Vec<(u64, u64)>, Vec<u64>) {
    let split: Vec<&str> = data.split("\n\n").collect();

    let mut ranges = Vec::new();
    for line in split[0].lines() {
        let range: Vec<&str> = line.split('-').collect();
        ranges.push((range[0].parse().unwrap(), range[1].parse().unwrap()));
    }
    let mut ids = Vec::new();
    for line in split[1].lines() {
        ids.push(line.parse().unwrap());
    }
    (ranges, ids)
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 3);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 14);
    }
    fn example() -> String {
        String::from(
            "
            3-5
            10-14
            16-20
            12-18

            1
            5
            8
            11
            17
            32
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

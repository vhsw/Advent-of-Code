use std::{collections::HashMap, fs};

fn main() {
    let data = fs::read_to_string("day_01/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}

fn part_1(data: &String) -> u32 {
    let (mut left, mut right) = get_lists(data);
    left.sort();
    right.sort();
    return left
        .iter()
        .zip(right.iter())
        .map(|(a, b)| a.abs_diff(*b))
        .sum();
}
fn get_lists(data: &String) -> (Vec<u32>, Vec<u32>) {
    let mut left: Vec<u32> = Vec::new();
    let mut right: Vec<u32> = Vec::new();
    for line in data.lines() {
        let mut it = line.split_whitespace();
        left.push(it.next().unwrap().parse().unwrap());
        right.push(it.next().unwrap().parse().unwrap());
    }
    return (left, right);
}
fn part_2(data: &String) -> u32 {
    let (left, right) = get_lists(data);
    let mut counter: HashMap<u32, u32> = HashMap::new();
    for key in right.iter() {
        counter
            .entry(*key)
            .and_modify(|count| *count += 1)
            .or_insert(1);
    }

    return left
        .iter()
        .map(|item| item * counter.get(item).unwrap_or(&0))
        .sum();
}

#[cfg(test)]
mod tests {
    use super::*;
    fn example() -> String {
        return String::from(
            "
            3   4
            4   3
            2   5
            1   3
            3   9
            3   3
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect();
    }

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 11);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 31);
    }
}

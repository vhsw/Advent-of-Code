use std::{collections::HashMap, fs};
fn main() {
    let data = fs::read_to_string("day_11/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data, 25));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str, steps: usize) -> usize {
    let stones = get_stones(data);
    let mut memory = HashMap::new();
    stones
        .iter()
        .map(|stone| change_stone(*stone, steps, &mut memory))
        .sum()
}
fn part_2(data: &str) -> usize {
    part_1(data, 75)
}
fn get_stones(data: &str) -> Vec<usize> {
    data.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect()
}
fn change_stone(stone: usize, steps: usize, memory: &mut HashMap<(usize, usize), usize>) -> usize {
    if steps == 0 {
        return 1;
    }
    if let Some(size) = memory.get(&(stone, steps)) {
        return *size;
    }
    let mut size = 0;
    for stone in step(stone) {
        size += change_stone(stone, steps - 1, memory);
    }
    memory.insert((stone, steps), size);
    size
}
fn step(stone: usize) -> Vec<usize> {
    let mut new_stones = Vec::new();
    if stone == 0 {
        new_stones.push(1);
        return new_stones;
    }
    let label = stone.to_string();
    if label.len() % 2 == 0 {
        new_stones.push(label[..label.len() / 2].parse().unwrap());
        new_stones.push(label[label.len() / 2..].parse().unwrap());
    } else {
        new_stones.push(stone * 2024);
    }
    new_stones
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example(), 1), 7);
        assert_eq!(part_1(&larger_example(), 6), 22);
        assert_eq!(part_1(&larger_example(), 25), 55312);
    }
    fn example() -> String {
        String::from("0 1 10 99 999")
    }
    fn larger_example() -> String {
        String::from("125 17")
    }
}

use std::{collections::HashSet, fs};

fn main() {
    let data = fs::read_to_string("day_04/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let grid = parse_input(data);
    grid.iter()
        .filter(|roll| is_accessable(**roll, &grid))
        .count()
}
fn part_2(data: &str) -> usize {
    let mut grid = parse_input(data);
    let mut count = 0;
    loop {
        let new_grid = HashSet::from_iter(
            grid.iter()
                .filter(|roll| !is_accessable(**roll, &grid))
                .cloned(),
        );
        count += grid.len() - new_grid.len();
        if grid.len() == new_grid.len() {
            return count;
        }
        grid = new_grid;
    }
}
fn is_accessable((row, col): (i32, i32), grid: &HashSet<(i32, i32)>) -> bool {
    let mut count = 0;
    for d_row in [-1, 0, 1] {
        for d_col in [-1, 0, 1] {
            if d_row == 0 && d_col == 0 {
                continue;
            }
            if grid.contains(&(row + d_row, col + d_col)) {
                if count == 3 {
                    return false;
                }
                count += 1;
            }
        }
    }
    true
}

fn parse_input(data: &str) -> HashSet<(i32, i32)> {
    let mut result = HashSet::new();
    for (row, line) in data.lines().enumerate() {
        for (col, c) in line.chars().enumerate() {
            if c == '@' {
                result.insert((row as i32, col as i32));
            }
        }
    }
    result
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 13);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 43);
    }
    fn example() -> String {
        String::from(
            "
            ..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

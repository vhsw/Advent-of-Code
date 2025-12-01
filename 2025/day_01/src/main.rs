use std::fs;

fn main() {
    let data = fs::read_to_string("day_01/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}

fn part_1(data: &str) -> u32 {
    let instructions = parse_input(data);
    let mut dial = 50;
    let mut zeros = 0;
    for (dir, val) in instructions {
        match dir {
            'L' => dial = dial - val,
            'R' => dial = dial + val,
            _ => panic!("Unknown direction: {}", dir),
        }
        dial = dial.rem_euclid(100);
        if dial == 0 {
            zeros += 1;
        }
    }
    zeros
}
fn part_2(data: &str) -> u32 {
    let instructions = parse_input(data);
    let mut dial: i32 = 50;
    let mut zeros = 0;
    for (dir, val) in instructions {
        // CPU goes brrrrrr
        for _ in 0..val {
            match dir {
                'L' => dial = dial - 1,
                'R' => dial = dial + 1,
                _ => panic!("Unknown direction: {}", dir),
            }
            dial = dial.rem_euclid(100);
            if dial == 0 {
                zeros += 1;
            }
        }
    }
    zeros
}
fn parse_input(data: &str) -> Vec<(char, i32)> {
    let mut result = Vec::new();
    for line in data.lines() {
        let dir = line.chars().nth(0).unwrap();
        let val = line[1..].parse().unwrap();
        result.push((dir, val))
    }
    result
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
        assert_eq!(part_2(&example()), 6);
    }
    fn example() -> String {
        String::from(
            "
            L68
            L30
            R48
            L5
            R60
            L55
            L1
            L99
            R14
            L82
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

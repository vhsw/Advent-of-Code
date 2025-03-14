use std::fs;

fn main() {
    let data = fs::read_to_string("day_25/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
}
fn part_1(data: &str) -> usize {
    let (locks, keys) = parse_input(data);
    let mut count = 0;
    for lock in locks.iter() {
        for key in keys.iter() {
            if lock.iter().zip(key.iter()).any(|(l, k)| l + k > 5) {
                continue;
            }
            count += 1;
        }
    }
    count
}
type Heights = [usize; 5];
fn parse_input(data: &str) -> (Vec<Heights>, Vec<Heights>) {
    let mut locks = Vec::new();
    let mut keys = Vec::new();
    data.trim().split("\n\n").for_each(|schematic| {
        let heights = get_heights(schematic);
        match schematic.chars().next() {
            Some('#') => locks.push(heights),
            Some('.') => keys.push(heights),
            _ => panic!("Invalid schematic: '{schematic}'"),
        }
    });
    (locks, keys)
}
fn get_heights(schematic: &str) -> Heights {
    let mut heights = [0; 5];
    schematic.lines().for_each(|line| {
        line.chars().enumerate().for_each(|(i, c)| {
            if c == '#' {
                heights[i] += 1;
            }
        })
    });
    heights.iter_mut().for_each(|height| *height -= 1);
    heights
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 3);
    }
    fn example() -> String {
        String::from(
            "
            #####
            .####
            .####
            .####
            .#.#.
            .#...
            .....

            #####
            ##.##
            .#.##
            ...##
            ...#.
            ...#.
            .....

            .....
            #....
            #....
            #...#
            #.#.#
            #.###
            #####

            .....
            .....
            #.#..
            ###..
            ###.#
            ###.#
            #####

            .....
            .....
            .....
            #....
            #.#..
            #.#.#
            #####
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

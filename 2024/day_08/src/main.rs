use std::ops;
use std::{collections::HashSet, fs};
fn main() {
    let data = fs::read_to_string("day_08/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let (antennas, bounds) = parse_input(data);
    let mut antiodes = HashSet::new();
    for (i, a) in antennas.iter().enumerate() {
        for b in antennas.iter().skip(i + 1) {
            get_antinodes(a, b)
                .iter()
                .filter(|pos| in_bounds(pos, &bounds))
                .for_each(|antinode| {
                    antiodes.insert(*antinode);
                });
        }
    }
    antiodes.len()
}
fn part_2(data: &str) -> usize {
    let (antennas, bounds) = parse_input(data);
    let mut antiodes = HashSet::new();
    for (i, a) in antennas.iter().enumerate() {
        for b in antennas.iter().skip(i + 1) {
            get_antinodes_2(a, b, &bounds).iter().for_each(|antinode| {
                antiodes.insert(*antinode);
            });
        }
    }
    antiodes.len()
}
fn parse_input(data: &str) -> (Vec<Antenna>, Vec2D) {
    let antennas = read_antennas(data);
    let bounds = Vec2D {
        row: data.lines().count() as isize,
        col: data.lines().next().unwrap().chars().count() as isize,
    };
    (antennas, bounds)
}
fn get_antinodes(a: &Antenna, b: &Antenna) -> Vec<Vec2D> {
    if a.frequency != b.frequency {
        return vec![];
    }
    let diff = a.pos - b.pos;
    vec![a.pos + diff, b.pos - diff]
}
fn in_bounds(pos: &Vec2D, bounds: &Vec2D) -> bool {
    pos.row >= 0 && pos.row < bounds.row && pos.col >= 0 && pos.col < bounds.col
}
fn get_antinodes_2(a: &Antenna, b: &Antenna, bounds: &Vec2D) -> Vec<Vec2D> {
    let mut result = Vec::new();
    let mut a = a.clone();
    let mut b = b.clone();
    if a.frequency != b.frequency {
        return result;
    }
    let diff = a.pos - b.pos;
    while in_bounds(&a.pos, bounds) {
        result.push(a.pos);
        a.pos = a.pos + diff;
    }
    while in_bounds(&b.pos, bounds) {
        result.push(b.pos);
        b.pos = b.pos - diff;
    }
    result
}
#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
struct Vec2D {
    row: isize,
    col: isize,
}
impl ops::Add for Vec2D {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self {
            row: self.row + other.row,
            col: self.col + other.col,
        }
    }
}
impl ops::Sub for Vec2D {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        Self {
            row: self.row - other.row,
            col: self.col - other.col,
        }
    }
}
#[derive(Clone, Debug)]
struct Antenna {
    frequency: char,
    pos: Vec2D,
}
fn read_antennas(data: &str) -> Vec<Antenna> {
    data.lines()
        .enumerate()
        .flat_map(|(row, line)| {
            line.chars()
                .enumerate()
                .filter(|(_, c)| *c != '.')
                .map(|(col, c)| Antenna {
                    frequency: c,
                    pos: Vec2D {
                        row: row as isize,
                        col: col as isize,
                    },
                })
                .collect::<Vec<_>>()
        })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 14);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 34);
    }
    fn example() -> String {
        String::from(
            "
            ............
            ........0...
            .....0......
            .......0....
            ....0.......
            ......A.....
            ............
            ............
            ........A...
            .........A..
            ............
            ............
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

use std::{collections::HashSet, fs};
fn main() {
    let data = fs::read_to_string("day_10/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let map = parse_input(data);
    get_trailheads(&map)
        .iter()
        .map(|trailhead| get_score(trailhead, &map))
        .sum()
}
fn part_2(data: &str) -> usize {
    let map = parse_input(data);
    get_trailheads(&map)
        .iter()
        .map(|trailhead| get_rating(trailhead, &map))
        .sum()
}
fn parse_input(data: &str) -> Vec<Vec<u32>> {
    data.lines()
        .map(|line| line.chars().map(|c| c.to_digit(10).unwrap()).collect())
        .collect()
}
fn get_trailheads(map: &[Vec<u32>]) -> Vec<(usize, usize)> {
    let mut trailheads = Vec::new();
    for (i, row) in map.iter().enumerate() {
        for (j, &val) in row.iter().enumerate() {
            if val == 0 {
                trailheads.push((i, j));
            }
        }
    }
    trailheads
}
fn get_score(trailhead: &(usize, usize), map: &[Vec<u32>]) -> usize {
    fn travel(pos: &(usize, usize), map: &[Vec<u32>]) -> HashSet<(usize, usize)> {
        let height = map[pos.0][pos.1];
        let mut tails = HashSet::new();
        if height == 9 {
            tails.insert(*pos);
            return tails;
        }
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        for (dx, dy) in dirs.iter() {
            let x = pos.0.checked_add_signed(*dx);
            let y = pos.1.checked_add_signed(*dy);
            if x.is_none() || y.is_none() {
                continue;
            }
            let x = x.unwrap();
            let y = y.unwrap();
            if x >= map.len() || y >= map[0].len() {
                continue;
            }
            if map[x][y] != height + 1 {
                continue;
            }
            tails.extend(travel(&(x, y), map));
        }
        tails
    }
    travel(trailhead, map).len()
}
fn get_rating(trailhead: &(usize, usize), map: &[Vec<u32>]) -> usize {
    fn travel(pos: &(usize, usize), map: &[Vec<u32>], count: usize) -> usize {
        let height = map[pos.0][pos.1];
        if height == 9 {
            return count + 1;
        }
        let mut count = count;
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        for (dx, dy) in dirs.iter() {
            let x = pos.0.checked_add_signed(*dx);
            let y = pos.1.checked_add_signed(*dy);
            if x.is_none() || y.is_none() {
                continue;
            }
            let x = x.unwrap();
            let y = y.unwrap();
            if x >= map.len() || y >= map[0].len() {
                continue;
            }
            if map[x][y] != height + 1 {
                continue;
            }
            count += travel(&(x, y), map, 0);
        }
        count
    }
    travel(trailhead, map, 0)
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 1);
        assert_eq!(part_1(&larger_example()), 36);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&larger_example()), 81);
    }
    fn example() -> String {
        String::from(
            "
            0123
            1234
            8765
            9876
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn larger_example() -> String {
        String::from(
            "
            89010123
            78121874
            87430965
            96549874
            45678903
            32019012
            01329801
            10456732
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

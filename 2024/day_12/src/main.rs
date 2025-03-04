use std::{collections::HashSet, fs};
fn main() {
    let data = fs::read_to_string("day_12/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let map = parse_input(data);
    divide_map(&map)
        .iter()
        .map(|region| region.borders * region.plots.len())
        .sum()
}
fn part_2(data: &str) -> usize {
    let map = parse_input(data);
    divide_map(&map)
        .iter()
        .map(|region| count_sides(region) * region.plots.len())
        .sum()
}
fn parse_input(data: &str) -> Vec<Vec<char>> {
    data.lines().map(|line| line.chars().collect()).collect()
}
#[derive(Debug)]
struct Region {
    plots: HashSet<(isize, isize)>,
    borders: usize,
}
fn divide_map(map: &[Vec<char>]) -> Vec<Region> {
    let mut regions = vec![];
    let mut seen = HashSet::<(isize, isize)>::new();
    for (x, row) in map.iter().enumerate() {
        for (y, _) in row.iter().enumerate() {
            if seen.contains(&(x as isize, y as isize)) {
                continue;
            }
            let region = explore_map(map, (x as isize, y as isize));
            seen.extend(region.plots.iter());
            regions.push(region);
        }
    }

    regions
}
fn explore_map(map: &[Vec<char>], start: (isize, isize)) -> Region {
    let mut plots = HashSet::new();
    let mut stack = vec![(start.0, start.1)];
    let id = map[start.0 as usize][start.1 as usize];
    let mut borders = 0;
    while let Some((x, y)) = stack.pop() {
        if x < 0 || y < 0 || x as usize >= map.len() || y as usize >= map[0].len() {
            borders += 1;
            continue;
        }
        if map[x as usize][y as usize] != id {
            borders += 1;
            continue;
        }
        if plots.contains(&(x, y)) {
            continue;
        }
        plots.insert((x, y));
        for &(dx, dy) in &[(0, 1), (1, 0), (0, -1), (-1, 0)] {
            stack.push((x + dx, y + dy));
        }
    }
    Region { plots, borders }
}
fn count_sides(region: &Region) -> usize {
    let mut corners = 0;
    for (x, y) in region.plots.iter() {
        for [a, b, c] in &[
            [(1, 0), (1, 1), (0, 1)],
            [(-1, 0), (-1, -1), (0, -1)],
            [(1, 0), (1, -1), (0, -1)],
            [(-1, 0), (-1, 1), (0, 1)],
        ] {
            let side_a = region.plots.contains(&(x + a.0, y + a.1));
            let middle = region.plots.contains(&(x + b.0, y + b.1));
            let side_b = region.plots.contains(&(x + c.0, y + c.1));
            if middle && (side_a || side_b) {
                continue;
            }
            if side_a != side_b {
                continue;
            }
            corners += 1;
        }
    }
    corners
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 140);
        assert_eq!(part_1(&second_example()), 772);
        assert_eq!(part_1(&larger_example()), 1930);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 80);
        assert_eq!(part_2(&larger_example()), 1206);
        assert_eq!(part_2(&second_example()), 436);
        assert_eq!(part_2(&e_xample()), 236);
        assert_eq!(part_2(&ab_example()), 368);
    }
    fn example() -> String {
        String::from(
            "
            AAAA
            BBCD
            BBCC
            EEEC
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn second_example() -> String {
        String::from(
            "
            OOOOO
            OXOXO
            OOOOO
            OXOXO
            OOOOO
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
            RRRRIICCFF
            RRRRIICCCF
            VVRRRCCFFF
            VVRCCCJFFF
            VVVVCJJCFE
            VVIVCCJJEE
            VVIIICJJEE
            MIIIIIJJEE
            MIIISIJEEE
            MMMISSJEEE
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn e_xample() -> String {
        String::from(
            "
            EEEEE
            EXXXX
            EEEEE
            EXXXX
            EEEEE
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn ab_example() -> String {
        String::from(
            "
            AAAAAA
            AAABBA
            AAABBA
            ABBAAA
            ABBAAA
            AAAAAA
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

use std::{collections::HashSet, fs};

fn main() {
    let data = fs::read_to_string("day_06/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let grid = parse_input(data);
    let pos = find_guard(&grid);
    let dir = (-1, 0);
    let path = find_path(pos, dir, &grid);
    path.len()
}
fn part_2(data: &str) -> usize {
    let grid = parse_input(data);
    let pos = find_guard(&grid);
    let dir = (-1, 0);
    let path = find_path(pos, dir, &grid);

    let mut count = 0;
    for (row, col) in path.iter() {
        if *row == pos.0 && *col == pos.1 {
            continue;
        }
        let mut new_grid = grid.clone();
        new_grid[*row as usize][*col as usize] = '#';
        if will_stuck(pos, dir, &new_grid) {
            count += 1;
        }
    }
    count
}
fn parse_input(data: &str) -> Vec<Vec<char>> {
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in data.lines() {
        let chars = line.chars().collect();
        grid.push(chars);
    }
    grid
}
fn find_guard(grid: &[Vec<char>]) -> (isize, isize) {
    grid.iter()
        .enumerate()
        .find_map(|(i, row)| {
            row.iter().enumerate().find_map(|(j, &c)| match c {
                '^' => Some((i as isize, j as isize)),
                _ => None,
            })
        })
        .unwrap()
}
fn find_path(
    pos: (isize, isize),
    dir: (isize, isize),
    grid: &[Vec<char>],
) -> HashSet<(isize, isize)> {
    let mut pos = pos;
    let mut dir = dir;
    let mut seen = HashSet::new();
    loop {
        seen.insert(pos);
        let new_pos = (pos.0 + dir.0, pos.1 + dir.1);
        if new_pos.0 < 0
            || new_pos.1 < 0
            || new_pos.0 >= grid.len() as isize
            || new_pos.1 >= grid[0].len() as isize
        {
            break;
        }
        if grid[new_pos.0 as usize][new_pos.1 as usize] == '#' {
            dir = (dir.1, -dir.0);
            continue;
        }
        pos = new_pos;
    }
    seen
}
fn will_stuck(pos: (isize, isize), dir: (isize, isize), grid: &[Vec<char>]) -> bool {
    let mut pos = pos;
    let mut dir = dir;
    let mut seen = HashSet::new();
    loop {
        if seen.contains(&(pos, dir)) {
            return true;
        }
        seen.insert((pos, dir));
        let new_pos = (pos.0 + dir.0, pos.1 + dir.1);
        if new_pos.0 < 0
            || new_pos.1 < 0
            || new_pos.0 >= grid.len() as isize
            || new_pos.1 >= grid[0].len() as isize
        {
            return false;
        }
        if grid[new_pos.0 as usize][new_pos.1 as usize] == '#' {
            dir = (dir.1, -dir.0);
            continue;
        }
        pos = new_pos;
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 41);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 6);
    }
    fn example() -> String {
        String::from(
            "
            ....#.....
            .........#
            ..........
            ..#.......
            .......#..
            ..........
            .#..^.....
            ........#.
            #.........
            ......#...
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

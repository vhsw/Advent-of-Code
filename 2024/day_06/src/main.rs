use std::{collections::HashSet, fs};

fn main() {
    let data = fs::read_to_string("day_06/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &String) -> usize {
    let grid = make_grid(data);
    let (mut guard_pos, mut guard_dir) = find_guard(&grid);
    let mut seen = HashSet::new();
    loop {
        seen.insert(guard_pos);
        let new_pos = (guard_pos.0 + guard_dir.0, guard_pos.1 + guard_dir.1);
        if new_pos.0 < 0
            || new_pos.1 < 0
            || new_pos.0 >= grid.len() as isize
            || new_pos.1 >= grid[0].len() as isize
        {
            break;
        }
        if grid[new_pos.0 as usize][new_pos.1 as usize] == '#' {
            guard_dir = (guard_dir.1, -guard_dir.0);
            continue;
        }
        guard_pos = new_pos;
    }
    seen.len()
}
fn part_2(data: &String) -> usize {
    let grid = make_grid(data);
    let (guard_pos, guard_dir) = find_guard(&grid);
    let mut count = 0;
    for row in 0..grid.len() {
        for col in 0..grid[row].len() {
            if row == guard_pos.0 as usize && col == guard_pos.1 as usize {
                continue;
            }
            let mut new_grid = grid.clone();
            new_grid[row][col] = '#';
            if will_stuck(guard_pos, guard_dir, &new_grid) {
                count += 1;
            }
        }
    }
    count
}
fn will_stuck(pos: (isize, isize), dir: (isize, isize), grid: &Vec<Vec<char>>) -> bool {
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

fn make_grid(data: &String) -> Vec<Vec<char>> {
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in data.lines() {
        let chars = line.chars().collect();
        grid.push(chars);
    }
    grid
}
fn find_guard(grid: &Vec<Vec<char>>) -> ((isize, isize), (isize, isize)) {
    for row in 0..grid.len() {
        for col in 0..grid[row].len() {
            match grid[row][col] {
                '^' => return ((row as isize, col as isize), (-1, 0)),
                'v' => return ((row as isize, col as isize), (1, 0)),
                '>' => return ((row as isize, col as isize), (0, 1)),
                '<' => return ((row as isize, col as isize), (0, -1)),
                _ => continue,
            }
        }
    }
    panic!("Guard not found")
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
        return String::from(
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
        .collect();
    }
}

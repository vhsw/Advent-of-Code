use std::{
    collections::{HashMap, HashSet},
    fs,
};

fn main() {
    let data = fs::read_to_string("day_07/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let (src, grid, size) = parse_input(data);
    let mut beams = HashSet::new();
    beams.insert(src);
    let mut splits = 0;
    for _ in 0..size {
        let mut new_beams = HashSet::new();
        for beam in &beams {
            let new_beam = (beam.0 + 1, beam.1);
            if grid.contains(&new_beam) {
                new_beams.insert((new_beam.0, new_beam.1 - 1));
                new_beams.insert((new_beam.0, new_beam.1 + 1));
                splits += 1;
            } else {
                new_beams.insert(new_beam);
            }
        }
        beams = new_beams;
    }
    splits
}
fn part_2(data: &str) -> usize {
    let (src, grid, size) = parse_input(data);
    let mut memo = HashMap::new();
    count_pathes(src, &grid, 1, size, &mut memo)
}
fn count_pathes(
    beam: (i32, i32),
    grid: &HashSet<(i32, i32)>,
    step: usize,
    max_step: usize,
    memo: &mut HashMap<(i32, i32), usize>,
) -> usize {
    if step >= max_step {
        return 1;
    }

    if memo.contains_key(&beam) {
        return *memo.get(&beam).unwrap();
    }
    let new_beam = (beam.0 + 1, beam.1);
    let count = match grid.contains(&new_beam) {
        false => count_pathes(new_beam, grid, step + 1, max_step, memo),
        true => {
            count_pathes((new_beam.0, new_beam.1 - 1), grid, step + 1, max_step, memo)
                + count_pathes((new_beam.0, new_beam.1 + 1), grid, step + 1, max_step, memo)
        }
    };
    memo.insert(beam, count);
    count
}
fn parse_input(data: &str) -> ((i32, i32), HashSet<(i32, i32)>, usize) {
    let mut src = None;
    let mut grid = HashSet::new();
    for (row, line) in data.lines().enumerate() {
        for (col, chr) in line.chars().enumerate() {
            match chr {
                '.' => continue,
                'S' => {
                    src = Some((row as i32, col as i32));
                }
                '^' => {
                    grid.insert((row as i32, col as i32));
                }
                _ => panic!("{row}, {col}, {chr}"),
            }
        }
    }
    (src.unwrap(), grid, data.lines().count())
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 21);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 40);
    }
    fn example() -> String {
        String::from(
            "
            .......S.......
            ...............
            .......^.......
            ...............
            ......^.^......
            ...............
            .....^.^.^.....
            ...............
            ....^.^...^....
            ...............
            ...^.^...^.^...
            ...............
            ..^...^.....^..
            ...............
            .^.^.^.^.^...^.
            ...............
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

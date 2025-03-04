use regex::Regex;
use std::{collections::HashSet, fs};

fn main() {
    let data = fs::read_to_string("day_14/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    solve(data, 100, 101, 103)
}
fn part_2(data: &str) -> usize {
    let mut robots = parse_input(data);
    let room_cols = 101;
    let room_rows = 103;
    let mut step = 0;
    let mut mem = HashSet::new();
    mem.insert(robots.clone());
    loop {
        make_step(&mut robots, room_cols, room_rows);
        if mem.contains(&robots) {
            panic!("Cycle detected at step {}", step);
        }
        mem.insert(robots.clone());
        step += 1;
        let lookup: HashSet<(isize, isize)> =
            HashSet::from_iter(robots.iter().map(|r| (r.pos.col, r.pos.row)));
        if lookup.len() != robots.len() {
            continue;
        }
        // println!("Step {step}");
        // let text: String = (0..room_rows)
        //     .map(|row| {
        //         (0..room_cols)
        //             .map(|col| {
        //                 if lookup.contains(&(col, row)) {
        //                     '#'
        //                 } else {
        //                     ' '
        //                 }
        //             })
        //             .collect()
        //     })
        //     .collect::<Vec<String>>()
        //     .join("\n");
        // println!("{text}\n");
        return step;
    }
}
fn solve(data: &str, steps: usize, room_cols: isize, room_rows: isize) -> usize {
    let mut robots = parse_input(data);
    for _ in 0..steps {
        make_step(&mut robots, room_cols, room_rows);
    }
    safety_factor(&robots, room_cols, room_rows)
}
fn make_step(robots: &mut [Robot], room_cols: isize, room_rows: isize) {
    for robot in robots.iter_mut() {
        robot.pos.col = (robot.pos.col + robot.vel.col).rem_euclid(room_cols);
        robot.pos.row = (robot.pos.row + robot.vel.row).rem_euclid(room_rows);
    }
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
struct Vec2D {
    col: isize,
    row: isize,
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
struct Robot {
    pos: Vec2D,
    vel: Vec2D,
}
fn parse_input(data: &str) -> Vec<Robot> {
    let re = Regex::new(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)").unwrap();
    data.lines()
        .map(|line| {
            let caps = re.captures(line).unwrap();
            Robot {
                pos: Vec2D {
                    col: caps[1].parse().unwrap(),
                    row: caps[2].parse().unwrap(),
                },
                vel: Vec2D {
                    col: caps[3].parse().unwrap(),
                    row: caps[4].parse().unwrap(),
                },
            }
        })
        .collect()
}
fn safety_factor(robots: &[Robot], room_cols: isize, room_rows: isize) -> usize {
    let quad_cols = room_cols / 2;
    let quad_rows = room_rows / 2;
    let mut quad_counts = [0; 4];
    for robot in robots.iter() {
        let pos = &robot.pos;
        for (i, ((min_col, max_col), (min_row, max_row))) in [
            ((0, quad_cols), (0, quad_rows)),
            ((0, quad_cols), (quad_rows + 1, room_rows)),
            ((quad_cols + 1, room_cols), (0, quad_rows)),
            ((quad_cols + 1, room_cols), (quad_rows + 1, room_rows)),
        ]
        .iter()
        .enumerate()
        {
            if pos.col >= *min_col
                && pos.col < *max_col
                && pos.row >= *min_row
                && pos.row < *max_row
            {
                quad_counts[i] += 1;
                break;
            }
        }
    }
    quad_counts.iter().product()
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        // assert_eq!(solve("p=2,4 v=2,-3", 5, 11, 7), 12);
        assert_eq!(solve(&example(), 100, 11, 7), 12);
    }
    // #[test]
    // fn test_part_2() {
    //     assert_eq!(part_2(&example()), 80);
    // }
    fn example() -> String {
        String::from(
            "
            p=0,4 v=3,-3
            p=6,3 v=-1,-3
            p=10,3 v=-1,2
            p=2,0 v=2,-1
            p=0,0 v=1,3
            p=3,0 v=-2,-2
            p=7,6 v=-1,-3
            p=3,0 v=-1,-2
            p=9,3 v=2,3
            p=7,3 v=-1,2
            p=2,4 v=2,-3
            p=9,5 v=-3,-3
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

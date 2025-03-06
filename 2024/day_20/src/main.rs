use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet};
use std::fs;
use std::ops;

fn main() {
    let data = fs::read_to_string("day_20/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    count_cheats(data, 100, 2)
}
fn part_2(data: &str) -> usize {
    count_cheats(data, 100, 20)
}
fn count_cheats(data: &str, min_save: isize, max_duration: isize) -> usize {
    let (walls, src, dst) = parse_input(data);
    let path = astar(&walls, src, dst);
    let mut count = 0;
    for (i, src) in path.iter().enumerate() {
        for (j, dst) in path.iter().enumerate().skip(i + 1) {
            let cheat_len = heuristic(src, dst);
            if cheat_len <= max_duration && (j - i) as isize >= min_save + cheat_len {
                count += 1;
            }
        }
    }
    count
}
fn parse_input(data: &str) -> (HashSet<Vec2D>, Vec2D, Vec2D) {
    let mut walls = HashSet::new();
    let mut src = None;
    let mut dst = None;
    data.lines().enumerate().for_each(|(row, line)| {
        line.chars().enumerate().for_each(|(col, c)| {
            let pos = Vec2D {
                row: row as isize,
                col: col as isize,
            };
            match c {
                'S' => {
                    src = Some(pos);
                }
                'E' => {
                    dst = Some(pos);
                }
                '#' => {
                    walls.insert(pos);
                }
                _ => {}
            };
        })
    });
    (walls, src.unwrap(), dst.unwrap())
}
fn astar(walls: &HashSet<Vec2D>, src: Vec2D, dst: Vec2D) -> Vec<Vec2D> {
    let mut heap = BinaryHeap::new();
    heap.push((Reverse(0), src));
    let mut cost_so_far = HashMap::new();
    cost_so_far.insert(src, 0);
    let mut came_from = HashMap::new();
    came_from.insert(src, None);
    while let Some((_, current)) = heap.pop() {
        let current_cost = *cost_so_far.get(&current).unwrap();
        if current == dst {
            let mut path = Vec::new();
            path.push(current);
            let mut current = current;
            while let Some(prev) = came_from.get(&current).unwrap() {
                path.push(*prev);
                current = *prev;
            }
            path.reverse();
            return path;
        }
        for next in neighbors(current) {
            if walls.contains(&next) {
                continue;
            }
            let new_cost = current_cost + 1;
            let best_cost_so_far = cost_so_far.get(&next);
            if best_cost_so_far.is_none() || new_cost < *best_cost_so_far.unwrap() {
                cost_so_far.insert(next, new_cost);
                let priority = new_cost + heuristic(&next, &dst);
                heap.push((Reverse(priority), next));
                came_from.insert(next, Some(current));
            }
        }
    }
    unreachable!()
}
fn neighbors(pos: Vec2D) -> [Vec2D; 4] {
    [
        pos + Vec2D { row: -1, col: 0 },
        pos + Vec2D { row: 0, col: -1 },
        pos + Vec2D { row: 1, col: 0 },
        pos + Vec2D { row: 0, col: 1 },
    ]
}
fn heuristic(src: &Vec2D, dst: &Vec2D) -> isize {
    (src.row - dst.row).abs() + (src.col - dst.col).abs()
}
#[derive(Debug, Copy, Clone, Eq, PartialEq, PartialOrd, Ord, Hash)]
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
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(count_cheats(&example(), 2, 2), 44);
        assert_eq!(count_cheats(&example(), 4, 2), 30);
        assert_eq!(count_cheats(&example(), 6, 2), 16);
        assert_eq!(count_cheats(&example(), 8, 2), 14);
        assert_eq!(count_cheats(&example(), 10, 2), 10);
        assert_eq!(count_cheats(&example(), 12, 2), 8);
        assert_eq!(count_cheats(&example(), 20, 2), 5);
        assert_eq!(count_cheats(&example(), 36, 2), 4);
        assert_eq!(count_cheats(&example(), 38, 2), 3);
        assert_eq!(count_cheats(&example(), 40, 2), 2);
        assert_eq!(count_cheats(&example(), 64, 2), 1);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(count_cheats(&example(), 50, 20,), 285);
        assert_eq!(count_cheats(&example(), 52, 20,), 253);
        assert_eq!(count_cheats(&example(), 54, 20,), 222);
        assert_eq!(count_cheats(&example(), 56, 20,), 193);
        assert_eq!(count_cheats(&example(), 58, 20,), 154);
        assert_eq!(count_cheats(&example(), 60, 20,), 129);
        assert_eq!(count_cheats(&example(), 62, 20,), 106);
        assert_eq!(count_cheats(&example(), 64, 20,), 86);
        assert_eq!(count_cheats(&example(), 66, 20,), 67);
        assert_eq!(count_cheats(&example(), 68, 20,), 55);
        assert_eq!(count_cheats(&example(), 70, 20,), 41);
        assert_eq!(count_cheats(&example(), 72, 20,), 29);
        assert_eq!(count_cheats(&example(), 74, 20,), 7);
        assert_eq!(count_cheats(&example(), 76, 20,), 3);
    }
    fn example() -> String {
        String::from(
            "
            ###############
            #...#...#.....#
            #.#.#.#.#.###.#
            #S#...#.#.#...#
            #######.#.#.###
            #######.#.#...#
            #######.#.###.#
            ###..E#...#...#
            ###.#######.###
            #...###...#...#
            #.#####.#.###.#
            #.#...#.#.#...#
            #.#.#.#.#.#.###
            #...#...#...###
            ###############
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

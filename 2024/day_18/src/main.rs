use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet};
use std::fs;
use std::ops;

fn main() {
    let data = fs::read_to_string("day_18/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    astar(data, 70, 1024).unwrap()
}
fn part_2(data: &str) -> String {
    find_cutoff(data, 70)
}
fn astar(data: &str, size: isize, limit: usize) -> Option<usize> {
    let corrupted: HashSet<Vec2D> =
        HashSet::from_iter(parse_input(data).iter().take(limit).cloned());
    let src = Vec2D { row: 0, col: 0 };
    let dst = Vec2D {
        row: size,
        col: size,
    };
    let mut heap = BinaryHeap::new();
    heap.push((Reverse(0), src));
    let mut cost_so_far = HashMap::new();
    cost_so_far.insert(src, 0);
    while let Some((_, current)) = heap.pop() {
        let current_cost = *cost_so_far.get(&current).unwrap();
        if current == dst {
            return Some(current_cost);
        }
        for next in neighbors(current) {
            if corrupted.contains(&next)
                || next.row < 0
                || next.col < 0
                || next.row > size
                || next.col > size
            {
                continue;
            }
            let new_cost = current_cost + 1;
            let best_cost_so_far = cost_so_far.get(&next);
            if best_cost_so_far.is_none() || new_cost < *best_cost_so_far.unwrap() {
                cost_so_far.insert(next, new_cost);
                let priority = new_cost + heuristic(&next, &dst);
                heap.push((Reverse(priority), next));
            }
        }
    }
    None
}
fn parse_input(data: &str) -> Vec<Vec2D> {
    data.lines()
        .map(|line| line.split_once(',').unwrap())
        .map(|(row, col)| Vec2D {
            row: row.parse().unwrap(),
            col: col.parse().unwrap(),
        })
        .collect()
}
fn neighbors(pos: Vec2D) -> Vec<Vec2D> {
    vec![
        pos + Vec2D { row: 0, col: -1 },
        pos + Vec2D { row: 0, col: 1 },
        pos + Vec2D { row: -1, col: 0 },
        pos + Vec2D { row: 1, col: 0 },
    ]
}
fn heuristic(src: &Vec2D, dst: &Vec2D) -> usize {
    ((src.row - dst.row).abs() + (src.col - dst.col).abs()) as usize
}
fn find_cutoff(data: &str, size: isize) -> String {
    let lines: Vec<&str> = data.lines().collect();
    let mut lower = 0;
    let mut upper = lines.len();
    while lower < upper {
        let limit = lower + (upper - lower) / 2;
        if astar(data, size, limit).is_none() {
            upper = limit;
            continue;
        }
        lower = limit + 1;
    }
    lines[lower - 1].to_string()
}
#[derive(Debug, PartialEq, Eq, Hash, PartialOrd, Ord, Clone, Copy)]
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
        assert_eq!(astar(&example(), 6, 12), Some(22));
    }
    #[test]
    fn test_part_2() {
        assert_eq!(find_cutoff(&example(), 6), "6,1");
    }
    fn example() -> String {
        String::from(
            "
            5,4
            4,2
            4,5
            3,0
            2,1
            6,3
            2,4
            1,5
            0,6
            3,3
            2,6
            5,1
            1,2
            5,5
            2,5
            6,5
            1,4
            0,4
            6,4
            1,1
            6,1
            1,0
            0,5
            1,6
            2,0
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

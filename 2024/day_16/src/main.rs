use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, VecDeque};
use std::ops;
use std::{collections::HashSet, fs};

fn main() {
    let data = fs::read_to_string("day_16/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> isize {
    let (nodes, src, dst) = parse_input(data);
    astar(
        &nodes,
        Node {
            pos: src,
            dir: Vec2D { row: 0, col: 1 },
        },
        dst,
    )
}
fn part_2(data: &str) -> usize {
    let (nodes, src, dst) = parse_input(data);
    ugly_astar(
        &nodes,
        Node {
            pos: src,
            dir: Vec2D { row: 0, col: 1 },
        },
        dst,
    )
    .len()
}
fn parse_input(data: &str) -> (HashSet<Vec2D>, Vec2D, Vec2D) {
    let mut nodes = HashSet::new();
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
                    nodes.insert(pos);
                }
                'E' => {
                    dst = Some(pos);
                    nodes.insert(pos);
                }
                '.' => {
                    nodes.insert(pos);
                }
                _ => {}
            };
        })
    });
    (nodes, src.unwrap(), dst.unwrap())
}
fn astar(nodes: &HashSet<Vec2D>, src: Node, dst: Vec2D) -> isize {
    let mut heap = BinaryHeap::new();
    heap.push((Reverse(0), src));
    let mut cost_so_far = HashMap::new();
    cost_so_far.insert(src, 0isize);

    while let Some((_, current)) = heap.pop() {
        let current_cost = *cost_so_far.get(&current).unwrap();
        if current.pos == dst {
            return current_cost;
        }
        for (next_cost, next) in neighbors(current) {
            if !nodes.contains(&next.pos) {
                continue;
            }
            let new_cost = current_cost + next_cost;
            let best_cost_so_far = cost_so_far.get(&next);
            if best_cost_so_far.is_none() || new_cost < *best_cost_so_far.unwrap() {
                cost_so_far.insert(next, new_cost);
                let priority = new_cost + heuristic(&next, &dst);
                heap.push((Reverse(priority), next));
            }
        }
    }
    panic!("dst {dst:?} is unreachable")
}
fn ugly_astar(nodes: &HashSet<Vec2D>, src: Node, dst: Vec2D) -> HashSet<Vec2D> {
    let mut heap = BinaryHeap::new();
    heap.push((Reverse(0), src));
    let mut cost_so_far = HashMap::new();
    cost_so_far.insert(src, 0isize);
    let mut best_path_cost = None;
    let mut all_best_path_nodes = HashSet::new();
    let mut came_from = HashMap::new();
    came_from.insert(src, HashSet::new());
    let mut end_nodes = HashSet::new();

    while let Some((_, current)) = heap.pop() {
        let current_cost = *cost_so_far.get(&current).unwrap();
        if current.pos == dst {
            if best_path_cost.is_none() {
                best_path_cost = Some(current_cost);
            }
            if current_cost > best_path_cost.unwrap() {
                break;
            }
            end_nodes.insert(current);
            continue;
        }
        for (next_cost, next) in neighbors(current) {
            if !nodes.contains(&next.pos) {
                continue;
            }
            let new_cost = current_cost + next_cost;
            let best_cost_so_far = cost_so_far.get(&next);
            if best_cost_so_far.is_none() || new_cost <= *best_cost_so_far.unwrap() {
                if best_cost_so_far.is_none() || new_cost < *best_cost_so_far.unwrap() {
                    came_from.insert(next, HashSet::from([current]));
                } else {
                    came_from.entry(next).and_modify(|v| {
                        v.insert(current);
                    });
                }
                cost_so_far.insert(next, new_cost);
                let priority = new_cost + heuristic(&next, &dst);
                heap.push((Reverse(priority), next));
            }
        }
    }
    let mut todo = VecDeque::new();
    for node in end_nodes.iter() {
        todo.push_back(*node);
    }
    while let Some(node) = todo.pop_front() {
        all_best_path_nodes.insert(node.pos);
        todo.extend(came_from.get(&node).unwrap());
    }
    all_best_path_nodes
}
fn neighbors(Node { pos, dir }: Node) -> [(isize, Node); 3] {
    [
        (
            1,
            Node {
                pos: pos + dir,
                dir,
            },
        ),
        (
            1000,
            Node {
                pos,
                dir: Vec2D {
                    row: dir.col,
                    col: -dir.row,
                },
            },
        ),
        (
            1000,
            Node {
                pos,
                dir: Vec2D {
                    row: -dir.col,
                    col: dir.row,
                },
            },
        ),
    ]
}
fn heuristic(Node { pos, dir: _ }: &Node, dst: &Vec2D) -> isize {
    (pos.row - dst.row).abs() + (pos.col - dst.col).abs()
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
impl ops::Sub for Vec2D {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        Self {
            row: self.row - other.row,
            col: self.col - other.col,
        }
    }
}

#[derive(Debug, Copy, Clone, Eq, PartialEq, PartialOrd, Ord, Hash)]
struct Node {
    dir: Vec2D,
    pos: Vec2D,
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 7036);
        assert_eq!(part_1(&second_example()), 11048);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 45);
        assert_eq!(part_2(&second_example()), 64);
    }
    fn example() -> String {
        String::from(
            "
            ###############
            #.......#....E#
            #.#.###.#.###.#
            #.....#.#...#.#
            #.###.#####.#.#
            #.#.#.......#.#
            #.#.#####.###.#
            #...........#.#
            ###.#.#####.#.#
            #...#.....#.#.#
            #.#.#.###.#.#.#
            #.....#...#.#.#
            #.###.#.#.#.#.#
            #S..#.....#...#
            ###############
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
            #################
            #...#...#...#..E#
            #.#.#.#.#.#.#.#.#
            #.#.#.#...#...#.#
            #.#.#.#.###.#.#.#
            #...#.#.#.....#.#
            #.#.#.#.#.#####.#
            #.#...#.#.#.....#
            #.#.#####.#.###.#
            #.#.#.......#...#
            #.#.###.#####.###
            #.#.#...#.....#.#
            #.#.#.#####.###.#
            #.#.#.........#.#
            #.#.#.#########.#
            #S#.............#
            #################
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

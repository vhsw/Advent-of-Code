use std::cmp::Reverse;
use std::{
    collections::{BinaryHeap, HashSet},
    fs,
};

fn main() {
    let data = fs::read_to_string("day_08/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data, 1000));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str, steps: usize) -> usize {
    let boxes = parse_input(data);
    let mut heap = BinaryHeap::new();
    for (i, a) in boxes.iter().enumerate() {
        for (j, b) in boxes.iter().skip(i + 1).enumerate() {
            let distance = euclidean_distance_sq(a, b);
            heap.push((Reverse(distance), i, i + j + 1));
        }
    }
    let mut circuits: Vec<HashSet<usize>> = Vec::new();

    for _ in 0..steps {
        let (_, i, j) = heap.pop().unwrap();

        let found: Vec<HashSet<usize>> = circuits
            .iter()
            .filter(|c| c.contains(&i) || c.contains(&j))
            .cloned()
            .collect();

        if found.len() == 0 {
            let mut c = HashSet::new();
            c.insert(i);
            c.insert(j);
            circuits.push(c);
        } else {
            circuits = circuits
                .iter()
                .filter(|c| !(c.contains(&i) || c.contains(&j)))
                .cloned()
                .collect();
            let mut c = HashSet::new();
            c.insert(i);
            c.insert(j);
            for set in found {
                for p in set {
                    c.insert(p);
                }
            }
            circuits.push(c);
        }
    }
    let mut circuit_lens: Vec<usize> = circuits.iter().map(|c| c.len()).collect();
    circuit_lens.sort();
    circuit_lens.reverse();
    circuit_lens.iter().take(3).product()
}
fn part_2(data: &str) -> u64 {
    let boxes = parse_input(data);
    let mut heap = BinaryHeap::new();
    for (i, a) in boxes.iter().enumerate() {
        for (j, b) in boxes.iter().skip(i + 1).enumerate() {
            let distance = euclidean_distance_sq(a, b);
            heap.push((Reverse(distance), i, i + j + 1));
        }
    }
    let mut adj = vec![vec![false; boxes.len()]; boxes.len()];
    for i in 0..adj.len() {
        adj[i][i] = true;
    }
    let mut circuits: Vec<HashSet<usize>> = Vec::new();
    for i in 0..boxes.len() {
        let mut c = HashSet::new();
        c.insert(i);
        circuits.push(c);
    }
    loop {
        let (_, i, j) = heap.pop().unwrap();

        let found: Vec<HashSet<usize>> = circuits
            .iter()
            .filter(|c| c.contains(&i) || c.contains(&j))
            .cloned()
            .collect();

        if found.len() == 0 {
            let mut c = HashSet::new();
            c.insert(i);
            c.insert(j);
            circuits.push(c);
        } else {
            circuits = circuits
                .iter()
                .filter(|c| !(c.contains(&i) || c.contains(&j)))
                .cloned()
                .collect();
            let mut c = HashSet::new();
            for set in found {
                for p in set {
                    c.insert(p);
                }
            }
            c.insert(i);
            c.insert(j);
            circuits.push(c);
        }
        if circuits.len() == 1 {
            return boxes[i].0 * boxes[j].0;
        }
    }
}
type Point = (u64, u64, u64);
fn euclidean_distance_sq(a: &Point, b: &Point) -> u64 {
    (a.0.abs_diff(b.0)).pow(2) + (a.1.abs_diff(b.1)).pow(2) + (a.2.abs_diff(b.2)).pow(2)
}
fn parse_input(data: &str) -> Vec<Point> {
    let mut result = Vec::new();
    for line in data.lines() {
        let nums: Vec<u64> = line.split(',').map(|part| part.parse().unwrap()).collect();
        result.push((nums[0], nums[1], nums[2]));
    }
    result
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example(), 10), 40);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 25272);
    }
    fn example() -> String {
        String::from(
            "
            162,817,812
            57,618,57
            906,360,560
            592,479,940
            352,342,300
            466,668,158
            542,29,236
            431,825,988
            739,650,466
            52,470,668
            216,146,977
            819,987,18
            117,168,530
            805,96,715
            346,949,466
            970,615,88
            941,993,340
            862,61,35
            984,92,344
            425,690,689
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

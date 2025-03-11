use std::collections::{HashMap, HashSet, VecDeque};
use std::fs;
use std::ops;
use std::sync::LazyLock;
fn main() {
    let data = fs::read_to_string("day_21/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    solve(data, 2)
}
fn part_2(data: &str) -> usize {
    solve(data, 25)
}
fn solve(data: &str, depth: usize) -> usize {
    parse_input(data)
        .iter()
        .map(|string| find_length(string.to_string(), depth) * to_number(string))
        .sum()
}
fn parse_input(data: &str) -> Vec<String> {
    data.trim().lines().map(|line| line.to_string()).collect()
}
fn find_length(input: String, depth: usize) -> usize {
    let mut cache = HashMap::new();
    let total = "A"
        .chars()
        .chain(input.chars())
        .zip(input.chars())
        .map(|(prev, cur)| {
            NUMPAD
                .get(&(prev, cur))
                .unwrap()
                .iter()
                .map(|keys| shortest_seq(keys.to_owned() + &'A'.to_string(), depth, &mut cache))
                .min()
                .unwrap()
        })
        .sum();
    total
}
fn to_number(s: &str) -> usize {
    s[..s.len() - 1].parse().unwrap()
}
fn shortest_seq(keys: String, depth: usize, cache: &mut HashMap<(String, usize), usize>) -> usize {
    if depth == 0 {
        return keys.len();
    }
    let cache_key = (keys.to_owned(), depth);
    if let Some(total) = cache.get(&cache_key) {
        return *total;
    }
    let total = keys
        .split_inclusive('A')
        .map(|sub_key| {
            let mut result = Vec::new();
            build_seq(sub_key, 0, 'A', "".to_string(), &mut result);
            result
                .iter()
                .map(|sequence| shortest_seq(sequence.to_owned(), depth - 1, cache))
                .min()
                .unwrap()
        })
        .sum();
    cache.insert(cache_key, total);
    total
}
fn build_seq(
    keys: &str,
    index: usize,
    prev_key: char,
    curr_path: String,
    result: &mut Vec<String>,
) {
    if index == keys.len() {
        result.push(curr_path);
        return;
    }
    let current_key = keys.chars().nth(index).unwrap();
    DPAD.get(&(prev_key, current_key))
        .unwrap()
        .iter()
        .for_each(|path| {
            build_seq(
                keys,
                index + 1,
                current_key,
                curr_path.to_owned() + path + &'A'.to_string(),
                result,
            )
        });
}
type Keypad = HashMap<char, Vec2D>;
fn numeric_keypad() -> Keypad {
    HashMap::from([
        ('7', Vec2D { row: 0, col: 0 }),
        ('8', Vec2D { row: 0, col: 1 }),
        ('9', Vec2D { row: 0, col: 2 }),
        ('4', Vec2D { row: 1, col: 0 }),
        ('5', Vec2D { row: 1, col: 1 }),
        ('6', Vec2D { row: 1, col: 2 }),
        ('1', Vec2D { row: 2, col: 0 }),
        ('2', Vec2D { row: 2, col: 1 }),
        ('3', Vec2D { row: 2, col: 2 }),
        ('0', Vec2D { row: 3, col: 1 }),
        ('A', Vec2D { row: 3, col: 2 }),
    ])
}
fn directional_keypad() -> Keypad {
    HashMap::from([
        ('^', Vec2D { row: 0, col: 1 }),
        ('A', Vec2D { row: 0, col: 2 }),
        ('<', Vec2D { row: 1, col: 0 }),
        ('v', Vec2D { row: 1, col: 1 }),
        ('>', Vec2D { row: 1, col: 2 }),
    ])
}
type Moves = HashMap<(char, char), Vec<String>>;
static NUMPAD: LazyLock<Moves> = LazyLock::new(|| precalc_best_pathes(&numeric_keypad()));
static DPAD: LazyLock<Moves> = LazyLock::new(|| precalc_best_pathes(&directional_keypad()));
fn precalc_best_pathes(keypad: &Keypad) -> HashMap<(char, char), Vec<String>> {
    let mut hm = HashMap::new();
    keypad.keys().for_each(|src| {
        keypad.keys().for_each(|dst| {
            hm.insert((*src, *dst), bfs(src, dst, keypad));
        })
    });
    hm
}
fn bfs(src: &char, dst: &char, keypad: &Keypad) -> Vec<String> {
    let mut results = Vec::new();
    let mut todo = VecDeque::new();
    let mut seen = HashSet::new();
    todo.push_back((*src, "".to_string()));
    while let Some((src, path)) = todo.pop_front() {
        seen.insert(src);
        if src == *dst {
            let perplexity = path
                .chars()
                .zip(path.chars().skip(1))
                .filter(|(a, b)| a != b)
                .count();
            results.push((path, perplexity));
            continue;
        }
        for (dir, next) in neighbors(&src, keypad) {
            if seen.contains(&next) {
                continue;
            }
            todo.push_back((next, path.to_owned() + &dir.to_string()));
        }
    }
    let best = results
        .iter()
        .map(|(path, pp)| (path.len(), pp))
        .min()
        .unwrap();

    results
        .iter()
        .filter(|(path, pp)| (path.len(), pp) <= best)
        .map(|(path, _)| path)
        .cloned()
        .collect()
}
fn neighbors(src: &char, keypad: &Keypad) -> Vec<(char, char)> {
    let rev: HashMap<Vec2D, char> = HashMap::from_iter(keypad.iter().map(|(k, v)| (*v, *k)));
    let src = *keypad.get(src).unwrap();
    [
        ('<', Vec2D { row: 0, col: -1 }),
        ('v', Vec2D { row: 1, col: 0 }),
        ('^', Vec2D { row: -1, col: 0 }),
        ('>', Vec2D { row: 0, col: 1 }),
    ]
    .iter()
    .map(|&(c, dir)| (c, src + dir))
    .filter(|(_, dir)| rev.contains_key(dir))
    .map(|(c, dir)| (c, *rev.get(&dir).unwrap()))
    .collect()
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
        assert_eq!(part_1(&example()), 126384);
    }
    fn example() -> String {
        String::from(
            "
            029A
            980A
            179A
            456A
            379A
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

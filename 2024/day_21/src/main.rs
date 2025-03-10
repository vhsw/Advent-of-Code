use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap, HashSet, VecDeque};
use std::fs;
use std::ops;
fn main() {
    let data = fs::read_to_string("day_21/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let sequences = parse_input(data);
    let keypads = make_keypad_stack(3);
    sequences
        .iter()
        .map(|string| {
            type_on_keypad(string, &keypads).len()
                * string[..string.len() - 1].parse::<usize>().unwrap()
        })
        .sum()
}
fn part_2(data: &str) -> usize {
    let sequences = parse_input(data);
    let keypads = make_keypad_stack(26);
    sequences
        .iter()
        .map(|string| {
            type_on_keypad(string, &keypads).len()
                * string[..string.len() - 1].parse::<usize>().unwrap()
        })
        .sum()
}
fn parse_input(data: &str) -> Vec<String> {
    data.trim().lines().map(|line| line.to_string()).collect()
}
fn make_keypad_stack(size: usize) -> Vec<Keypad> {
    let mut keypads = vec![numeric_keypad()];
    for _ in 0..size {
        keypads.push(directional_keypad());
    }
    keypads
}
fn type_on_keypad(string: &str, keypads: &[Keypad]) -> String {
    println!("Typing \"{string}\"");
    let mut keypad_states: Vec<char> = keypads.iter().map(|_| 'A').collect();
    let mut result = String::new();
    let mut memo = HashMap::new();
    for dst in string.chars() {
        let path = astar(&mut keypad_states, keypads, dst, &mut memo);
        result.push_str(&path);
    }
    // assert_eq!(check_answer(&result, keypads), string);
    result
}
#[allow(clippy::type_complexity)]
fn astar(
    keypad_states: &mut [char],
    keypads: &[Keypad],
    dst: char,
    memo: &mut HashMap<(Vec<char>, char), (Vec<char>, String)>,
) -> String {
    let keypad = &keypads[0];
    if keypads.len() == 1 {
        assert!(keypad.contains_key(&dst));
        keypad_states[0] = dst;
        return dst.to_string();
    }
    let memo_key = (keypad_states.to_owned(), dst);
    if let Some((states, result)) = memo.get(&memo_key) {
        keypad_states.copy_from_slice(states);
        return result.clone();
    }
    let src = keypad_states[0];
    let mut heap = BinaryHeap::new();
    heap.push(State {
        priority: 0,
        perplexity: 0,
        current: src,
        states: keypad_states[1..].to_vec().clone(),
        path: "".to_string(),
    });
    let mut best_len = None;
    let mut shortest_path: Option<String> = None;
    while let Some(State {
        priority: _,
        perplexity: _,
        current,
        states,
        path: current_path,
    }) = heap.pop()
    {
        if current == dst {
            if let Some(bl) = best_len {
                if bl < current_path.len() {
                    break;
                }
            } else {
                best_len = Some(current_path.len());
            }
            let mut states = states.clone();
            let path = current_path.clone() + &astar(&mut states, &keypads[1..], 'A', memo);
            for state in states.iter() {
                assert_eq!(*state, 'A');
            }
            if let Some(sp) = &shortest_path {
                if sp.len() < path.len() {
                    continue;
                }
            }
            shortest_path = Some(path);
            keypad_states[0] = dst;
            keypad_states[1..(states.len() + 1)].copy_from_slice(&states[..]);
        }
        for (dir, next) in neighbors(&current, keypad) {
            let mut states = states.clone();
            let new_path = current_path.to_owned() + &astar(&mut states, &keypads[1..], dir, memo);
            let priority = new_path.len() + heuristic(&next, &dst, keypad);
            let perplexity = new_path
                .chars()
                .zip(new_path.chars().skip(1))
                .filter(|(a, b)| a != b)
                .count();
            heap.push(State {
                priority,
                perplexity,
                current: next,
                states,
                path: new_path,
            });
        }
    }
    let path = shortest_path.unwrap();
    memo.insert(memo_key, (keypad_states.to_owned(), path.to_owned()));
    path
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
fn heuristic(src: &char, dst: &char, keypad: &Keypad) -> usize {
    let src = keypad.get(src).unwrap();
    let dst = keypad.get(dst).unwrap();
    (src.row - dst.row).unsigned_abs() + (src.col - dst.col).unsigned_abs()
}
#[allow(dead_code)]
fn check_answer(ans: &str, keypads: &[Keypad]) -> String {
    let (keypad, keypads) = keypads.split_last().unwrap();
    if keypads.is_empty() {
        ans.chars().for_each(|c| assert!(keypad.contains_key(&c)));
        return ans.to_string();
    }
    let (keypad, _) = keypads.split_last().unwrap();
    let rev: HashMap<Vec2D, char> = HashMap::from_iter(keypad.iter().map(|(k, v)| (*v, *k)));
    let mut pos = *keypad.get(&'A').unwrap();
    let mut buf = String::new();
    for char in ans.chars() {
        print!("{}", char);
        match char {
            '<' => {
                pos = pos + Vec2D { row: 0, col: -1 };
            }
            'v' => {
                pos = pos + Vec2D { row: 1, col: 0 };
            }
            '^' => {
                pos = pos + Vec2D { row: -1, col: 0 };
            }
            '>' => {
                pos = pos + Vec2D { row: 0, col: 1 };
            }
            'A' => {
                let ch = *rev.get(&pos).unwrap();
                buf.push(ch);
            }
            _ => unreachable!(),
        }
    }
    println!();
    check_answer(&buf, keypads)
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
#[derive(Clone, Eq, PartialEq)]
struct State {
    priority: usize,
    perplexity: usize,
    current: char,
    states: Vec<char>,
    path: String,
}
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .priority
            .cmp(&self.priority)
            .then_with(|| self.perplexity.cmp(&other.perplexity))
    }
}
impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_precalc() {
        dbg!(precalc_best_pathes(&numeric_keypad()));
        dbg!(precalc_best_pathes(&directional_keypad()));
    }

    #[test]
    fn test_type_on_keypad_len() {
        // assert_eq!(
        //     type_on_keypad(
        //         "029A",
        //         &[numeric_keypad(), directional_keypad(), directional_keypad()]
        //     ),
        //     "v<<A>>^A<A>AvA<^AA>A<vAAA>^A"
        // );
        let keypads = &make_keypad_stack(3);
        assert_eq!(
            type_on_keypad("029A", keypads).len(),
            "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A".len(),
            "029A"
        );
        assert_eq!(
            type_on_keypad("980A", keypads).len(),
            "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A".len(),
            "980A"
        );
        assert_eq!(
            type_on_keypad("179A", keypads).len(),
            "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A".len(),
            "179A"
        );
        assert_eq!(
            type_on_keypad("456A", keypads).len(),
            "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A".len(),
            "456A"
        );
        assert_eq!(
            type_on_keypad("379A", keypads).len(),
            "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A".len(),
            "379A"
        );
    }
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

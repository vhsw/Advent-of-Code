use std::collections::{HashMap, HashSet};
use std::fs;

fn main() {
    let data = fs::read_to_string("day_22/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    parse_input(data)
        .iter()
        .map(|secret| {
            let mut secret = *secret;
            (0..2000).for_each(|_| {
                secret = evolve(secret);
            });
            secret
        })
        .sum()
}
fn part_2(data: &str) -> usize {
    let mut totals: HashMap<Vec<isize>, usize> = HashMap::new();
    parse_input(data)
        .iter()
        .cloned()
        .map(generate_seqence)
        .for_each(|(seq, diff)| {
            let chunk_size = 4;
            let mut seen = HashSet::new();
            for i in chunk_size..diff.len() + 1 {
                let chunk = &diff[i - chunk_size..i];
                if seen.contains(chunk) {
                    continue;
                }
                seen.insert(chunk.to_vec());
                *totals.entry(chunk.to_vec()).or_insert(0) += seq[i - 1];
            }
        });
    *totals.iter().max_by_key(|(_, v)| *v).unwrap().1
}
fn parse_input(data: &str) -> Vec<usize> {
    data.trim()
        .lines()
        .map(|line| line.parse().unwrap())
        .collect()
}
fn evolve(secret: usize) -> usize {
    let mut secret = secret;
    let result = secret * 64;
    secret = mix(secret, result);
    secret = prune(secret);
    let result = secret / 32;
    secret = mix(secret, result);
    secret = prune(secret);
    let result = secret * 2048;
    secret = mix(secret, result);
    secret = prune(secret);
    secret
}
fn mix(secret: usize, value: usize) -> usize {
    value ^ secret
}
fn prune(secret: usize) -> usize {
    secret % 16777216
}
fn generate_seqence(secret: usize) -> (Vec<usize>, Vec<isize>) {
    let mut secret = secret;
    let mut rems = Vec::new();
    let mut diff = Vec::new();
    (0..2000).for_each(|_| {
        let new_secret = evolve(secret);
        rems.push(new_secret % 10);
        diff.push((new_secret % 10) as isize - (secret % 10) as isize);
        secret = new_secret
    });
    (rems, diff)
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 37327623);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example_2()), 23);
    }
    #[test]
    fn test_mix() {
        assert_eq!(mix(42, 15), 37);
    }
    #[test]
    fn test_prune() {
        assert_eq!(prune(100000000), 16113920);
    }
    #[test]
    fn test_evolve() {
        let mut secret = 123;
        for (step, result) in [
            15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432,
            5908254,
        ]
        .iter()
        .enumerate()
        {
            secret = evolve(secret);
            assert_eq!(secret, *result, "step {}", step);
        }
    }
    fn example() -> String {
        String::from(
            "
            1
            10
            100
            2024
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn example_2() -> String {
        String::from(
            "
            1
            2
            3
            2024
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

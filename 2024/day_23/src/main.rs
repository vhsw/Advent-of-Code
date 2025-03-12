use std::collections::{HashMap, HashSet};
use std::fs;

fn main() {
    let data = fs::read_to_string("day_23/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let graph = parse_input(data);
    let mut triplets = HashSet::new();
    for key in graph.keys() {
        if !key.starts_with('t') {
            continue;
        }
        let peers = graph.get(key).unwrap();
        if peers.len() < 2 {
            continue;
        }
        for (n, a) in peers.iter().enumerate().take(peers.len() - 1) {
            for b in peers.iter().skip(n + 1) {
                if graph.get(a).unwrap().contains(b) && graph.get(b).unwrap().contains(a) {
                    let mut parts = [key.to_string(), a.to_string(), b.to_string()];
                    parts.sort();
                    triplets.insert(parts.join(","));
                }
            }
        }
    }
    triplets.len()
}
fn part_2(data: &str) -> String {
    let graph = parse_input(data);
    let mut p = graph.keys().cloned().collect::<HashSet<_>>();
    let r = HashSet::new();
    let mut x = HashSet::new();
    let max_clique = bron_kerbosch(&r, &mut p, &mut x, &graph);
    let mut parts = max_clique.iter().cloned().collect::<Vec<_>>();
    parts.sort();
    parts.join(",")
}
fn parse_input(data: &str) -> HashMap<&str, HashSet<&str>> {
    let mut graph = HashMap::new();
    data.trim().lines().for_each(|line| {
        let (a, b) = line.split_once('-').unwrap();
        graph.entry(a).or_insert_with(HashSet::new).insert(b);
        graph.entry(b).or_insert_with(HashSet::new).insert(a);
    });
    graph
}
pub fn bron_kerbosch<'a>(
    r: &HashSet<&'a str>,
    p: &mut HashSet<&'a str>,
    x: &mut HashSet<&'a str>,
    graph: &'a HashMap<&str, HashSet<&str>>,
) -> HashSet<&'a str> {
    if p.is_empty() && x.is_empty() {
        return r.clone();
    }
    let mut max_clique = HashSet::new();
    for v in p.clone() {
        let mut new_r = r.clone();
        new_r.insert(v);
        let neighbors = graph.get(&v).unwrap();
        let mut new_p = p.intersection(neighbors).cloned().collect();
        let mut new_x = x.intersection(neighbors).cloned().collect();
        let clique = bron_kerbosch(&new_r, &mut new_p, &mut new_x, graph);
        if clique.len() > max_clique.len() {
            max_clique = clique;
        }
        p.remove(&v);
        x.insert(v);
    }
    max_clique
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 7);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), "co,de,ka,ta");
    }
    fn example() -> String {
        String::from(
            "
            kh-tc
            qp-kh
            de-cg
            ka-co
            yn-aq
            qp-ub
            cg-tb
            vc-aq
            tb-ka
            wh-tc
            yn-cg
            kh-ub
            ta-co
            de-co
            tc-td
            tb-wq
            wh-td
            ta-ka
            td-qp
            aq-cg
            wq-ub
            ub-vc
            de-ta
            wq-aq
            wq-vc
            wh-yn
            ka-de
            kh-ta
            co-tc
            wh-qp
            tb-vc
            td-yn
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

use std::fs;

fn main() {
    let data = fs::read_to_string("day_05/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &String) -> usize {
    let (head, trail) = data.split_once("\n\n").unwrap();
    let rules = read_rules(&head.to_string());
    let updates = read_updates(&trail.to_string());
    return updates
        .iter()
        .filter(|update| is_correct_order(update, &rules))
        .map(get_middle)
        .sum();
}
fn part_2(data: &String) -> usize {
    let (head, trail) = data.split_once("\n\n").unwrap();
    let rules = read_rules(&head.to_string());
    let updates = read_updates(&trail.to_string());
    return updates
        .iter()
        .filter(|update| !is_correct_order(update, &rules))
        .map(|update| fix_order(update.clone(), &rules))
        .map(|update| get_middle(&update))
        .sum();
}
fn read_rules(data: &String) -> Vec<(usize, usize)> {
    let mut rules = Vec::new();
    for line in data.lines() {
        let parts: Vec<&str> = line.split('|').collect();
        let rule = (parts[0].parse().unwrap(), parts[1].parse().unwrap());
        rules.push(rule);
    }
    return rules;
}
fn read_updates(data: &String) -> Vec<Vec<usize>> {
    let mut updates = Vec::new();
    for line in data.lines() {
        let update = line.split(',').map(|num| num.parse().unwrap()).collect();
        updates.push(update);
    }
    return updates;
}
fn is_correct_order(update: &Vec<usize>, rules: &Vec<(usize, usize)>) -> bool {
    for rule in rules {
        let (before, after) = rule;
        let before_idx = update.iter().position(|&x| x == *before);
        let after_idx = update.iter().position(|&x| x == *after);
        if before_idx.is_none() || after_idx.is_none() {
            continue;
        }
        if before_idx.unwrap() > after_idx.unwrap() {
            return false;
        }
    }
    return true;
}
fn fix_order(update: Vec<usize>, rules: &Vec<(usize, usize)>) -> Vec<usize> {
    let mut update = update.clone();
    // YOLO
    while !is_correct_order(&update, rules) {
        for rule in rules {
            let (before, after) = rule;
            let before_idx = update.iter().position(|&x| x == *before);
            let after_idx = update.iter().position(|&x| x == *after);
            if before_idx.is_none() || after_idx.is_none() {
                continue;
            }
            if before_idx.unwrap() > after_idx.unwrap() {
                update.swap(before_idx.unwrap(), after_idx.unwrap());
            }
        }
    }
    return update;
}
fn get_middle(update: &Vec<usize>) -> usize {
    return update[update.len() / 2];
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 143);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 123);
    }
    fn example() -> String {
        return String::from(
            "
            47|53
            97|13
            97|61
            97|47
            75|29
            61|13
            75|53
            29|13
            97|29
            53|29
            61|53
            97|53
            61|29
            47|13
            75|47
            97|75
            47|61
            75|61
            47|29
            75|13
            53|13

            75,47,61,53,29
            97,61,53,29,13
            75,29,13
            75,97,47,61,53
            61,13,29
            97,13,75,29,47
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect();
    }
}

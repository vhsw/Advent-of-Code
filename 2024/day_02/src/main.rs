use std::fs;

fn main() {
    let data = fs::read_to_string("day_02/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}

fn part_1(data: &str) -> usize {
    let reports = parse_input(data);
    reports.iter().filter(|report| is_safe(report)).count()
}
fn part_2(data: &str) -> usize {
    let reports = parse_input(data);
    reports
        .iter()
        .filter(|report| {
            for idx in 0..report.len() {
                let new_report = [&report[..idx], &report[idx + 1..]].concat();
                if is_safe(&new_report) {
                    return true;
                };
            }
            false
        })
        .count()
}
fn parse_input(data: &str) -> Vec<Vec<u32>> {
    let mut reports = Vec::new();
    for line in data.lines() {
        reports.push(
            line.split_whitespace()
                .map(|val| val.parse().unwrap())
                .collect(),
        );
    }
    reports
}
fn is_safe(report: &[u32]) -> bool {
    (all_decreasing(report) || all_increasing(report)) && adj_diff_is_good(report)
}
fn all_increasing(report: &[u32]) -> bool {
    if report.len() < 2 {
        return true;
    }
    for (prev, val) in report.iter().zip(report[1..].iter()) {
        if prev >= val {
            return false;
        };
    }
    true
}
fn all_decreasing(report: &[u32]) -> bool {
    if report.len() < 2 {
        return true;
    }
    for (prev, val) in report.iter().zip(report[1..].iter()) {
        if prev <= val {
            return false;
        };
    }
    true
}
fn adj_diff_is_good(report: &[u32]) -> bool {
    if report.len() < 2 {
        return true;
    }
    for (prev, val) in report.iter().zip(report[1..].iter()) {
        let diff = prev.abs_diff(*val);
        if !(1..=3).contains(&diff) {
            return false;
        };
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 2);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 4);
    }
    fn example() -> String {
        String::from(
            "
            7 6 4 2 1
            1 2 7 8 9
            9 7 6 2 1
            1 3 2 4 5
            8 6 4 4 1
            1 3 6 7 9
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

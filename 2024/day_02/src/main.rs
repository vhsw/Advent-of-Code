use std::fs;

fn main() {
    let data = fs::read_to_string("day_02/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}

fn part_1(data: &String) -> usize {
    let reports = get_reports(data);
    return reports.iter().filter(|report| is_safe(report)).count();
}
fn part_2(data: &String) -> usize {
    let reports = get_reports(data);
    return reports
        .iter()
        .filter(|report| {
            for idx in 0..report.len() {
                let new_report = [&report[..idx], &report[idx + 1..]].concat();
                if is_safe(&new_report) {
                    return true;
                };
            }
            return false;
        })
        .count();
}
fn get_reports(data: &String) -> Vec<Vec<u32>> {
    let mut reports = Vec::new();
    for line in data.lines() {
        reports.push(
            line.split_whitespace()
                .map(|val| val.parse().unwrap())
                .collect(),
        );
    }
    return reports;
}
fn is_safe(report: &Vec<u32>) -> bool {
    return (all_decreasing(report) || all_increasing(report)) && adj_diff_is_good(report);
}
fn all_increasing(report: &Vec<u32>) -> bool {
    if report.len() < 2 {
        return true;
    }
    for (prev, val) in report.iter().zip(report[1..].iter()) {
        if prev >= val {
            return false;
        };
    }
    return true;
}
fn all_decreasing(report: &Vec<u32>) -> bool {
    if report.len() < 2 {
        return true;
    }
    for (prev, val) in report.iter().zip(report[1..].iter()) {
        if prev <= val {
            return false;
        };
    }
    return true;
}
fn adj_diff_is_good(report: &Vec<u32>) -> bool {
    if report.len() < 2 {
        return true;
    }
    for (prev, val) in report.iter().zip(report[1..].iter()) {
        let diff = prev.abs_diff(*val);
        if diff > 3 || diff < 1 {
            return false;
        };
    }
    return true;
}

#[cfg(test)]
mod tests {
    use super::*;
    fn example() -> String {
        return String::from(
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
        .collect();
    }

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 2);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 4);
    }
}

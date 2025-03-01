use regex::Regex;
use std::fs;

fn main() {
    let data = fs::read_to_string("day_03/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}

fn part_1(data: &String) -> i32 {
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();

    return re
        .captures_iter(data)
        .map(|c| c.extract())
        .map(|(_, [a, b])| a.parse::<i32>().unwrap() * b.parse::<i32>().unwrap())
        .sum();
}
fn part_2(data: &String) -> i32 {
    let mut sum = 0;
    for chunk in data.split("do()") {
        for enabled in chunk.split("don't()") {
            sum += part_1(&enabled.to_string());
            break;
        }
    }
    return sum;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(
            part_1(
                &"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
                    .to_string()
            ),
            161
        );
    }
    #[test]
    fn test_part_2() {
        assert_eq!(
            part_2(
                &"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
                    .to_string()
            ),
            48
        );
    }
}

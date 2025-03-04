use regex::Regex;
use std::fs;

fn main() {
    let data = fs::read_to_string("day_13/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> isize {
    let machines = create_machines(data);
    machines
        .iter()
        .filter_map(try_solve_machine)
        .filter(|(a, b)| *a <= 100 && *b <= 100)
        .map(|(a, b)| a * 3 + b)
        .sum()
}
fn part_2(data: &str) -> isize {
    let mut machines = create_machines(data);
    machines.iter_mut().for_each(|m| {
        m.prize.x += 10000000000000;
        m.prize.y += 10000000000000;
    });
    machines
        .iter()
        .filter_map(try_solve_machine)
        .map(|(a, b)| a * 3 + b)
        .sum()
}
#[derive(Debug)]
struct Vec2D {
    x: isize,
    y: isize,
}
#[derive(Debug)]
struct Machine {
    btn_a: Vec2D,
    btn_b: Vec2D,
    prize: Vec2D,
}
fn create_machines(data: &str) -> Vec<Machine> {
    let re = Regex::new(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)",
    )
    .unwrap();
    data.split("\n\n")
        .map(|section| {
            let caps = re.captures(section).unwrap();
            Machine {
                btn_a: Vec2D {
                    x: caps[1].parse().unwrap(),
                    y: caps[2].parse().unwrap(),
                },
                btn_b: Vec2D {
                    x: caps[3].parse().unwrap(),
                    y: caps[4].parse().unwrap(),
                },
                prize: Vec2D {
                    x: caps[5].parse().unwrap(),
                    y: caps[6].parse().unwrap(),
                },
            }
        })
        .collect()
}
fn try_solve_machine(machine: &Machine) -> Option<(isize, isize)> {
    let (a_x, a_y) = (machine.btn_a.x, machine.btn_a.y);
    let (b_x, b_y) = (machine.btn_b.x, machine.btn_b.y);
    let (p_x, p_y) = (machine.prize.x, machine.prize.y);
    // p_x = x * a_x + y * b_x
    // p_y = x * a_y + y * b_y
    let x_num = (p_x * b_y) - (b_x * p_y);
    let x_den = (a_x * b_y) - (b_x * a_y);
    if x_num % x_den != 0 {
        return None;
    }
    let x = x_num / x_den;
    let y_num = p_y - x * a_y;
    let y_den = b_y;
    if y_num % y_den != 0 {
        return None;
    }
    let y = (p_y - x * a_y) / b_y;
    if x >= 0 && y >= 0 { Some((x, y)) } else { None }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 480);
    }
    fn example() -> String {
        String::from(
            "
            Button A: X+94, Y+34
            Button B: X+22, Y+67
            Prize: X=8400, Y=5400

            Button A: X+26, Y+66
            Button B: X+67, Y+21
            Prize: X=12748, Y=12176

            Button A: X+17, Y+86
            Button B: X+84, Y+37
            Prize: X=7870, Y=6450

            Button A: X+69, Y+23
            Button B: X+27, Y+71
            Prize: X=18641, Y=10279
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

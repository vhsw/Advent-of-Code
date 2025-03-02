use std::fs;

fn main() {
    let data = fs::read_to_string("day_07/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &String) -> usize {
    let equations = read_equations(data);
    let ops = vec![add, mul];
    get_calibration_result(&equations, &ops)
}
fn part_2(data: &String) -> usize {
    let equations = read_equations(data);
    let ops = vec![add, mul, concat];
    get_calibration_result(&equations, &ops)
}
fn get_calibration_result(
    equations: &Vec<Equation>,
    ops: &Vec<fn(usize, usize) -> usize>,
) -> usize {
    equations
        .iter()
        .filter(|equation| is_possible(equation, &ops))
        .map(|equation| equation.result)
        .sum()
}
#[derive(Debug)]
struct Equation {
    result: usize,
    variables: Vec<usize>,
}
fn read_equations(data: &String) -> Vec<Equation> {
    data.lines()
        .map(|line| {
            let parts: Vec<&str> = line.split(':').collect();
            let result = parts[0].parse().unwrap();
            let variables: Vec<usize> = parts[1]
                .split_whitespace()
                .map(|v| v.parse().unwrap())
                .rev()
                .collect();
            Equation { result, variables }
        })
        .collect()
}
fn is_possible(equation: &Equation, ops: &Vec<fn(usize, usize) -> usize>) -> bool {
    if equation.variables.len() == 1 {
        return equation.result == equation.variables[0];
    }
    for op in ops.iter() {
        let mut variables = equation.variables.clone();
        let a = variables.pop().unwrap();
        let b = variables.pop().unwrap();
        variables.push(op(a, b));
        if is_possible(
            &Equation {
                result: equation.result,
                variables,
            },
            ops,
        ) {
            return true;
        }
    }
    return false;
}
fn add(a: usize, b: usize) -> usize {
    a + b
}
fn mul(a: usize, b: usize) -> usize {
    a * b
}
fn concat(a: usize, b: usize) -> usize {
    (a.to_string() + &b.to_string()).parse().unwrap()
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 3749);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 11387);
    }
    fn example() -> String {
        String::from(
            "
            190: 10 19
            3267: 81 40 27
            83: 17 5
            156: 15 6
            7290: 6 8 6 15
            161011: 16 10 13
            192: 17 8 14
            21037: 9 7 18 13
            292: 11 6 16 20
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

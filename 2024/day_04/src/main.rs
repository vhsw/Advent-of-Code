use std::fs;

fn main() {
    let data = fs::read_to_string("day_04/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let grid = parse_input(data);
    let mut count = 0;
    for row in 0..grid.len() {
        for col in 0..grid[row].len() {
            count += find_xmas(&grid, row, col)
        }
    }
    count
}
fn part_2(data: &str) -> usize {
    let grid = parse_input(data);
    let mut count = 0;
    for row in 0..grid.len() {
        for col in 0..grid[row].len() {
            count += find_x_mas(&grid, row, col)
        }
    }
    count
}
fn parse_input(data: &str) -> Vec<Vec<char>> {
    let mut grid: Vec<Vec<char>> = Vec::new();
    for line in data.lines() {
        let chars = line.chars().collect();
        grid.push(chars);
    }
    grid
}
fn find_xmas(grid: &[Vec<char>], row: usize, col: usize) -> usize {
    let target: Vec<char> = "XMAS".chars().collect();
    let mut count = 0;
    if grid[row][col] != target[0] {
        return count;
    }

    // South
    if col < grid[row].len() - 3 && (1..4).all(|i| grid[row][col + i] == target[i]) {
        count += 1;
    }
    // North
    if col > 2 && (1..4).all(|i| grid[row][col - i] == target[i]) {
        count += 1;
    }
    // East
    if row < grid.len() - 3 && (1..4).all(|i| grid[row + i][col] == target[i]) {
        count += 1;
    }
    // West
    if row > 2 && (1..4).all(|i| grid[row - i][col] == target[i]) {
        count += 1;
    }
    // South-East
    if row < grid.len() - 3
        && col < grid[row].len() - 3
        && (1..4).all(|i| grid[row + i][col + i] == target[i])
    {
        count += 1;
    }
    // South-West
    if row > 2 && col < grid[row].len() - 3 && (1..4).all(|i| grid[row - i][col + i] == target[i]) {
        count += 1;
    }
    // North-West
    if row > 2 && col > 2 && (1..4).all(|i| grid[row - i][col - i] == target[i]) {
        count += 1;
    }
    // North-East
    if row < grid.len() - 3 && col > 2 && (1..4).all(|i| grid[row + i][col - i] == target[i]) {
        count += 1;
    }
    count
}
fn find_x_mas(grid: &[Vec<char>], row: usize, col: usize) -> usize {
    if row < 1
        || col < 1
        || row > grid.len() - 2
        || col > grid[row].len() - 2
        || grid[row][col] != 'A'
    {
        return 0;
    }
    let nw = grid[row - 1][col - 1];
    let ne = grid[row - 1][col + 1];
    let sw = grid[row + 1][col - 1];
    let se = grid[row + 1][col + 1];
    if (nw == 'M' && se == 'S' || nw == 'S' && se == 'M')
        && (ne == 'M' && sw == 'S' || ne == 'S' && sw == 'M')
    {
        return 1;
    }
    0
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 18);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 9);
    }
    fn example() -> String {
        String::from(
            "
            MMMSXXMASM
            MSAMXMSMSA
            AMXSXMAAMM
            MSAMASMSMX
            XMASAMXAMM
            XXAMMXXAMA
            SMSMSASXSS
            SAXAMASAAA
            MAMMMXMMMM
            MXMXAXMASX
            "
            .trim(),
        )
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

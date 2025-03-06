use std::collections::HashSet;
use std::fs;
use std::ops;

fn main() {
    let data = fs::read_to_string("day_15/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> isize {
    let (mut warehouse, moves) = parse_input(data);
    moves.iter().for_each(|dir| warehouse.attempt_move(dir));
    warehouse.sum_of_all_boxes_gps_coordinates()
}
fn part_2(data: &str) -> isize {
    let data = grow_map(data);
    let (mut warehouse, moves) = parse_input(&data);
    moves.iter().for_each(|dir| {
        warehouse.attempt_move(dir);
    });
    warehouse.sum_of_all_boxes_gps_coordinates()
}
fn parse_input(data: &str) -> (Warehouse, Vec<Vec2D>) {
    let (warehouse, moves) = data.split_once("\n\n").unwrap();
    (parse_warehouse(warehouse), parse_moves(moves))
}
fn grow_map(data: &str) -> String {
    data.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
}
fn parse_warehouse(data: &str) -> Warehouse {
    let mut robot = None;
    let mut walls = HashSet::new();
    let mut boxes = HashSet::new();
    let mut wide = false;
    data.lines().enumerate().for_each(|(row, line)| {
        line.chars().enumerate().for_each(|(col, c)| {
            let pos = Vec2D {
                row: row as isize,
                col: col as isize,
            };
            match c {
                '@' => robot = Some(pos),
                '#' => {
                    walls.insert(pos);
                }
                'O' => {
                    boxes.insert(pos);
                }
                '[' => {
                    boxes.insert(pos);
                    wide = true;
                }
                '.' | ']' => {}
                _ => unreachable!(),
            }
        })
    });
    Warehouse {
        robot: robot.unwrap(),
        walls,
        boxes,
        wide,
    }
}
fn parse_moves(data: &str) -> Vec<Vec2D> {
    data.chars()
        .filter(|c| *c != '\n')
        .map(|c| match c {
            '^' => Vec2D { row: -1, col: 0 },
            'v' => Vec2D { row: 1, col: 0 },
            '<' => Vec2D { row: 0, col: -1 },
            '>' => Vec2D { row: 0, col: 1 },
            _ => unreachable!("Invalid move character '{c}'"),
        })
        .collect()
}

#[derive(Debug, PartialEq, Eq, Hash, Clone, Copy)]
struct Vec2D {
    row: isize,
    col: isize,
}
impl Vec2D {
    fn gps_coordinates(&self) -> isize {
        self.row * 100 + self.col
    }
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
#[derive(Debug)]
struct Warehouse {
    robot: Vec2D,
    walls: HashSet<Vec2D>,
    boxes: HashSet<Vec2D>,
    wide: bool,
}
impl Warehouse {
    fn attempt_move(&mut self, dir: &Vec2D) {
        if self.wide {
            self.__attempt_move_wide(dir);
        } else {
            self.__attempt_move(dir);
        }
    }
    fn __attempt_move(&mut self, dir: &Vec2D) {
        let mut pos = self.robot + *dir;
        let mut boxes_to_move = Vec::new();
        while self.boxes.contains(&(pos)) {
            boxes_to_move.push(pos);
            pos = pos + *dir;
        }
        if self.walls.contains(&pos) {
            return;
        }
        for box_pos in &boxes_to_move {
            self.boxes.remove(box_pos);
        }
        for box_pos in &boxes_to_move {
            self.boxes.insert(*box_pos + *dir);
        }
        self.robot = self.robot + *dir;
    }
    fn __attempt_move_wide(&mut self, dir: &Vec2D) {
        let pos = self.robot + *dir;
        if self.walls.contains(&pos) {
            return;
        }

        let boxes_to_move = self.__move_box(&pos, dir);
        if boxes_to_move.is_none() {
            return;
        }
        let boxes_to_move = boxes_to_move.unwrap();
        for box_pos in &boxes_to_move {
            self.boxes.remove(box_pos);
        }
        for box_pos in &boxes_to_move {
            self.boxes.insert(*box_pos + *dir);
        }
        self.robot = pos;
        assert!(!self.boxes.contains(&self.robot));
        assert!(
            !self
                .boxes
                .contains(&(self.robot + Vec2D { row: 0, col: -1 }))
        );
    }
    fn __move_box(&self, src: &Vec2D, dir: &Vec2D) -> Option<Vec<Vec2D>> {
        if self.walls.contains(src) {
            return None;
        }
        let src = self.__find_box(src);
        if src.is_none() {
            return Some(Vec::new());
        }
        let src = src.unwrap();
        if self.walls.contains(&(src + *dir))
            || self
                .walls
                .contains(&(src + *dir + Vec2D { row: 0, col: 1 }))
        {
            return None;
        }
        let mut affected_boxes = vec![src];
        if dir.row == 0 {
            if dir.col == -1 {
                if let Some(boxes) = self.__move_box(&(src + *dir), dir) {
                    affected_boxes.extend(boxes);
                } else {
                    return None;
                }
            } else if let Some(boxes) = self.__move_box(&(src + *dir + *dir), dir) {
                affected_boxes.extend(boxes);
            } else {
                return None;
            }
        } else {
            if let Some(boxes) = self.__move_box(&(src + *dir), dir) {
                affected_boxes.extend(boxes);
            } else {
                return None;
            }
            if let Some(boxes) = self.__move_box(&(src + *dir + Vec2D { row: 0, col: 1 }), dir) {
                affected_boxes.extend(boxes);
            } else {
                return None;
            }
        }
        Some(affected_boxes)
    }
    fn __find_box(&self, pos: &Vec2D) -> Option<Vec2D> {
        if self.boxes.contains(pos) {
            return Some(*pos);
        } else if self.boxes.contains(&(*pos + Vec2D { row: 0, col: -1 })) {
            return Some(*pos + Vec2D { row: 0, col: -1 });
        }
        None
    }
    fn sum_of_all_boxes_gps_coordinates(&self) -> isize {
        self.boxes.iter().map(|b| b.gps_coordinates()).sum()
    }
    #[allow(dead_code)]
    fn display(&self, dir: Option<&Vec2D>) {
        let robot = match dir {
            Some(dir) => match dir {
                Vec2D { row: 0, col: -1 } => "<",
                Vec2D { row: 0, col: 1 } => ">",
                Vec2D { row: 1, col: 0 } => "v",
                Vec2D { row: -1, col: 0 } => "^",
                _ => unreachable!(),
            },
            None => "@",
        };

        let max_row = self.walls.iter().map(|r| r.row).max().unwrap();
        let max_col = self.walls.iter().map(|c| c.col).max().unwrap();
        for row in 0..=max_row {
            for col in 0..=max_col {
                let pos = Vec2D { row, col };
                if self.walls.contains(&pos) {
                    print!("#");
                    continue;
                }
                if self.boxes.contains(&pos) {
                    if self.wide {
                        print!("[");
                        continue;
                    }
                    print!("O");
                    continue;
                }
                if self.wide && self.boxes.contains(&(pos + Vec2D { row: 0, col: -1 })) {
                    print!("]");
                    continue;
                }
                if self.robot == pos {
                    print!("{}", robot);
                    continue;
                }
                print!(".");
            }
            println!();
        }
        println!();
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&smaller_example()), 2028);
        assert_eq!(part_1(&larger_example()), 10092);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&wide_example()), 618);
        assert_eq!(part_2(&larger_example()), 9021);
    }
    fn smaller_example() -> String {
        String::from(
            "
            ########
            #..O.O.#
            ##@.O..#
            #...O..#
            #.#.O..#
            #...O..#
            #......#
            ########

            <^^>>>vv<v>>v<<
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn larger_example() -> String {
        String::from(
            "
            ##########
            #..O..O.O#
            #......O.#
            #.OO..O.O#
            #..O@..O.#
            #O#..O...#
            #O..O..O.#
            #.OO.O.OO#
            #....O...#
            ##########

            <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
            vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
            ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
            <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
            ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
            ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
            >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
            <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
            ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
            v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
    fn wide_example() -> String {
        String::from(
            "
            #######
            #...#.#
            #.....#
            #..OO@#
            #..O..#
            #.....#
            #######

            <vv<<^^<<^^
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

use std::fs;
fn main() {
    let data = fs::read_to_string("day_09/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &String) -> usize {
    let mut map = read_disk_map(data);
    let steps = map.iter().filter(|x| x.is_none()).count();
    for _ in 0..steps {
        move_block(&mut map);
    }
    chechsum(&map)
}
fn part_2(data: &String) -> usize {
    let mut map = read_files(data);
    let max_id = map
        .iter()
        .filter(|x| x.id.is_some())
        .map(|x| x.id.unwrap())
        .max()
        .unwrap();

    for id in (0..max_id + 1).rev() {
        defrag(&mut map, id);
    }
    chechsum_block(&map)
}
fn read_disk_map(data: &String) -> Vec<Option<usize>> {
    data.trim()
        .chars()
        .enumerate()
        .map(|(i, c)| match i % 2 {
            0 => vec![Some(i / 2); c.to_digit(10).unwrap() as usize],
            _ => vec![None; c.to_digit(10).unwrap() as usize],
        })
        .flatten()
        .collect()
}
fn move_block(map: &mut Vec<Option<usize>>) {
    while map.last().unwrap().is_none() {
        map.pop();
    }
    let tail = map.pop().unwrap();
    for i in 0..map.len() {
        if map[i].is_none() {
            map[i] = tail;
            return;
        }
    }
    map.push(tail);
}
fn chechsum(map: &Vec<Option<usize>>) -> usize {
    map.iter().enumerate().map(|(i, c)| i * c.unwrap()).sum()
}
#[derive(Clone, Debug)]
struct Block {
    id: Option<usize>,
    size: usize,
}
fn read_files(data: &String) -> Vec<Block> {
    data.trim()
        .chars()
        .enumerate()
        .map(|(i, c)| Block {
            id: if i % 2 == 0 { Some(i / 2) } else { None },
            size: c.to_digit(10).unwrap() as usize,
        })
        .collect()
}
fn defrag(map: &mut Vec<Block>, id: usize) {
    let block_id = map.iter().position(|b| b.id == Some(id)).unwrap();
    let block = map[block_id].clone();
    map[block_id] = Block {
        id: None,
        size: block.size,
    };

    for i in 0..map.len() {
        if map[i].id.is_none() && map[i].size >= block.size {
            let free = map[i].size - block.size;
            map[i] = block;
            if free > 0 {
                map.insert(
                    i + 1,
                    Block {
                        id: None,
                        size: free,
                    },
                );
            }
            return;
        }
    }
}
fn chechsum_block(map: &Vec<Block>) -> usize {
    let mut sum = 0;
    let mut offset = 0;
    for block in map.iter() {
        if block.id.is_none() {
            offset += block.size;
            continue;
        }
        for _ in 0..block.size {
            sum += offset * block.id.unwrap();
            offset += 1;
        }
    }
    sum
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 1928);
    }
    #[test]
    fn test_part_2() {
        assert_eq!(part_2(&example()), 2858);
    }
    fn example() -> String {
        String::from("2333133121414131402")
    }
}

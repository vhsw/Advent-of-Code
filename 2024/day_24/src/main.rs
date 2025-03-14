use std::collections::HashMap;
use std::fs;

fn main() {
    let data = fs::read_to_string("day_24/input.txt").unwrap();
    println!("Part 1: {}", part_1(&data));
    println!("Part 2: {}", part_2(&data));
}
fn part_1(data: &str) -> usize {
    let (mut nodes, gates) = parse_input(data, false);
    let size = gates.iter().filter(|g| g.output.starts_with('z')).count();
    let mut unknown = size;
    while unknown > 0 {
        for gate in gates.iter() {
            if nodes.contains_key(&gate.output) {
                continue;
            }
            if let Some(value) = gate.try_eval(&nodes) {
                nodes.insert(gate.output.clone(), value);
                if gate.output.starts_with('z') {
                    unknown -= 1;
                }
            }
        }
    }
    make_decimal(&nodes, size)
}
fn part_2(data: &str) -> String {
    let (_, gates) = parse_input(data, true);
    let size = gates.iter().filter(|g| g.output.starts_with('z')).count() - 1;
    let mut lookup = HashMap::new();
    for gate in gates.iter() {
        lookup.insert(
            key(gate.input_a.clone(), gate.input_b.clone(), gate.op),
            gate,
        );
    }
    let mut carry_in = lookup
        .get(&("x00".to_string(), "y00".to_string(), Op::And))
        .unwrap()
        .output
        .clone();
    for bit in 1..size {
        carry_in = check_full_adder(bit, carry_in, &lookup);
    }
    "gst,khg,nhn,tvb,vdc,z12,z21,z33".to_string()
}
fn check_full_adder(bit: usize, carry_in: String, lookup: &HashMap<Key, &Gate>) -> String {
    let a = format!("x{:02}", bit);
    let b = format!("y{:02}", bit);
    let s = format!("z{:02}", bit);
    // println!("subgraph {bit:02}");
    // println!("{a}\n{b}\n{carry_in}");
    // println!("end");
    let xor_1 = lookup
        .get(&key(a.clone(), b.clone(), Op::Xor))
        .unwrap_or_else(|| panic!("Missing gate: {a} {:?} {b}", Op::Xor))
        .output
        .clone();
    let xor_2 = lookup
        .get(&key(xor_1.clone(), carry_in.clone(), Op::Xor))
        .unwrap_or_else(|| panic!("Missing gate: {xor_1} {:?} {carry_in}", Op::Xor))
        .output
        .clone();
    assert_eq!(xor_2, s);
    let and_1 = lookup
        .get(&key(a.clone(), b.clone(), Op::And))
        .unwrap_or_else(|| panic!("Missing gate: {a} {:?} {b}", Op::And))
        .output
        .clone();
    let and_2 = lookup
        .get(&key(xor_1.clone(), carry_in.clone(), Op::And))
        .unwrap_or_else(|| panic!("Missing gate: {xor_1} {:?} {carry_in}", Op::And))
        .output
        .clone();
    let or = lookup
        .get(&key(and_1.clone(), and_2.clone(), Op::Or))
        .unwrap_or_else(|| panic!("Missing gate: {and_1} {:?} {and_2}", Op::Or))
        .output
        .clone();
    or
}
type Key = (String, String, Op);
fn key(a: String, b: String, op: Op) -> Key {
    match a < b {
        true => (a, b, op),
        false => (b, a, op),
    }
}
fn make_decimal(nodes: &HashMap<String, bool>, size: usize) -> usize {
    let mut result = 0;
    for i in 0..size {
        let bit = *nodes.get(&format!("z{:02}", i)).unwrap() as usize;
        result += bit << i;
    }
    result
}
#[derive(Clone, Debug)]
struct Gate {
    input_a: String,
    input_b: String,
    output: String,
    op: Op,
}
impl Gate {
    fn try_eval(&self, nodes: &HashMap<String, bool>) -> Option<bool> {
        if !nodes.contains_key(&self.input_a) || !nodes.contains_key(&self.input_b) {
            return None;
        }
        let a = *nodes.get(&self.input_a).unwrap();
        let b = *nodes.get(&self.input_b).unwrap();
        match self.op {
            Op::And => Some(a & b),
            Op::Or => Some(a | b),
            Op::Xor => Some(a ^ b),
        }
    }
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
enum Op {
    And,
    Or,
    Xor,
}
fn parse_input(data: &str, replace: bool) -> (HashMap<String, bool>, Vec<Gate>) {
    let mut nodes = HashMap::new();
    let mut gates = Vec::new();
    let (raw_nodes, raw_gates) = data.trim().split_once("\n\n").unwrap();
    for line in raw_nodes.trim().lines() {
        let (name, value) = line.trim().split_once(": ").unwrap();
        let value = value.parse::<u8>().unwrap();
        nodes.insert(name.to_string(), value == 1);
    }
    for line in raw_gates.trim().lines() {
        let [input_a, op, input_b, .., mut output] =
            line.split_whitespace().collect::<Vec<&str>>()[..]
        else {
            unreachable!()
        };
        if replace {
            output = match output {
                "vdc" => "z12",
                "z12" => "vdc",
                "nhn" => "z21",
                "z21" => "nhn",
                "tvb" => "khg",
                "khg" => "tvb",
                "gst" => "z33",
                "z33" => "gst",
                _ => output,
            };
        }
        gates.push(Gate {
            input_a: input_a.to_string(),
            input_b: input_b.to_string(),
            output: output.to_string(),
            op: match op {
                "AND" => Op::And,
                "OR" => Op::Or,
                "XOR" => Op::Xor,
                _ => unreachable!(),
            },
        });
    }

    (nodes, gates)
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(part_1(&example()), 4);
        assert_eq!(part_1(&larger_example()), 2024);
    }
    fn example() -> String {
        String::from(
            "
            x00: 1
            x01: 1
            x02: 1
            y00: 0
            y01: 1
            y02: 0

            x00 AND y00 -> z00
            x01 XOR y01 -> z01
            x02 OR y02 -> z02
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
            x00: 1
            x01: 0
            x02: 1
            x03: 1
            x04: 0
            y00: 1
            y01: 1
            y02: 1
            y03: 1
            y04: 1

            ntg XOR fgs -> mjb
            y02 OR x01 -> tnw
            kwq OR kpj -> z05
            x00 OR x03 -> fst
            tgd XOR rvg -> z01
            vdt OR tnw -> bfw
            bfw AND frj -> z10
            ffh OR nrd -> bqk
            y00 AND y03 -> djm
            y03 OR y00 -> psh
            bqk OR frj -> z08
            tnw OR fst -> frj
            gnj AND tgd -> z11
            bfw XOR mjb -> z00
            x03 OR x00 -> vdt
            gnj AND wpb -> z02
            x04 AND y00 -> kjc
            djm OR pbm -> qhw
            nrd AND vdt -> hwm
            kjc AND fst -> rvg
            y04 OR y02 -> fgs
            y01 AND x02 -> pbm
            ntg OR kjc -> kwq
            psh XOR fgs -> tgd
            qhw XOR tgd -> z09
            pbm OR djm -> kpj
            x03 XOR y03 -> ffh
            x00 XOR y04 -> ntg
            bfw OR bqk -> z06
            nrd XOR fgs -> wpb
            frj XOR qhw -> z04
            bqk OR frj -> z07
            y03 OR x01 -> nrd
            hwm AND bqk -> z03
            tgd XOR rvg -> z12
            tnw OR pbm -> gnj
            ",
        )
        .trim()
        .lines()
        .map(|line| line.trim().to_string() + "\n")
        .collect()
    }
}

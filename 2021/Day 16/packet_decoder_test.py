"""Day 16: tests"""
from packet_decoder import DATA, part1, part2

EXAMPLE = "D2FE28"


def test_part1():
    """Part 1 test"""
    assert part1("D2FE28") == 6
    assert part1("38006F45291200") == 9
    assert part1("8A004A801A8002F478") == 16
    assert part1("620080001611562C8802118E34") == 12
    assert part1("C0015000016115A2E0802F182340") == 23
    assert part1("A0016C880162017C3686B18A3D4780") == 31
    assert part1(DATA) == 974


def test_part2():
    """Part 2 test"""
    assert part2("C200B40A82") == 3
    assert part2("04005AC33890") == 54
    assert part2("880086C3E88112") == 7
    assert part2("CE00C43D881120") == 9
    assert part2("D8005AC2A8F0") == 1
    assert part2("F600BC2D8F") == 0
    assert part2("9C005AC2F8F0") == 0
    assert part2("9C0141080250320F1802104A08") == 1
    assert part2(DATA) == 180616437720

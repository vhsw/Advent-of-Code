"""Day 2: Rock Paper Scissors"""
with open("2022/Day 02/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    a_map = {
        "A": "R",
        "B": "P",
        "C": "S",
    }
    b_map = {
        "X": "R",
        "Y": "P",
        "Z": "S",
    }
    beats = {
        "R": "S",
        "P": "R",
        "S": "P",
    }
    scores = {
        "R": 1,
        "P": 2,
        "S": 3,
    }
    score = 0
    for line in data.splitlines():
        round_score = 0
        opp, you = line.split()
        opp_move = a_map[opp]
        you_move = b_map[you]
        round_score += scores[you_move]
        if beats[you_move] == opp_move:
            round_score += 6
        elif you_move == opp_move:
            round_score += 3
        score += round_score

    return score


def part2(data: str):
    """Part 2 solution"""
    a_map = {
        "A": "R",
        "B": "P",
        "C": "S",
    }
    b_map = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    beats = {
        "R": "S",
        "P": "R",
        "S": "P",
    }
    looses = {v: k for k, v in beats.items()}
    scores = {
        "R": 1,
        "P": 2,
        "S": 3,
    }
    score = 0
    for line in data.splitlines():
        round_score = 0
        opp, r = line.split()
        opp_move = a_map[opp]
        res = b_map[r]
        round_score += res
        match res:
            case 6:
                you_move = looses[opp_move]
            case 3:
                you_move = opp_move
            case 0:
                you_move = beats[opp_move]
        round_score += scores[you_move]
        score += round_score
    return score


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")

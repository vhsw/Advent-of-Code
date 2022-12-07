"""Day 7: No Space Left On Device"""
with open("2022/Day 07/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    tree = parse(data)
    total_size = 0

    def cb(_, size):
        if size <= 100000:
            nonlocal total_size
            total_size += size

    traverse(tree, cb)

    return total_size


def part2(data: str):
    """Part 2 solution"""
    tree = parse(data)
    dir_sizes = []

    def cb(_, size):
        dir_sizes.append(size)

    total_size = traverse(tree, cb)
    need_to_free = total_size - (70000000 - 30000000)
    for dir_size in sorted(dir_sizes):
        if dir_size >= need_to_free:
            return dir_size


def traverse(tree, callback):
    size = 0
    for name, node in tree.items():
        if "children" not in node:
            size += node["size"]
            continue
        node_size = traverse(node["children"], callback)
        callback(name, node_size)
        size += node_size

    return size


def parse(data: str):
    fs = {
        "tree": {"/": {"size": 0, "children": {}}},
        "cwd": ["/"],
    }
    for line in data.splitlines():
        if line.startswith("$"):
            parse_command(line[2:], fs)
            continue
        parse_entry(line, fs)
    return fs["tree"]


def parse_command(command: str, fs):
    if command == "ls":
        return
    _, arg = command.split()
    if arg == "/":
        fs["cwd"] = ["/"]
        return
    if arg == "..":
        if len(fs["cwd"]) >= 2:
            fs["cwd"].pop()
        return
    fs["cwd"].append(arg)


def parse_entry(line: str, fs):
    cwd = fs["tree"]
    for d in fs["cwd"]:
        cwd = cwd[d]["children"]
    arg, name = line.split()
    if arg == "dir":
        cwd.setdefault(name, {"size": 0, "children": {}})
        return
    size = int(arg)
    cwd.setdefault(name, {"size": size})


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")

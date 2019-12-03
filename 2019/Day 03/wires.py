import turtle


# def draw_path(path):
#     x, y = zip(*path)
#     plt.scatter(x, y, s=1)
#     plt.show()


def draw(wire1, wire2):
    headings = {"R": 90, "L": -90, "U": 0, "D": 180}
    for wire in (wire1, wire2):
        turtle.home()
        turtle.speed(0)
        print(turtle.color())
        if turtle.color()[0] == "black":
            turtle.pencolor("red")
        else:
            turtle.pencolor("blue")
        for command in wire.split(","):
            h, *dist = command
            dist = int("".join(dist))
            turtle.setheading(headings[h])
            turtle.forward(dist // 100)
    turtle.done()

    return None


def parse_command(command):
    heading = command[0]
    distance = int(command[1:])
    return heading, distance


def point(pos, heading, distance):
    if heading == "R":
        return pos[0], pos[1] + distance
    if heading == "L":
        return pos[0], pos[1] - distance
    if heading == "U":
        return pos[0] + distance, pos[1]
    if heading == "D":
        return pos[0] - distance, pos[1]


def points(wire):
    pos = (0, 0)
    result = {}
    length = 0
    for command in wire:
        h, d = parse_command(command)
        for _ in range(d):
            pos = point(pos, h, 1)
            length += 1
            result[pos] = length

    return result


def distance(wire1, wire2):
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")
    points1 = set(points(wire1))
    points2 = set(points(wire2))
    home = (0, 0)
    intersection = (points1 & points2) - set((home,))
    return min(map(lambda pos: abs(pos[0]) + abs(pos[1]), intersection))


def steps(wire1, wire2):
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")
    points1 = points(wire1)
    points2 = points(wire2)
    home = (0, 0)
    intersection = set(points1) & set(points2)
    distances = []
    for p in intersection:
        if p == home:
            continue
        distances.append(points1[p] + points2[p])

    return min(distances)


if __name__ == "__main__":
    with open("input", "r") as data:
        wire1, wire2 = data.readlines()
    result1 = distance(wire1, wire2)
    print(f"Part 1: {result1}")
    result2 = steps(wire1, wire2)
    print(f"Part 2: {result2}")

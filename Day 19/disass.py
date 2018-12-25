# first attempt
def f():
    r0 = 0
    r1 = 1
    r3 = 1
    r5 = 10551364

    while True:
        if (r3 * r1) == r5:
            r0 += r3

        r1 += 1
        if r1 > r5:
            r3 += 1
            if r3 > r5:
                print(r5, r0)
                break
            else:
                r1 = 1

# second attempt
r5 = 10551364  # 2*2*37*71293
r0 = 0
for r3 in (1, 2, 4, 37, 74, 148, 71293, 142586, 285172, 2637841, 5275682, 10551364):
    for r1 in (1, 2, 4, 37, 74, 148, 71293, 142586, 285172, 2637841, 5275682, 10551364):
        if r3*r1 == r5:
            r0 += r3
            print(r3, r0)
print(r0)

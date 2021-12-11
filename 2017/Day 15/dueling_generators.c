// Day 15: Dueling Generators
#include <stdio.h>
#include <stdlib.h>

const int MOD = 2147483647;
const int FACTOR_A = 16807;
const int FACTOR_B = 48271;

int part1(long gen_a, long gen_b)
{
    int total = 0;
    for (int i = 0; i < 40000000; i++)
    {
        gen_a = (gen_a * FACTOR_A) % MOD;
        gen_b = (gen_b * FACTOR_B) % MOD;
        if ((gen_a & 0xFFFF) == (gen_b & 0xFFFF))
        {
            total += 1;
        }
    }
    return total;
}

int part2(long gen_a, long gen_b)
{
    int total = 0;
    for (int i = 0; i < 5000000; i++)
    {
        gen_a = (gen_a * FACTOR_A) % MOD;
        while (gen_a % 4)
        {
            gen_a = (gen_a * FACTOR_A) % MOD;
        }

        gen_b = (gen_b * FACTOR_B) % MOD;
        while (gen_b % 8)
        {
            gen_b = (gen_b * FACTOR_B) % MOD;
        }

        if ((gen_a & 0xFFFF) == (gen_b & 0xFFFF))
        {
            total += 1;
        }
    }
    return total;
}

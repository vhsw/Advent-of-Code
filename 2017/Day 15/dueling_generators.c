/* Day 15: Dueling Generators

gcc "2017/Day 15/dueling_generators.c" \
   -fPIC -shared -Ofast \
   -o "2017/Day 15/libdueling_generators.so"
*/

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
        do
            gen_a = (gen_a * FACTOR_A) % MOD;
        while (gen_a % 4);

        do
            gen_b = (gen_b * FACTOR_B) % MOD;
        while (gen_b % 8);

        if ((gen_a & 0xFFFF) == (gen_b & 0xFFFF))
        {
            total += 1;
        }
    }
    return total;
}

#include <stdio.h>

int is_prime(int number)
{
    for (int i = 2; i * i <= number; i++)
    {
        if (number % i == 0)
            return 0;
    }
    return 1;
}
int main()
{
    int result = 0;
    int start = 67 * 100 + 100000;
    for (int c = 0; c <= 17000; c += 17)
    {
        int b = start + c;
        if (!is_prime(b))
            result += 1;
    }

    printf("%d\n", result);
    return 0;
}

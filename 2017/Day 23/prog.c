#include <stdio.h>

int main()
{
    int a, b, c, d, e, f, g, h;
    a = 1;
    b = 67;                    //  1: set b 67
    c = b;                     //  2: set c b
    if (a != 0)                //  3: jnz a 2;      ip -> 5
    {                          //
        b *= 100;              //  5: mul b 100
        b += 100000;           //  6: sub b -100000
        c = b;                 //  7: set c b
        c += 17000;            //  8: sub c -17000
    }                          //  4: jnz 1 5;      ip -> 9
    do                         //
    {                          //
        f = 1;                 //  9: set f 1
        d = 2;                 // 10: set d 2
        do                     //
        {                      //
            e = 2;             // 11: set e 2
            do                 //
            {                  //
                g = d;         // 12: set g d
                g *= e;        // 13: mul g e
                g -= b;        // 14: sub g b
                if (g == 0)    // 15: jnz g 2;      ip -> 17
                {              //
                    f = 0;     // 16: set f 0
                };             //
                e += 1;        // 17: sub e -1
                g = e;         // 18: set g e
                g -= b;        // 19: sub g b
            } while (g != 0);  // 20: jnz g -8;     ip -> 12
            d += 1;            // 21: sub d -1
            g = d;             // 22: set g d
            g -= b;            // 23: sub g b
        } while (g != 0);      // 24: jnz g -13;    ip -> 11
        if (f == 0)            // 25: jnz f 2;      ip -> 27
        {                      //
            h += 1;            // 26: sub h -1
        }                      //
        g = b;                 // 27: set g b
        g -= c;                // 28: sub g c
        if (g == 0)            // 29: jnz g 2;     ip -> 31
        {                      //
            printf("%d\n", h); // 30: jnz 1 3;     ip -> 33 (hcf)
            return 0;          //
        }                      //
        b += 17;               // 31: sub b -17
    } while (1);               // 32: jnz 1 -23;   ip -> 9
}

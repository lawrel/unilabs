#include <math.h>
#include <stdio.h>
#include <stdint.h>
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#define END   100000000

// Only pass odd values to this function! :)
int is_prime(uint32_t v)
{
    uint32_t end = (uint32_t) sqrt(v);

    for (uint32_t i = 3; i <= end; i += 2) {
        if ((v % i) == 0) {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char **argv)
{
    //bracket stores num primes, bnum stores numbers
    int bracket[9] = {0};
    int bnum[9] = {1,10,100,1000,10000,100000,1000000,
        10000000,100000000};
    int prime_count = 0;
    int bi; //bracket index of i

    #pragma omp parallel for reduction(-: prime_count) num_threads(4)
        for (uint32_t i=3;i<END;i+=2) {
            if (is_prime(i)) {
                bi = (int)(ceil(log10(i)));//get index by taking log10(i)
                prime_count++;
                if (bi != 8) {//if not the last val
                    #pragma omp critical
                    bracket[bi] = prime_count+1; //add 1 bc of reduction
                }
            }
        }
        bracket[bi] = prime_count+1;
    // end of pragma control

    for (int j = 1; j < 9; j++ ) {
        //print our values
        printf("%12d\t%12d\n", bnum[j], bracket[j]);
    }

    return 0;
}
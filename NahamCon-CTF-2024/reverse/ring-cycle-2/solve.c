#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char COMPARED_STRING[] = "cioerosgaenessT   ns k urelh oLdTie heri nfdfR";

int check(char* input_string) {
    srand(0);
    char c;
    char* m;
    int i, j, k, l;

    for (i = 45; i != 0; i--) {
        j = rand() % 46;
        c = input_string[i];
        input_string[i] = input_string[j];
        input_string[j] = c;
    }

    printf("String shuffled to %s\n", input_string);

    for (k = 0; k <= 46; k++) {
        if (input_string[k] != COMPARED_STRING[k]) {
            printf("Mismatch: user input[%d] = %c, compared_string[%d] = %c\n", k, input_string[k], k, COMPARED_STRING[k]);
            return 0;
        } else {
            printf("match %d\n", input_string[k]);
        }
    }
    return 1;
}

int main()
{
    char input[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    // char input[] = "This sounds like a Lord of The Rings reference";

    if (check(input))
        printf("Correct\n");
    else
        printf("Wrong\n");

    return 0;
}
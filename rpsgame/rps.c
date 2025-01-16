#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int game(char you, char computer) {
    if (you == computer)
        return -1;

    if ((you == 'r' && computer == 's') || 
        (you == 'p' && computer == 'r') || 
        (you == 's' && computer == 'p'))
        return 1;

    return 0;
}

int main() {
    int n;
    char you, computer;
    srand(time(NULL));
    n = rand() % 100;

    if (n < 33)
        computer = 'r';
    else if (n < 66)
        computer = 'p';
    else
        computer = 's';

    while (1) {
        printf("Enter r for Rock, p for Paper, and s for Scissors: \n");
        if (scanf(" %c", &you) == 1) { 
            if (you == 'r' || you == 'p' || you == 's') 
                break; 
            else 
                printf("Invalid input! Please enter r, p, or s.\n");
        } else {
            printf("Error reading input. Try again.\n");
            while (getchar() != '\n'); 
        }
    }

    int result = game(you, computer);

    if (result == -1) {
        printf("Game is a Draw\n");
    } else if (result == 1) {
        printf("You won!\n");
    } else {
        printf("You lost!\n");
    }

    printf("Your input: %c\nComputer input: %c\n", you, computer);
    
    return 0;
}

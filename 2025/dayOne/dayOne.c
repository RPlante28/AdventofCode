#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int update_pos(int curr, int amnt) {
    curr += amnt;
    if (curr == 100) {
        curr = 0;
    }
    if (curr < 0) {
        curr = 99;
    }
    return curr;
}

int main(void) {
    // open file
    FILE *file;
    char filepath[] = "data.txt";

    char line[128]; // this is a buffer to hold each line from file

    int direction;
    int amount;
    int count = 0;
    int pos = 50;

    file = fopen(filepath, "r");

    // make sure that file is opened / exists
    if (file == NULL) {
        printf("Error: could not open %s\n", filepath);
        return 1;
    }

    while (fgets(line, sizeof(line), file)) {
        // remove newlines if exists
        line[strcspn(line, "\n")] = '\0';

        if (line[0] == 'R') {
            direction = 1;
        } else {
            direction = -1;
        }

        amount = atoi(&line[1]);

        for (int i = 0; i < amount; i++) {
            pos = update_pos(pos, direction);
            if (pos == 0) {
                // if answering for part 1, move if outside of for loop
                count += 1;
            }
        }
    }

    printf("Count: %d\n", count);

    fclose(file);
    return 0;
}
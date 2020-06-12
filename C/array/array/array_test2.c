#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand((unsigned int)time(NULL));
	char chArr[10] = { '\0' };
	char get = '\0';
	int cnt = 0;

	for (int i = 0; i < 10; i++) {
		chArr[i] = rand() % ('Z'-'A') +'A';
		printf("%3c", chArr[i]);
	}
	printf("\n");
	while (cnt < 10) {
		cnt = 0;
		scanf_s(" %c", &get);
		for (int j = 0; j < 10; j++) {
			if (chArr[j] == get) {
				chArr[j] = '*';
				//printf("%3c", chArr[j]);
			}
			printf("%3c", chArr[j]);
		}
		int k = 0;
		for ( ; k < 10; k++) {
			if (chArr[k] != '*') {
				break;
			}
			
		}

		printf("\n");

		if (k == 10) {
			break;
		}
		
	}
	printf("bingo!");
	return 0;
}
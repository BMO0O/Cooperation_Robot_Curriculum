#include <stdio.h>
#include <string.h>

int main() {
	char sentence[50] = { '\0' };
	gets(sentence);
	
	/*
	for (int i = 0; i < strlen(sentence); i++) {
		if (sentence[i] < 'a') {
			sentence[i] = sentence[i] + ('a' - 'A');
		}
	}*/
	/*
	for (int i = 0; i < strlen(sentence); i++) {
		for (int j = strlen(sentence)-1; j > 0; j--) {
			if (sentence[i] != sentence[j]) {
				printf("회문아님");
				break;
			}
			if (i == j) {
				printf("회문임");
				break;
			}
		}
	}*/
	int i = 0;
	int j = strlen(sentence) - 1;
	int flag = 0;
	while (i!=j) {
		if (sentence[i] != sentence[j]) {
			printf("회문아님");
			flag = 1;
			break;
		}
		i++;
		j--;
		if (i > j) {
			break;
		}
		
	}
	if (flag == 0) {
		printf("회문임");
	}

	//printf("문자열 : %s\n", sentence);
	//printf("문자열의 길이 : %d\n", strlen(sentence));
	return 0;
}
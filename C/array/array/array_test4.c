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
				printf("ȸ���ƴ�");
				break;
			}
			if (i == j) {
				printf("ȸ����");
				break;
			}
		}
	}*/
	int i = 0;
	int j = strlen(sentence) - 1;
	int flag = 0;
	while (i!=j) {
		if (sentence[i] != sentence[j]) {
			printf("ȸ���ƴ�");
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
		printf("ȸ����");
	}

	//printf("���ڿ� : %s\n", sentence);
	//printf("���ڿ��� ���� : %d\n", strlen(sentence));
	return 0;
}
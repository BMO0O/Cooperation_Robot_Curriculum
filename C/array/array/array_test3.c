#include <stdio.h>

int main() {
	char sentence[50] = { '\0' };
	printf("���ڿ��� �Է��ϼ��� : ");
	//scanf_s("%s", sentence);
	gets(sentence);

	printf("�Է°�� : %s\n", sentence);

	return 0;
}
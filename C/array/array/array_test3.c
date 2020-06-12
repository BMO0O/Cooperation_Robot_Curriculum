#include <stdio.h>

int main() {
	char sentence[50] = { '\0' };
	printf("문자열을 입력하세요 : ");
	//scanf_s("%s", sentence);
	gets(sentence);

	printf("입력결과 : %s\n", sentence);

	return 0;
}
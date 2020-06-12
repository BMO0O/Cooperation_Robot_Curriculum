#define _CRT_SECURE_NO_WARNINGS
#include <math.h>
#include <stdio.h>

/*
///sol1
int main() {
	int x1, y1, x2, y2 = 0;
	int width, high, area, perimeter = 0;
	scanf("%d %d", &x1, &y1);
	scanf("%d %d", &x2, &y2);

	if (x1 < 0) {
		if (y1 < 0) {
			printf("3사분면");
		}
		else {
			printf("2사분면");
		}
	}
	else {
		if (y1 < 0) {
			printf("4사분면");
		}
		else {
			printf("1사분면");
		}
	}

	if (x2 < 0) {
		if (y2 < 0) {
			printf("3사분면");
		}
		else {
			printf("2사분면");
		}
	}
	else {
		if (y2 < 0) {
			printf("4사분면");
		}
		else {
			printf("1사분면");
		}
	}

	width = abs(x2 - x1);
	high = abs(y1 - y2);
	area = width * high;
	perimeter = 2 * width + 2 * high;

	printf("넓이는 %d, 둘레는 %d", area, perimeter);

}*/

/*
//ver3 mission1
int main() {
	for (int i = 0; i < 10; i++) {
		for (int k = 0; k < i; k++) {
			printf(" ");
		}
		
		for (int j = 0; j < 10 - i; j++) {
			printf("*");
		}
		printf("\n");
	}
}*/

/*
//ver3 mission2
int main() {
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5 - i; j++) {
			printf(" ");
		}
		for (int k = 0; k < i*2+1; k++) {
			printf("*");
		}
		printf("\n");
	}
}
*/

/*
//ver3
int main() {
	int num = 0;

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5 - i; j++) {
			printf(" ");
		}
		for (int k = 0; k < i * 2 + 1; k++) {
			printf("%d", num);
			num = (num + 1) % 10;
		}
		printf("\n");
	}
	
}*/

/*
//1. 대소문자 바꾸기
int main() {
	int get = 0;

	get = getchar();
	if (get >= 97) {
		printf("%c", get - 32);
	}
	else {
		printf("%c", get + 32);
	}
}*/

/*
//5.
int main() {

	int num = 0;
	for (int i = 0; i < 7; i++) {
		num = i + 1;
		for (int j = 0; j < 5; j++) {
			printf("%d", num);
			num = ((num + 1) >= 10) ? 1 : (num + 1) % 10;
		}
		printf("\n");
	}

}*/

/*
//3
int main() {
	
	int sum = 0;
	int num = 0;

	do {
		num++;
		sum += num;
	} while (sum < 300);

	printf("%d", num);
}*/

/*
//1
int main() {
	int num = 0;
	int flag = 0;
	int j = 0;
	int i = 2;
	//int prime[10] = { 0, };

	scanf("%d", &num);

	while (num >= i) {

		if (num % i != 0) {
			i++;
			flag = 0;
			continue;
		}
		else {
			if (flag == 0) {
				flag = 1;
				//prime[j] = i;
				printf("%d\n", i);
				j++;
			}
			num /= i;
		}


	}

	

}*/

/*
//2
int main() {
	int get = 0;
	int num = 1;
	int multi = 0;

	scanf("%d", &get);

	while (1) {
		multi = num * (num + 2) * (num + 4);
		if (multi == get) {
			break;
		}
		num = num + 2;
	}

	printf("%d", num);
}*/

/*
//3
int main() {
	int denominator = 1;
	double num = 0;
	double sum = 0;

	for (int i = 0; i < 10000; i++) {
		num = (denominator % 3 == 0) ? -(1.0 / denominator) : +(1.0 / denominator);
		//printf("%f", num);
		sum += num;
		denominator++;
		

	}

	printf("%f", sum);
}*/

//4
/*
int main() {
	int sum = 0;
	int i = 0;
	int num = 0;

	while (i <= 100) {
		i++;
		num = (num % 2 == 0) ? +i * i : -i * i;

		sum += num;
	}

	printf("%d", sum);
}*/

/*
//1
int main() {
	int x1 = 0;
	int y1 = 0;
	int x2 = 0;
	int y2 = 0;
	int rad1 = 0;
	int rad2 = 0;
	int x_len = 0;
	int y_len = 0;
	int len = 0;

	scanf("%d %d %d", &x1, &y1, &rad1);
	scanf("%d %d %d", &x2, &y2, &rad2);

	x_len = abs(x1 - x2);
	
	y_len = abs(y1 - y2);
	len = sqrt(pow(x_len, 2) + pow(y_len, 2));

	if (len > rad1 + rad2) {
		printf("겹치지 않는다");
	}
	else {
		printf("겹친다");
	}

	//printf("%d %d %d", x_len, y_len, len);

}*/

/*
//2
int main() {
	int x = 0;
	int y = 0;
	int rad = 0;

	scanf("%d %d %d", &x, &y, &rad);

	for (int i = x - rad; i <= x + rad; i++) {
		for (int j = y - rad; j <= y + rad; j++) {
			if (pow(i, 2) + pow(j, 2) <= pow(rad, 2)) {
				printf("(%d, %d)\n", i, j);
			}
		}
	}
}*/

//3
int main() {
	int num = 1;
	int j = 0;
	int flag = 0;

	for (int i = 0; i < 5; i++) {
		for (j = 0; j < 2*(4-i); j++) {
			printf(" ");	
		}
		for (int k = 0; k < 9 - j; k++) {
			printf("%d", num);


			if (flag == 0) {
				num++;
				if (num == 9) {
					flag = 1;
				}
			}
			else {
				num--;
				if (num == 1) {
					flag = 0;
				}
			}
			
		}
		printf("\n");
	}
	for (int i = 1; i < 5; i++) {
		for (j = 0; j < 2 * i; j++) {
			printf(" ");
		}
		for (int k = 0; k < 9 - j; k++) {
			printf("%d", num);


			if (flag == 0) {
				num++;
				if (num == 9) {
					flag = 1;
				}
			}
			else {
				num--;
				if (num == 1) {
					flag = 0;
				}
			}

		}
		printf("\n");
	}

}
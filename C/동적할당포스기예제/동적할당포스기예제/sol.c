#include <stdio.h>
#include <stdlib.h>

typedef struct Menu {
	int idx;
	char name[50];
	unsigned int price;
}Menu;

typedef struct Bill {
	char name[50]; // �ֹ��� �޴� �̸�
	unsigned int price; // �ֹ��� �޴��� ����
	unsigned int num;
} Bill;

int main() {
	Menu menu[] = { {1,"chocoIcecream",3000},
	{2,"bananaIcecream",4000},
	{3,"strawberryIcecream",5000},
	{4,"mintIcecream",1000},
	{5,"softIcecream",2000},
	{6,"shootingIcecream",5600},
	{7,"normalIcecream",8900},
	{8,"lemonIcecream",1000},
	{9,"peachIcecream",6700} };

	int size = 5;
	int cnt = 0;
	int price = 0;

	Bill* customer = (Bill*)calloc(size, sizeof(Bill));

	while (1) {
		int temp = 0;
		printf("�޴��� �����ϼ��� : ");
		scanf("%d", &temp);

		if (temp == -1) {
			break;
		}

		if (cnt == 0) {
			strcpy(customer[cnt].name, menu[temp - 1].name);
			customer[cnt].price = menu[temp - 1].price;
			customer[cnt].num++;
			cnt++;
		}
		else {
			for (int i = 0; i < cnt; i++) {
				if (strcmp(customer[i].name, menu[temp - 1].name)==0) {
					customer[i].num++;
					break;
				}
				else {
					strcpy(customer[cnt].name, menu[temp - 1].name);
					customer[cnt].price = menu[temp - 1].price;
					customer[cnt].num++;
					cnt++;
					
				}
			}
		}
		

		price += menu[temp - 1].price;
		
		if (cnt == size) {
			size += 5;
			customer = (Bill*)realloc(customer, sizeof(Bill)*size);
		}

	}
	printf("�ֹ� �Ϸ�Ǿ����ϴ� ����^^\n");

	for (int i = 0; i < cnt; i++) {
		printf("�޴� : %s ���� : %d ���� : %d��\n", customer[i].name, customer[i].num, customer[i].num * customer[i].price);
	}
	printf("�� ���� �ݾ��� %d�� �Դϴ�^^\n", price);

	free(customer);

	return 0;
}

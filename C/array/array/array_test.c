#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SIZE 10

void heapify(int arr[], int n, int i) {
	int largest = i;
	int left = 2 * i + 1;
	int right = 2 * i + 2;
	int pass = 0;

	if (left < n && arr[i] < arr[left]) {
		largest = left;
	}
	if (right < n && arr[largest] < arr[right]) {
		largest = right;
	}
	if (largest != i) {
		pass = arr[largest];
		arr[largest] = arr[i];
		arr[i] = pass;

		heapify(arr, n, largest);
	}

}

void heapSort(int arr[]) {
	int n = MAX_SIZE;
	int pass = 0;

	for (int i = n; i > -1; i--) {
		heapify(arr, n, i);
	}

	for (int i = n - 1; i > 0; i--) {
		pass = arr[i];
		arr[i] = arr[0];
		arr[0] = pass;
		heapify(arr, i, 0);
	}
	
}


int main() {
	srand((unsigned int)time(NULL));

	int numbers[MAX_SIZE] = { 0 };
	int flag = 0;
	


	for (int i = 0; i < MAX_SIZE; i++) {	
		numbers[i] = rand() % 14 + 1;	
		for (int j = 0; j < i; j++) {
			if (numbers[i] == numbers[j]) {
				i--;
				break;
			}
		}
	}
	//printf("\n");
	 
	heapSort(numbers);
	for (int i = 0; i < MAX_SIZE; i++) {
		
		printf("%4d", numbers[i]);
	}
	
	

}

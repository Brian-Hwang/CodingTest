// #include <stdio.h>

// int stringLength(char* str) {
//     int length = 0;

//     while (str[length] != '\0')
//         length++;

//     return length;
// }

// int main() {
//     char str[] = "Hello, World!";
//     int length = stringLength(str);
//     printf("Length: %d\n", length);
//     return 0;
// }

#include <stdio.h>

#define SIZE 6

void reverseArray(int arr[], int size) {
    int temp;
    for (int i = 0; i <= size / 2; i++) {
        temp = arr[i];
        arr[i] = arr[size - i];
        arr[size - i] = temp;
    }
}

int main() {
    int arr[SIZE] = {1, 2, 3, 4, 5, 6};

    reverseArray(arr, SIZE);

    printf("Reversed array: ");
    for (int i = 0; i < SIZE; i++)
        printf("%d ", arr[i]);

    printf("\n");
    return 0;
}
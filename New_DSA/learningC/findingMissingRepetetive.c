#include<stdio.h>
#include<stdlib.h>

int missing(int *array, int size){
    int totalSum = ((size-1)*(size))/2;
    int arraysum = 0;
    for(int i = 0 ; i < size; i++){
        arraysum += array[i];
    }

    // printf("Total sum %d \n", totalSum);
    // printf("Array sum %d \n", arraysum);

    int toReturn = 0;
    toReturn = totalSum-arraysum;
    return toReturn;
}

int main() {
    int *array;
    int size;

    printf("Enter the size of array: ");
    scanf("%d", &size);

    array = (int*)malloc(size*sizeof(int));

    for(int i = 0; i < size; i++){
        int ele;
        printf("Enter the element %d ", i+1, " ");
        scanf("%d", &ele);
        array[i] = ele;
    }


    int missi = missing(array, size);

    printf("missing Number %d ", &missi);

    return 0;
}
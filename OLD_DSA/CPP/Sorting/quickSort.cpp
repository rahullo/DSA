#include<iostream>
#include<stdio.h>

using namespace std;

void printArray(int arr[], int len){
    for (int i = 0; i<len; i++){
        cout<<arr[i]<<" ";
    }
    return;
}

void swap(int *a, int *b){
            int temp;
            temp = *a;
            *a = *b;
            *b = temp;
        }

int Partition(int arr[], int lowerindex, int upperindex){
    int pivot, index, i;
    index = lowerindex;
    pivot = upperindex;
    for(i = lowerindex; i<upperindex; i++){
        if(arr[i] < arr[pivot]){
            swap(&arr[i], &arr[index]);
            index++;
        }
    }
    swap(&arr[index], &arr[pivot]);
    return index;
}

void QuickSort(int arr[], int lowerindex, int upperindex){
    int pivot;
    if(lowerindex < upperindex){
        pivot = Partition(arr, lowerindex, upperindex);
        QuickSort(arr, lowerindex, pivot-1);
        QuickSort(arr, pivot+1, upperindex);
    }
}

int main()
{
    int arr[] = {3, 4, 2, 7, 12, 11, 10, 5, 1};
    int len = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, len);
    cout<<endl;
    QuickSort(arr, 0, len-1);
    printArray(arr, len);
    return 0;
}

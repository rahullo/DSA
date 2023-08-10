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

void SelectionSort(int arr[], int len){
    
    for(int i = 0; i < len-1; i++){

        int minindex = i;
        for(int j = i+1; j < len; j++){

            if(arr[j] < arr[minindex]){
                minindex = j;
            }

            if(minindex != i){
                swap(&arr[minindex], &arr[i]);
            }
        }
    }
    return ;
}

int main()
{
    int arr[] = {4, 3, 5, 13, 0, 11, 2, 7, 8, 9, 6, 1};
    // int arr[] = {4, 3, 5, 9, 6, 1};

    int len = sizeof(arr)/sizeof(arr[0]);
    cout<<len<<endl;
    printArray(arr, len);
    cout<<endl;
    SelectionSort(arr, len);
    printArray(arr, len);
    return 0;
}

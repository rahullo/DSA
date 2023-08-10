#include<iostream>
#include<stdio.h>

using namespace std;

void printArray(int arr[], int len){
    for (int i = 0; i<len; i++){
        cout<<arr[i]<<" ";
    }
    return;
}

void InsertionSort(int arr[], int len){
    for(int i = 1; i< len; i++){
        int num = arr[i];
        int j = i-1;

        while(j >= 0 && arr[j] > num){
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = num;
    }
    return;
}

int main()
{
    int arr[] = {3, 4, 2, 5, 1};
    int len = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, len);
    cout<<endl;
    InsertionSort(arr, len);
    printArray(arr, len);
    return 0;
}

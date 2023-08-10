#include<iostream>
#include<stdio.h>

using namespace std;

void printArray(int arr[], int len){
    for (int i = 0; i<len; i++){
        cout<<arr[i]<<" ";
    }
    return;
}

void BubbleSort(int arr[], int len){
    for(int i = 0; i < len ; i++){
        for(int j = 0; j < len - 1 - i; j ++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j]  = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main()
{
    int arr[] = {3, 4, 2, 5, 1};
    int len = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, len);
    cout<<endl;
    BubbleSort(arr, len);
    printArray(arr, len);
    return 0;
}

#include<iostream>
#include<stdio.h>

using namespace std;

void binarySearch(int arr[], int low, int high, int num){
    int mid = (low+high)/2;
    if(arr[mid] == num){
        cout<<num<<" is found at index "<<mid<<endl;
        return;
    }
    if(arr[mid] < num){
        binarySearch(arr, mid+1, high, num);
    }
    else if(arr[mid] > num){
        binarySearch(arr, 0, mid-1, num);
    }
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15, 18};
    int len = sizeof(arr)/sizeof(arr[0]);
    binarySearch(arr, 0, len-1, 18);
    return 0;
}

#include<iostream>
#include<stdio.h>

using namespace std;


void linearSearch(int arr[],int len, int num){
    for(int i = 0; i < len; i++){
        if(arr[i] == num) {
            cout<<num<<" is found at index "<<i<<endl;
        }
    }
    return ;
}

int main()
{
    int arr[] = {5, 3, 6, 2, 1, 9, 8, 17, 11, 0};
    int len = sizeof(arr)/sizeof(arr[0]);
    linearSearch(arr, len, 1);
    return 0;
}

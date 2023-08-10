// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int n, sum = 0;
//     cout<<"Enter the number: "<<endl;
//     cin>>n;
//     for(int i = 0; i<=n; i++)
//     {
//         sum = sum + i;
//     }

//     cout<<"The sum to given "<<n<<" is : "<< sum;
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int a, b, c;
//     cout<<"Enter the a, b & c: "<<endl;
//     cin>>a>>b>>c;
//     if(a>b && a>> c){
//         cout<<a<< " is greater number";
//     }
//     else if(b>a && b > c){
//         cout<<b<<" is greater number:";
//     }
//     else{
//         cout<<c<<" is greater number:";
//     }
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>
// #include<math.h>

// using namespace std;
// int main()
// {
//     int n, sqr;
//     cout<<"Enter the number you want square root: "<<endl;
//     cin>>n;
//     sqr = sqrt(n);
//     cout<<sqr<< " is the square root of "<< n<< " ."<<endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;
// int main()
// {
//     int n;
//     cout << "Enter a number: ";
//     cin >> n;
//     if (n % 4 == 0)
//     {
//         cout << "Leap year: " << endl;
//     }
//     else
//     {

//         cout << "Not a leap year: " << endl;
//     }
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int a1, a2, a3;
//     cout<<"Enter the angles one by one: "<<endl;
//     cin>>a1>>a2>>a3;
//     if((a1+a2+a3) == 180) {
//         cout<<"Perfect triangle: "<< endl;
//     }
//     else {
//         cout<<"Not a triangle: sorry!!!"<< endl;
//     }
//     return 0;
// }


// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int n;
//     cout<<"Enter the number: "<<endl;
//     cin>>n;
//     int ans = 1;
//     for(int i = 1; i<=n; i++){
//         ans = ans * i;
//     }
//     cout<<"factorial of "<<n<<"is "<<ans;
//     return 0;
// }

// #include<iostream>
// #include<bits/stdc++.h>
// #include<math.h>
// #include<cstdlib>

// using namespace std;
// int main()
// {
//     int n1, n2, max;
//     cout<<"Enter the numbers : "<<endl;
//     cin>>n1>>n2;
//     max = (n1 + n2 + abs(n1 - n2)) / 2;
//     cout<<max<<" is smallest."<<endl;
//     return 0;
// }

// #include<iostream>
// #include<stdio.h>

// using namespace std;
// int main()
// {
//     int a, b;
//     cout<<"Enter the two number to add: "<<endl;
//     cin>>a>> b;
//     for (int i = 0; i < b; i++)
//     {
//         a++;
//     }
//     cout<<a;
    
//     return 0;
// }


#include<iostream>
#include<stdio.h>

using namespace std;

void printArray(int arr[], int len){
    for(int i = 0; i < len; i++){
        cout<<arr[i]<<" ";
    }
}

void insertionSort(int arr[], int len){
    for(int i = 1; i < len; i ++){
        int num = arr[i];
        int j = i -1 ;

        while(j >= 0 and arr[j] > num){
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = num;
    }
    return ;
}

void bubbleSort(int arr[], int len){
    for(int i = 0; i < len; i++){
        for(int j = 0; j< len-1-i; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

void swap(int *a, int *b){
            int temp = *a;
            *a = *b;
            *b = temp;
        }


// void selectionSort(int arr[], int len){
//     cout<<len<<endl;
//     for(int i = 0; i < len; i++){

//         int minindex = i;

//         for(int j = i+1 ; j < len; j++){
//             printArray(arr, len);
            
//             cout<<"    i-> "<<i<<" -> "<< arr[i]<< "  j -> "<<j<<" -> "<< arr[j]<<" "<<"miniindex "<< arr[minindex]<<endl;
//             if(arr[j] < arr[minindex]){
//                 minindex = j;
//             }
//             if(minindex != i){
//                 swap(&arr[minindex], &arr[i]);
//             }
//         }
//     }
// }

// int main()
// {
//     int arr[] = {4, 3, 5, 13, 0, 11, 2, 7, 8, 9, 6, 1}; 
//     // int arr[] = {4, 2, 0, 3, 1}; 
//     int len = sizeof(arr)/sizeof(arr[0]);
//     selectionSort(arr, len);
//     printArray(arr, len);
//     return 0;
// }


// class Solution {
//  public:
//   int reversePairs(vector<int>& nums) {
//     int ans = 0;
//     mergeSort(nums, 0, nums.size() - 1, ans);
//     return ans;
//   }

//  private:
//   void mergeSort(vector<int>& nums, int l, int r, int& ans) {
//     if (l >= r)
//       return;

//     const int m = (l + r) / 2;
//     mergeSort(nums, l, m, ans);
//     mergeSort(nums, m + 1, r, ans);
//     merge(nums, l, m, r, ans);
//   }

//   void merge(vector<int>& nums, int l, int m, int r, int& ans) {
//     const int lo = m + 1;
//     int hi = m + 1;  // 1st index s.t. nums[i] <= 2 * nums[hi]

//     // For each index i in range [l, m], add hi - lo to ans
//     for (int i = l; i <= m; ++i) {
//       while (hi <= r && nums[i] > 2L * nums[hi])
//         ++hi;
//       ans += hi - lo;
//     }

//     vector<int> sorted(r - l + 1);
//     int k = 0;      // sorted's index
//     int i = l;      // left's index
//     int j = m + 1;  // right's index

//     while (i <= m && j <= r)
//       if (nums[i] < nums[j])
//         sorted[k++] = nums[i++];
//       else
//         sorted[k++] = nums[j++];

//     // Put possible remaining left part to the sorted array
//     while (i <= m)
//       sorted[k++] = nums[i++];

//     // Put possible remaining right part to the sorted array
//     while (j <= r)
//       sorted[k++] = nums[j++];

//     copy(begin(sorted), end(sorted), begin(nums) + l);
//   }
// };

// s1= Solution(); 

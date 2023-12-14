#include<stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int returnSize) {
    int* ans = (int*)malloc(2* sizeof(int));
//	int ans[2];
    
    int i;
    for(i = 0; i < numsSize; i++){
    	int j;
    	for(j = i+1; j < numsSize; j++){
    		if(nums[i] + nums[j] == target){
    			ans[0] = i;
    			ans[1] = j;
    			return ans;
			}
		}
		
	}
};

int main(){
	int test1[] = {2,7,11,15};
	int test2[] = {3, 2, 4};
	int test3[] = {9, 5, 1, 3, 2, 4};
	
	int* ans = twoSum(test3, 6, 6, 2);
	printf("Digits are: %d and %d", ans[0], ans[1]);
	return 0;
}

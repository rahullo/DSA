// function reverseStrings(str) {
//     str.substr()
//     let reverse;
//     for (let i = str.length; i >= 0; i--) {
//         reverse = reverse + str[i]

//     }
//     return reverse.slice(3, reverse.length);
// }


// console.log(reverseStrings('yretsam oyoy'))

// var removeDuplicates = function(nums) {
//     let counter = 0
//     let arrayLength = nums.length
//     for (let i = 0; i < arrayLength; i++) {
//         for (let j = i + 1; j < arrayLength; j++) {
//             if (nums[i] === nums[j]) {
//                 console.log(nums.length);
//                 nums.splice(i, i + 1)
//                 counter++;
//             }
//         }

//     }
//     for (let i = 0; i < counter; i++) {
//         nums.push('_')
//     }
//     return nums;
// };

// console.log(removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 4]));

// let array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

// array.splice(1, 4)
// console.log(array);

// console.log('_' === '_');


// console.log(reverseStrings('yretsam oyoy'))

// var removeDuplicates = function(nums) {
//     let counter = 0
//     let arrayLength = nums.length
//     for (let i = 0; i < arrayLength; i++) {
//         if (nums[i] === nums[i + 1]) {
//             console.log(nums.length);
//             nums.splice(i + 1, i + 2)
//             i = 0;
//             counter++;

//         }

//     }
//     for (let i = 0; i < counter; i++) {
//         nums.push('_')
//     }
//     return nums;
// };

// console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));


/////////////////////////////////////////////////////////////////////
///////////////////////////////////////////
//BUBBLE SORT
// let array = [4, 3, 5, 2];
// let bigArray = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

// let bubbleSort = function(array) {
//     for (let i = 0; i < array.length; i++) {
//         for (let j = 0; j < array.length; j++) {
//             if (array[j] > array[j + 1]) {
//                 let temp = array[j];
//                 array[j] = array[j + 1];
//                 array[j + 1] = temp;
//             }
//         }
//     }
//     return array;
// }

// console.log(bubbleSort(bigArray));



///////////////////////////
// SELECTION SORT

// let bigArray = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


// let array = [4, 3, 2, 5];

// function selectionSort(array) {
//     for (let i = 0; i < array.length - 1; i++) {
//         let minIndex = i;
//         let min = array[i];
//         for (let j = i + 1; j < array.length; j++) {
//             if (array[minIndex] > array[j]) {
//                 minIndex = j;
//             }
//         }
//         let temp = array[i]
//         array[i] = array[minIndex];
//         array[minIndex] = temp

//     }
//     return array;
// }
// console.log(selectionSort(bigArray));
/////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
// INSERTION SORT

// let bigArray = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

// let array = [4, 3, 2, 5];

// let insertionSort = (array => {
//     for (let i = 0; i < array.length; i++) {
//         let key = i + 1;
//         for (let j = key - 1; j >= 0; j--) {
//             if (array[j] > array[j + 1]) {
//                 let temp = array[j];
//                 array[j] = array[j + 1];
//                 array[j + 1] = temp;
//             }
//         }
//     }
//     return array
// })

// console.log(insertionSort(bigArray));


////////////////////////////////////////////////////////////
//////////////////////////////////////

//////  MERGE SORTING

let bigArray = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

let array = [4, 3, 2, 5];

// function mergesort(array) {
//     let length = array.length;
//     if (length < 2) {
//         return array;
//     }

//     let mid;

//     if (length % 2 == 0) {
//         mid = (length / 2) - 1
//     } else {
//         mid = Math.floor(length / 2) - 1
//     }

//     let firstHalf = array.slice(0, mid + 1);
//     let secondHalf = array.slice(mid + 1, length + 1)

//     return merge(mergesort(firstHalf), mergesort(secondHalf))
// }

// function merge(left, right) {
//     let answer = []
//     let leftIndex = 0;
//     let rightIndex = 0;
//     while (leftIndex < left.length && rightIndex < right.length) {
//         if (left[leftIndex] < right[rightIndex]) {
//             answer.push(left[leftIndex]);
//             leftIndex++
//         } else {
//             answer.push(right[rightIndex]);
//             rightIndex++
//         }
//     }
//     return answer.concat(left.slice(leftIndex).concat(right.slice(rightIndex)))
// }


// console.log(mergesort(bigArray));

// [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
// const numbers = [6, 2, 63, 1, 5];

// function quickSort(array, left, right) {
//     let pivot;
//     let partitionIndex;
//     if (left < right) {
//         pivot = right;
//         // console.log(array);
//         partitionIndex = partition(array, pivot, left, right);

//         //sort left and right
//         quickSort(array, left, partitionIndex - 1);
//         quickSort(array, partitionIndex + 1, right);
//     }
//     return array;
// }

// function partition(array, pivot, left, right) {
//     let pivotValue = array[pivot];
//     let partitionIndex = left;
//     console.log(array, 'pivot', pivot, 'left', left, 'right', right, 'pivotValue', pivotValue);
//     for (let i = left; i < right; i++) {
//         if (array[i] < pivotValue) {
//             swap(array, i, partitionIndex);
//             partitionIndex++;
//         }
//     }
//     swap(array, right, partitionIndex);
//     return partitionIndex;
// }

// function swap(array, firstIndex, secondIndex) {
//     var temp = array[firstIndex];
//     array[firstIndex] = array[secondIndex];
//     array[secondIndex] = temp;
// }

// //Select first and last index as 2nd and 3rd parameters
// console.log(numbers);
// quickSort(numbers, 0, numbers.length - 1);
// console.log(numbers);
// let x = true

// setTimeout(() => {
//     x = false
//     console.log('timeout');
// }, 3000)

// while (x) {
//     console.log(x)
//     console.log("hello")
//     x = false
// }

// let x = 1
// console.log(x !== x);

let arr = ['red', 'blue', 'black', 'white', 'gray', 'green', 'yellow', 'brown']

let i = 0
const looper = function() {
    setTimeout(() => {
        if (i < arr.length) {
            console.log(i, "=> ", arr[i]);
            i += 1
        }
        display()
    }, 500)
}


const display = () => {
    if (i == arr.length) {
        i = 0
    }
    looper()

}

display()
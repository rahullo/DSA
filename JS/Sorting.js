//////////////////////////////////
// ///Bubble sort

// let array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

// let bubbleSort = function(array) {
//     for (let i = 0; i < array.length; i++) {
//         for (let j = 0; j < array.length; j++) {
//             if (array[j] > array[j + 1]) {
//                 let temp = array[j];
//                 array[j] = array[j + 1];
//                 array[j + 1] = temp;
//             }
//             continue;
//         }
//     }
//     return array;
// }

// console.log(bubbleSort(array));
// console.log(array);

////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////
//Selection sorting

// let array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
// let array = [3, 1, 5]

// function selectionSort(array) {
//     let length = array.length;
//     for (let i = 0; i < length; i++) {
//         let current_min = array[i];
//         for (let j = 0; j < length - 1; j++) {
//             console.log(current_min);
//             if (array[j] > array[j + 1]) {
//                 current_min = array[j + 1];
//             }

//         }
//         array[i] = current_min;
//         current_min = temp;
//     }
//     return array;
// }


// function selectionSort(array) {
//     const length = array.length;
//     for (let i = 0; i < length; i++) {
//         let min = i;
//         let temp = array[i];
//         for (let j = i + 1; j < length; j++) {
//             if (array[j] < array[min]) {
//                 min = j;
//             }

//         }
//         array[i] = array[min];
//         array[min] = temp;
//     }
//     return array;
// // }

// // selectionSort(array)
// // console.log(array);

// //////////////////////////////////////////
// ///////////////////////////////////////////////////////
// //Insertion sort 

// let array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
// // let array = [3, 1, 5]

// let insertionSort = (array => {
//     let length = array.length
//     for (let i = 0; i < length; i++) {
//         let currentNum = array[i]
//         for (let j = i + 1; j < length; j++) {
//             if (currentNum > array[j]) {
//                 currentNum = array[j];
//                 let temp = array[j];
//                 array[j] = array[j - 1];
//                 array[j - 1] = temp;

//             }
//         }
//     }
//     return array
// })
// console.log(insertionSort(array));
// array.splice(1, 0, 8)
//     // array.unshift(1)
// console.log(array);

/////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////
//              [1, 2, 3, 4]

//         [1, 2]          [3, 4]

//       [1]      [2]     [3]    [4]


let array = [3, 1, 5, 2, 7]
let bigArray = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 10];

// function mergeSort(array) {
//     if (array.length === 1) {
//         return array;
//     }
//     debugger;
//     let length = array.length;
//     let mid;
//     if (length % 2 == 0) {
//         mid = (length / 2) - 1;
//     } else {
//         mid = Math.round(length / 2) - 2;
//     }

//     // let tempArray = array;
//     let firstSection = array;
//     let secondSection = firstSection.splice(mid + 1, length - (mid + 1))
//         // if (firstSection.length > 1 && secondSection.length > 1) {
//         //     if (firstSection[0] > secondSection[0]) {
//         //         let temp = firstSection[0];
//         //         firstSection[0] = secondSection[0];
//         //         secondSection[0] = temp;
//         //     }
//         // }

//     return merge(mergeSort(firstSection), mergeSort(secondSection))


//     //  this function return merged array of two given array;
//     // function merge(leftarray, rightarray) {
//     //     let array = [];
//     //     let length = leftarray.length + rightarray.length;
//     //     for (let i = 0; i < leftarray.length; i++) {
//     //         array.push(leftarray[i])
//     //     }
//     //     for (let j = 0; j < rightarray.length; j++) {
//     //         array.push(rightarray[j])
//     //     }

//     //     return array;

//     // }


//     function merge(left, right) {
//         const result = [];
//         let leftIndex = 0;
//         let rightIndex = 0;
//         while (leftIndex < left.length && rightIndex < right.length) {

//             if (left[leftIndex] < right[rightIndex]) {
//                 result.push(left[leftIndex]);
//                 leftIndex++;
//             } else {
//                 result.push(right[rightIndex]);
//                 rightIndex++
//             }
//         }
//         return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));

//     }

// }

// console.log(mergeSort(bigArray));

// let ar1 = [1, 2, 0]
// let ar2 = [3, 4, 5, 6]
// let a3 = ar2
// console.log(a3);

// let h1 = ar2.splice(0, 2)
// console.log(h1, ar2);



// console.log(merge(ar1, ar2));

// function merge(leftarray, rightarray) {
//     let array = [];
//     let length = leftarray.length + rightarray.length;
//     for (let i = 0; i < leftarray.length; i++) {
//         array.push(leftarray[i])
//     }
//     for (let j = 0; j < rightarray.length; j++) {
//         array.push(rightarray[j])
//     }

//     return array;

// }



// function merge(leftarray, rightarray) {
//     let array = [];
//     let length = leftarray.length + rightarray.length;
//     console.log(length);
//     for (let i = 0; i < length - 1; i++) {
//         if (leftarray[i] > rightarray[i]) {
//             array.push(rightarray[i])
//         } else array.push(leftarray[i])

//     }


//     return array;

// }

// console.log(merge([6], [3]));


// function merge(left, right) {
//     const result = [];
//     let leftIndex = 0;
//     let rightIndex = 0;
//     while (leftIndex < left.length && rightIndex < right.length) {
//         console.log(leftIndex, rightIndex);

//         if (left[leftIndex] < right[rightIndex]) {
//             result.push(left[leftIndex]);
//             leftIndex++;
//         } else {
//             result.push(right[rightIndex]);
//             rightIndex++
//         }
//     }
//     console.log(leftIndex, rightIndex);
//     console.log(result);
//     return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));

// }

// console.log(merge([3], [2, 4]))

// const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];
// const nums = [6, 2, 1, 5]

// function quickSort(array, left, right) {
//     let pivot = right;
//     let leftItem;
//     if (array[pivot] > array[left]) {
//         leftItem = array[left];
//     }

//     for (let i = 0; i < right; i++) {
//         let leftItem;
//         if (pivot < array[i]) {
//             leftItem = array[i];


//         }
//         console.log(array);
//     }
// }

// // console.log(nums.indexOf(5) - 1)


// //Select first and last index as 2nd and 3rd parameters
// quickSort(numbers, 0, numbers.length - 1);
// console.log(numbers);
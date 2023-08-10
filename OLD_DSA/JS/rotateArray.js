var rotate = function(nums, k) {
    if (k) nums.unshift(nums.pop());
    else nums.push(nums.shift());
    return nums;
};


let array = [1, 2, 3, 4, 5, 6, 7]
console.log(rotate(array, 2));

// array.unshift(19)
// array.pop()
// console.log(array);
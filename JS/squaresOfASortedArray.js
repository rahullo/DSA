var sortedSquares = function(nums) {
    let sqares = nums.map((el) => el * el)
    let sorted = mergeSort(sqares)
    return sorted;
};

console.log(sortedSquares([-4, -1, 0, 3, 10]));


function mergeSort(array) {
    if (array.length === 1) {
        return array;
    }
    debugger;
    let length = array.length;
    let mid;
    if (length % 2 == 0) {
        mid = (length / 2) - 1;
    } else {
        mid = Math.round(length / 2) - 2;
    }
    let firstSection = array;
    let secondSection = firstSection.splice(mid + 1, length - (mid + 1))

    return merge(mergeSort(firstSection), mergeSort(secondSection))

    function merge(left, right) {
        const result = [];
        let leftIndex = 0;
        let rightIndex = 0;
        while (leftIndex < left.length && rightIndex < right.length) {

            if (left[leftIndex] < right[rightIndex]) {
                result.push(left[leftIndex]);
                leftIndex++;
            } else {
                result.push(right[rightIndex]);
                rightIndex++
            }
        }
        return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));

    }

}
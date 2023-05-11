var plusOne = function(digits) {
    let aarr = []
    if (digits[digits.length - 1] % 10 === 0) {
        let str = digits.join('')
        let temp = Number(str[str.length - 1]) + 1
        for (let i = 0; i < str.length - 1; i++) {
            aarr.push(Number(str[i]))
        }
        aarr.push(temp)
        return aarr;
    } else if (digits[digits.length - 1] % 10 === 9) {
        let str = String(digits[digits.length - 1] + 1)
        for (let i = 0; i < str.length; i++) {
            aarr.push(Number(str[i]))
        }
        return aarr;
    } else {
        let temp = digits[digits.length - 1]
        digits[digits.length - 1] = temp + 1;
        return digits;
    }
};

// console.log(plusOne([9, 9]));

// let array = [4, 3, 2, 1]
// let str = array.join('')
// let aarr = []
// let temp = Number(str[str.length - 1]) + 1
// str[str.length - 1] = String(Number(temp) + 1);
// for (let i = 0; i < str.length; i++) {
//     aarr.push(Number(str[i]))
// }
// if (array[array.length - 1] % 10 === 0) {
//     let temp = digits[digits.length - 1]
//     digits[digits.length - 1] = temp + 1;
//     return digits;
// }
// console.log(aarr);


function plusOne2(digits) {
    let aarr = []
    let str = String(Number(digits.join('')) + 1)
    for (let i = 0; i < str.length; i++) {
        aarr.push(Number(str[i]))
    }
    return aarr;
}

console.log(plusOne2([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]));
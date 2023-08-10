let ar1 = [1, 2, 3, 4, 5]
let ar2 = [6, 7, 8, 9]
let array = [];
for (let i = ar1.length - 1; i >= 0; i--) {
    ar2.unshift(ar1[i]);
}

console.log(ar2);
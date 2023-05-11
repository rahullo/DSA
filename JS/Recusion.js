// let counter = 0

// function inception() {
//     debugger;
//     if (counter > 3) {
//         return 'done!'
//     }
//     counter++;
//     return inception()
// }

// what = inception()
// console.log(what);

// function findFactorialIterative(number) {
//     let counter = number;
//     let factorial = 1;
//     for (let i = number; i > 0; i--) {
//         factorial = factorial * counter;
//         counter--;

//     }
//     return factorial;
// }

// console.log(findFactorialIterative(5))


// function findFactorialRecursive(number) {
//     if (number <= 2) {
//         return number;
//     }
//     return number * findFactorialRecursive(number - 1);
// }

// console.log(findFactorialRecursive(5))

// function fibonacciRecursive(n) {
//     debugger;
//     if (n < 2) {
//         return n;
//     }

//     return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

// }

// console.log(fibonacciRecursive(40));
// console.log();


// function fibonacciIteration(n) {
//     if (n == 0) {
//         return 0;
//     }
//     let a;
//     let num = 0;
//     let b = 1;
//     for (let i = 0; i < n; i++) {
//         a = num;
//         num = num + b;
//         b = a;

//     }
//     return num;
// }

// console.log(fibonacciIteration(3));
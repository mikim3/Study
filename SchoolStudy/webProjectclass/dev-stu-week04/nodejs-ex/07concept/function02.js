// ./concept/function02.js
function sum(a, b) {
    console.log(a + b);
}
sum(4, 2);

function sum2(a, b) {
    return a + b;
}
console.log(sum2(2,3));

function sum3(a, b) {
    console.log('A');
    return a + b;
    console.log('B');
}
console.log(sum3(5,6));

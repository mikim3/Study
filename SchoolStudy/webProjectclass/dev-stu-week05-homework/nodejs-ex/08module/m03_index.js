// ./module/m03.index.js
const { odd, even } = require('./m01_var');
const checkNumber = require('./m02_func');
function checkStringOddOrEven(str) {
    if (str.length % 2) {
        return odd;
    };
    return even;
};
console.log(checkNumber(10));
console.log(checkStringOddOrEven('hello'));

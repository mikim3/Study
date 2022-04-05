// ./module/m02_func.js
const { odd, even } = require('./m01_var');
function checkOddEven(num) {
    if (num % 2) { 
        return odd;
    };
    return even;
};
module.exports = checkOddEven;

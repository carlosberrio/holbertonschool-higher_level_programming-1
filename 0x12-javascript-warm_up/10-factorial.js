#!/usr/bin/node
function factorial (n) {
  return (n === 1) ? n : factorial(n - 1) * n;
}
const n = parseInt(process.argv[2]) || 1;
console.log(factorial(n));

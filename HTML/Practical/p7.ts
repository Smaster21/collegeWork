let number = prompt("Enter a number:");
let factorial = 1;
let i = number;

while (i > 0) {
  factorial *= i;
  i--;
}

alert("Factorial of " + number + " is " + factorial);

let numbers = [5, 2, 9, 4, 8, 1];
let max1 = numbers[0];
let max2 = numbers[0];

for (let i = 1; i < numbers.length; i++) {
  if (numbers[i] > max1) {
    max2 = max1;
    max1 = numbers[i];
  } else if (numbers[i] > max2 && numbers[i] !== max1) {
    max2 = numbers[i];
  }
}

alert("The maximum two elements are: " + max1 + " and " + max2);

let operation = prompt("Enter an operation (+, *, /):");
let num1 = Number(prompt("Enter the first number:"));
let num2 = Number(prompt("Enter the second number:"));

switch (operation) {
  case "+":
    alert(num1 + num2);
    break;
  case "*":
    alert(num1 * num2);
    break;
  case "/":
    alert(num1 / num2);
    break;
  default:
    alert("Invalid operation.");
}

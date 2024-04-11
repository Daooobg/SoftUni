/////////////////////////////////////////////////////////////////////////////////////////
// // 1. Calculate Rectangle Area
/////////////////////////////////////////////////////////////////////////////////////////

// const rectangleArea = (a: number, b: number): number => a * b;

// console.log(rectangleArea(5, 7));

/////////////////////////////////////////////////////////////////////////////////////////
// // 2. Largest Number
/////////////////////////////////////////////////////////////////////////////////////////

// const largestNumber = (a: number, b: number, c: number): string => {
//     let maxNumber = a;
//     if (maxNumber < b) {
//         maxNumber = b;
//     }
//     if (maxNumber < c) {
//         maxNumber = c;
//     }
//     return `The largest number is ${maxNumber}.`;
// };

// console.log(largestNumber(5, -3, 16));
// console.log(largestNumber(-3, -5, -22.5));

/////////////////////////////////////////////////////////////////////////////////////////
// // 3. Sum of Numbers N…M
/////////////////////////////////////////////////////////////////////////////////////////

// const sumNumbers = (a: string, b: string): void => {
//     let sum: number = 0;

//     for (let i = Number(a); i <= Number(b); i++) {
//         sum += i;
//     }
//     console.log(sum);
// };

// sumNumbers('1', '5');
// sumNumbers('-8', '20');

/////////////////////////////////////////////////////////////////////////////////////////
// // 4. Day of Week
/////////////////////////////////////////////////////////////////////////////////////////

// const printDayNumber = (day: string): void => {
//     enum DayOfWeek {
//         Monday = 1,
//         Tuesday,
//         Wednesday,
//         Thursday,
//         Friday,
//         Saturday,
//         Sunday,
//     }
//     const dayEnum: DayOfWeek = DayOfWeek[day as keyof typeof DayOfWeek];
//     if (dayEnum) {
//         console.log(dayEnum);
//     } else {
//         console.log('error');
//     }
// };

// printDayNumber('Monday');
// printDayNumber('Friday');
// printDayNumber('Invalid');

/////////////////////////////////////////////////////////////////////////////////////////
// // 5. Math Operations
/////////////////////////////////////////////////////////////////////////////////////////

// const printResult = (a: number, b: number, c: string): void => {
//     const operators: Record<string, (a: number, b: number) => number> = {
//         '+': (a, b) => a + b,
//         '-': (a, b) => a - b,
//         '*': (a, b) => a * b,
//         '/': (a, b) => a / b,
//         '%': (a, b) => a % b,
//         '**': (a, b) => a ** b,
//     };

//     if (c in operators) {
//         console.log(operators[c](a, b));
//     }
// };

// printResult(5, 6, '+');
// printResult(3, 5.5, '*');

/////////////////////////////////////////////////////////////////////////////////////////
// // 6. Even Position Element
/////////////////////////////////////////////////////////////////////////////////////////

// const printEventPositions = (arr: string[]): void => {
//     let result: string[] = [];
//     for (let i = 0; i < arr.length; i += 2) {
//         result.push(arr[i]);
//     }
//     console.log(result.join(' '));
// };

// printEventPositions(['20', '30', '40', '50', '60']);
// printEventPositions(['5', '10']);

/////////////////////////////////////////////////////////////////////////////////////////
// // 7. Bigger Half
/////////////////////////////////////////////////////////////////////////////////////////

// const biggerHalf = (arr: number[]): number[] => {
//     const sortedArr = arr.sort((a, b) => a - b);

//     return sortedArr.splice(sortedArr.length / 2);
// };

// console.log(biggerHalf([4, 7, 2, 5]));
// console.log(biggerHalf([3, 19, 14, 7, 2, 19, 6]));

/////////////////////////////////////////////////////////////////////////////////////////
// // 8. Cats
/////////////////////////////////////////////////////////////////////////////////////////

// class Cat {
//     constructor(public name: string, public age: string) {}

//     meow(): void {
//         console.log(`${this.name}, age ${this.age} says Meow`);
//     }
// }

// const createCat = (catsData: string[]): void => {
//     catsData.forEach((catData) => {
//         const [name, age] = catData.split(' ');
//         const cat = new Cat(name, age);
//         cat.meow();
//     });
// };

// createCat(['Mellow 2', 'Tom 5']);
// createCat(['Candy 1', 'Poppy 3', 'Nyx 2']);

/////////////////////////////////////////////////////////////////////////////////////////
// // 9. Employees
/////////////////////////////////////////////////////////////////////////////////////////

// class Employee {
//     constructor(public name: string) {}
//     printText(): void {
//         console.log(`Name: ${this.name} -- Personal Number: ${this.name.length}`);
//     }
// }

// const employees = (names: string[]): void => {
//     names.forEach((name) => {
//         const currentEmployee = new Employee(name);
//         currentEmployee.printText();
//     });
// };

// employees(['Silas Butler', 'Adnaan Buckley', 'Juan Peterson', 'Brendan Villarreal']);
// employees(['Samuel Jackson', 'Will Smith', 'Bruce Willis', 'Tom Holland']);

/////////////////////////////////////////////////////////////////////////////////////////
// // 10. Aggregate Elements
/////////////////////////////////////////////////////////////////////////////////////////

// const printSums = (arr: number[]): void => {
//     let sum1: number = 0;
//     let sum2: number = 0;
//     let concat: string = '';

//     arr.forEach((x) => {
//         sum1 += x;
//         sum2 += 1 / x;
//         concat += String(x);
//     });

//     console.log(sum1);
//     console.log(sum2);
//     console.log(concat);
// };

// printSums([1, 2, 3]);
// printSums([2, 4, 8, 16]);

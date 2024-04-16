class Person {
    constructor(data) {
        const [name, age] = data.split(' ');
        this.name = name;
        this.age = Number(age);
    }
    printText() {
        console.log(`${this.name} is ${this.age} years old.`);
    }
}
const peter = new Person('Peter 12');
const sofia = new Person('Sofia 33');
peter.printText();
sofia.printText();

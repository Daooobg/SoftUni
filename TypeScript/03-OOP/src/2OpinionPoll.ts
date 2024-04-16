class Person {
    name: string;
    age: number;

    constructor(data: string) {
        const [name, age] = data.split(' ');
        this.name = name;
        this.age = Number(age);
    }

    printText(): void {
        console.log(`${this.name} is ${this.age} years old.`);
    }
}

const peter = new Person('Peter 12');
const sofia = new Person('Sofia 33');

peter.printText();
sofia.printText();

class Animal {
    eat() {
        console.log('eating…');
    }
}
class Dog extends Animal {
    bark() {
        console.log('barking…');
    }
}
class Cat extends Animal {
    meow() {
        console.log('meowing…');
    }
}
const dog = new Dog();
dog.eat();
dog.bark();

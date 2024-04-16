class Car {
    get carInfo() {
        return `The car is: ${this.brand} ${this.model} - ${this.horsePower} HP.`;
    }
    set carInfo(data) {
        const [brand, model, horsePower] = data.split(' ');
        this.brand = brand;
        this.model = model;
        this.horsePower = Number(horsePower);
    }
}
const carOne = new Car();
carOne.carInfo = 'Chevrolet Impala 390';
console.log(carOne.carInfo);
console.log('-----------------------------');
const carTwo = new Car();
carTwo.carInfo = 'Skoda Karoq 150';
console.log(carTwo.carInfo);

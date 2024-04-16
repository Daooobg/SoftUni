class Car {
    brand: string;
    model: string;
    horsePower: number;

    get carInfo(): string {
        return `The car is: ${this.brand} ${this.model} - ${this.horsePower} HP.`;
    }

    set carInfo(data: string) {
        const [brand, model, horsePower] = data.split(' ');
        this.brand = brand;
        this.model = model;
        this.horsePower = Number(horsePower);
    }
}

const carOne = new Car();
carOne.carInfo = 'Chevrolet Impala 390';
console.log(carOne.carInfo);
console.log('-----------------------------')
const carTwo = new Car();
carTwo.carInfo = 'Skoda Karoq 150';
console.log(carTwo.carInfo);
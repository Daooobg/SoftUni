interface Dealership<T> {
    dealershipName: T;
    soldCars: number;
}

interface Actions<V> {
    dealerID: V;
    model: V;
}

class CarDealer implements Dealership<string>, Actions<string> {
    dealershipName: string;
    soldCars: number;
    dealerID: string;
    model: string;
    modelsSold: {};

    constructor(dealershipName: string) {
        this.dealershipName = dealershipName;
        this.modelsSold = {};
    }
    sellCar(id: string, model: string) {
        this.modelsSold[id] = model;
    }
    showDetails(): string {
        let modelsSold = '';
        for (let model in this.modelsSold) {
            modelsSold += `${model} sold ${this.modelsSold[model]}\n`;
        }
        return `${this.dealershipName}: \n${modelsSold}`;
    }
}

let dealership = new CarDealer('SilverStar');

dealership.sellCar('BG01', 'C Class');
dealership.sellCar('BG02', 'S Class');
dealership.sellCar('BG03', 'ML Class');
dealership.sellCar('BG04', 'CLK Class');
console.log(dealership.showDetails());

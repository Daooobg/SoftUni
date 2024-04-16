class CarDealer {
    dealershipName;
    soldCars;
    dealerID;
    model;
    modelsSold;
    constructor(dealershipName) {
        this.dealershipName = dealershipName;
        this.modelsSold = {};
    }
    sellCar(id, model) {
        this.modelsSold[id] = model;
    }
    showDetails() {
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
//# sourceMappingURL=3.carDealership.js.map
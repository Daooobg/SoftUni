class Box {
    data;
    constructor(data) {
        this.data = data;
    }
    toString() {
        return `${this.data} is of type ${typeof this.data}`;
    }
}
let box1 = new Box(['test']);
let box2 = new Box(20);
let box3 = new Box('Hello');
console.log(box1.toString());
console.log(box2.toString());
console.log(box3.toString());
//# sourceMappingURL=1.genericBoxOfString.js.map
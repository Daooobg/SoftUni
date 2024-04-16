class CompareElements {
    data;
    constructor(data) {
        this.data = data;
    }
    compare(element) {
        let counter = 0;
        this.data.forEach((el) => {
            if (el === element) {
                counter++;
            }
        });
        return counter;
    }
}
let c = new CompareElements(['a', 'b', 'ab', 'abc', 'cba', 'b']);
console.log(c.compare('b'));
let d = new CompareElements([1, 2, 3, 4, 5, 1, 1]);
console.log(d.compare(1));
//# sourceMappingURL=2.genericCompareElements.js.map
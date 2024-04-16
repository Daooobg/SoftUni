class BankAccount {
    constructor() {
        this._id = 0;
        this._balance = 0;
        this._interestRate = 0.02;
        BankAccount._counter++;
        this._id = BankAccount._counter;
    }
    setInterestRate(interestRate) {
        this._interestRate = interestRate;
    }
    getInterest() {
        return this._interestRate;
    }
    deposit(amount) {
        this._balance += amount;
    }
    getId() {
        return this._id;
    }
}
BankAccount._counter = 0;
class TestClient {
    constructor() {
        this._accounts = {};
    }
    action(command) {
        const args = command.split(' ');
        const action = args[0];
        if (action == 'Create') {
            this.createAccount();
        }
        else if (action == 'Deposit') {
            const id = Number(args[1]);
            const balance = Number(args[2]);
            this.deposit(id, balance);
        }
        else if (action == 'SetInterest') {
            const interestRate = Number(args[1]);
            this.setInterest(interestRate);
        }
        else if (action == 'GetInterest') {
            const id = Number(args[1]);
            const years = Number(args[2]);
            this.getInterest(id, years);
        }
        else if (action === 'End') {
            console.log('End');
        }
    }
    createAccount() {
        const account = new BankAccount();
        this._accounts[account['_id']] = account;
        console.log(`Account ID${account['_id']} created`);
    }
    deposit(id, amount) {
        if (this._accounts.hasOwnProperty(id)) {
            this._accounts[id]['_balance'] += amount;
        }
        else {
            console.log('Account does not exist');
        }
    }
    setInterest(interestRate) {
        for (let acc in this._accounts) {
            this._accounts[acc]['_interestRate'] = interestRate;
        }
    }
    getInterest(id, years) {
        if (this._accounts.hasOwnProperty(id)) {
            const interest = this._accounts[id]['_balance'] * this._accounts[id]['_interestRate'] * years;
            console.log(interest.toFixed(2));
        }
        else {
            console.log('Account does not exist');
        }
    }
}
const client = new TestClient();
client.action('Create');
client.action('Create');
client.action('Deposit 1 20');
client.action('Deposit 3 20');
client.action('Deposit 2 10');
client.action('SetInterest 1.5');
client.action('GetInterest 1 1');
client.action('GetInterest 2 1');
client.action('GetInterest 3 1');
client.action('End');

class BankAccount {
    private _id: number = 0;
    private static _counter = 0;
    private _balance: number = 0;
    private _interestRate: number = 0.02;

    constructor() {
        BankAccount._counter++;
        this._id = BankAccount._counter;
    }

    setInterestRate(interestRate: number): void {
        this._interestRate = interestRate;
    }

    getInterest(): number {
        return this._interestRate;
    }

    deposit(amount: number): void {
        this._balance += amount;
    }

    getId(): number {
        return this._id;
    }
}

class TestClient {
    private _accounts: { [id: number]: BankAccount };

    constructor() {
        this._accounts = {};
    }

    action(command: string) {
        const args = command.split(' ');
        const action = args[0];

        if (action == 'Create') {
            this.createAccount();
        } else if (action == 'Deposit') {
            const id = Number(args[1]);
            const balance = Number(args[2]);
            this.deposit(id, balance);
        } else if (action == 'SetInterest') {
            const interestRate = Number(args[1]);
            this.setInterest(interestRate);
        } else if (action == 'GetInterest') {
            const id = Number(args[1]);
            const years = Number(args[2]);
            this.getInterest(id, years);
        } else if (action === 'End') {
            console.log('End');
        }
    }

    private createAccount(): void {
        const account = new BankAccount();
        this._accounts[account['_id']] = account;
        console.log(`Account ID${account['_id']} created`);
    }

    private deposit(id: number, amount: number): void {
        if (this._accounts.hasOwnProperty(id)) {
            this._accounts[id]['_balance'] += amount;
        } else {
            console.log('Account does not exist');
        }
    }

    private setInterest(interestRate: number) {
        for (let acc in this._accounts) {
            this._accounts[acc]['_interestRate'] = interestRate;
        }
    }

    private getInterest(id: number, years: number) {
        if (this._accounts.hasOwnProperty(id)) {
            const interest = this._accounts[id]['_balance'] * this._accounts[id]['_interestRate'] * years;
            console.log(interest.toFixed(2));
        } else {
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

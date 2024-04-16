abstract class CreateAccount<T, V> {
    bankName: T;
    bankID: V;

    constructor(bankName: T, bankId: V) {
        this.bankID = bankId;
        this.bankName = bankName;
    }
}

class PersonalAccount extends CreateAccount<string, number> {
    readonly ownerName: string;
    money: number = 0;
    recentTransactions: {} = {};
    totalMoneySpentOnExpenses: number = 0;
    constructor(bankName: string, bankID: number, ownerName: string) {
        super(bankName, bankID);
        this.ownerName = ownerName;
    }

    deposit(amount: number): void {
        this.money += amount;
    }

    expense(amount, expenseType) {
        if (this.money < amount) {
            console.log(`You cant make ${expenseType} transaction`);
        } else {
            this.money -= amount;
            this.totalMoneySpentOnExpenses += amount;
            if (this.recentTransactions.hasOwnProperty(expenseType)) {
                this.recentTransactions[expenseType] += amount;
            } else {
                this.recentTransactions[expenseType] = amount;
            }
        }
    }

    showDetails(): string {
        return `Bank name: ${this.bankName}\nBank ID: ${this.bankID}\nOwner name: ${this.ownerName}\nMoney: ${this.money}\nMoney spent: ${this.totalMoneySpentOnExpenses}`;
    }
}

let account = new PersonalAccount('DSK', 101240, 'Ivan Ivanov');

account.deposit(1000);
account.deposit(1000);
account.expense(700, 'Buy new phone');
account.expense(400, 'Book a vacation');
account.expense(400, 'Book a vacation');
account.expense(100, 'Buy food');
console.log(account.showDetails());

let account2 = new PersonalAccount('Fibank', 100000, 'Petar Petrol');

account2.deposit(10000);
account2.deposit(7000);
account2.expense(1200, 'Buy a new car');
account2.expense(200, 'Go to a fancy restaurant');
account2.expense(100, 'Go to a bar');
account2.expense(30, 'Go to the movies');
console.log(account2.showDetails());

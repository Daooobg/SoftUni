class Employee {
    constructor(data) {
        const [name, salary, position, department, email, age] = data.split(' ');
        this.name = name;
        this.salary = Number(salary);
        this.position = position;
        if (email) {
            this.email = email;
        }
        if (age) {
            this.age = Number(age);
        }
    }
}
class Departments {
    constructor(data) {
        this.departments = {};
        data.forEach((x) => {
            const splitData = x.split(' ');
            const department = splitData[3];
            const employee = new Employee(x);
            if (this.departments.hasOwnProperty(department)) {
                this.departments[department].push(employee);
            }
            else {
                this.departments[department] = [employee];
            }
        });
    }
}
const departments = new Departments([
    'Peter 120.00 Dev Development peter@abv.bg 28',
    'Tina 333.33 Manager Marketing 33',
    'Sam 840.20 ProjectLeader Development sam@sam.com',
    'George 0.20 Freeloader Nowhere 18',
]);
console.log(departments['departments']);

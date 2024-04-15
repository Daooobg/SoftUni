/////////////////////////////////////////////////////////////////////////////////////////
// // 1. Calorie Object
/////////////////////////////////////////////////////////////////////////////////////////
// type CalorieObject = {
//     [key: string]: number;
// };

// const calorieObj = (arr: string[]): void => {
//     const result: CalorieObject = {};
//     for (let a: number = 0; a < arr.length; a += 2) {
//         result[arr[a]] = Number(arr[a + 1]);
//     }
//     console.log(result);
// };

// calorieObj(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']);
// calorieObj(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42']);

/////////////////////////////////////////////////////////////////////////////////////////
// // 2.	Person Info
/////////////////////////////////////////////////////////////////////////////////////////

// type PersonInfo = {
//     firstName: string;
//     lastName: string;
//     age: number;
// };

// const personInfo = (firstName: string, lastName: string, age: string): PersonInfo => {
//     return { firstName: firstName, lastName: lastName, age: Number(age) };
// };

// console.log(personInfo('Peter', 'Pan', '20'));
// console.log(personInfo('George', 'Smith', '18'));

/////////////////////////////////////////////////////////////////////////////////////////
// // 3.	Inventory
/////////////////////////////////////////////////////////////////////////////////////////

// type Hero = {
//     hero: string;
//     level: number;
//     items?: string;
// };

// const printHeroes = (heroes: Hero[]): void => {
//     heroes.forEach((hero: Hero) => {
//         console.log(`Hero: ${hero.hero} \nlevel => ${hero.level}`);
//         if (hero.items) {
//             console.log(`items => ${hero.items}`);
//         }
//     });
// };

// const heroes = (arr: string[]): void => {
//     const allHeroes: Hero[] = [];
//     arr.forEach((hero) => {
//         const [name, level, items] = hero.split(' / ');
//         allHeroes.push(
//             items ? { hero: name, level: Number(level), items: items } : { hero: name, level: Number(level) }
//         );
//     });
//     const sortedHeroesByLevel = allHeroes.sort((a, b) => a.level - b.level);
//     printHeroes(sortedHeroesByLevel);
// };

// heroes([
//     'Isacc / 25 / Apple, GravityGun',
//     'Derek / 12 / BarrelVest, DestructionSword',
//     'Hes / 1 / Desolator, Sentinel, Antara',
// ]);
// heroes(['Batman / 2 / Banana, Gun', 'Superman / 18 / Sword', 'Poppy / 28 / Sentinel, Antara']);

/////////////////////////////////////////////////////////////////////////////////////////
// // 4.	Towns
/////////////////////////////////////////////////////////////////////////////////////////

// type Towns = {
//     town: string;
//     latitude: number;
//     longitude: number;
// };

// const printTowns = (arr: string[]): void => {
//     const towns: Towns[] = [];
//     arr.forEach((data: string) => {
//         const [town, lat, log] = data.split(' | ');
//         const currTown: Towns = {
//             town: town,
//             latitude: Number(Number(lat).toFixed(2)),
//             longitude: Number(Number(log).toFixed(2)),
//         };
//         console.log(currTown);
//     });
// };

// printTowns(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625']);
// printTowns(['Plovdiv | 136.45 | 812.575']);

/////////////////////////////////////////////////////////////////////////////////////////
// // 5.	Town Population
/////////////////////////////////////////////////////////////////////////////////////////

// type Populations = {
//     [town: string]: number;
// };

// const population = (data: string[]): void => {
//     const populations: Populations = {};
//     data.forEach((x: string) => {
//         let [town, population] = x.split(' <-> ');

//         if (populations.hasOwnProperty(town)) {
//             populations[town] += Number(population);
//         } else {
//             populations[town] = Number(population);
//         }
//     });
//     for (let town in populations) {
//         console.log(`${town} : ${populations[town]}`);
//     }
// };

// population([
//     'Sofia <-> 1200000',
//     'Montana <-> 20000',
//     'New York <-> 10000000',
//     'Washington <-> 2345000',
//     'Las Vegas <-> 1000000',
// ]);

// population([
//     'Istanbul <-> 100000',
//     'Honk Kong <-> 2100004',
//     'Jerusalem <-> 2352344',
//     'Mexico City <-> 23401925',
//     'Istanbul <-> 1000',
// ]);

/////////////////////////////////////////////////////////////////////////////////////////
// // 6.	Lowest Prices in Cities
/////////////////////////////////////////////////////////////////////////////////////////
// type ProductData = {
//     town: string;
//     price: number;
// };

// type Product = {
//     [product: string]: ProductData;
// };

// const printProducts = (data: string[]): void => {
//     const products: Product = {};
//     data.forEach((x: string) => {
//         const [town, name, price] = x.split(' | ');
//         if (products.hasOwnProperty(name)) {
//             if (products[name].price > Number(price)) {
//                 products[name].town = town;
//                 products[name].price = Number(price);
//             }
//         } else {
//             const productData: ProductData = { town: town, price: Number(price) };
//             products[name] = productData;
//         }
//     });

//     for (let p in products) {
//         console.log(`${p} => ${products[p].price} (${products[p].town})`);
//     }
// };

// printProducts([
//     'Sample Town | Sample Product | 1000',
//     'Sample Town | Orange | 2',
//     'Sample Town | Peach | 1',
//     'Sofia | Orange | 3',
//     'Sofia | Peach | 2',
//     'New York | Sample Product | 1000.1',
//     'New York | Burger | 10',
// ]);

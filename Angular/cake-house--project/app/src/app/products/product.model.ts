export class Product {
  constructor(
    public productId: string,
    public productName: string,
    public description: string,
    public images: string[],
    public price: number,
    public types: string[],
    public name: string
  ) {}
}

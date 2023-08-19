export class Product {
  constructor(
    public description: string,
    public images: string[],
    public price: number,
    public types: string[],
    public name: string,
    public sizes: string[],
    public createAt?: string,
    public ownerId?: string,
    public priceDiscount?: number,
    public product?: string,
    public slug?: string,
    public _id?: string,
    public comments?: {
      comment: String;
      rating: Number;
      ownerId: { _id: String; name: String };
    }[],
    public averageRating?: number 
  ) {}
}

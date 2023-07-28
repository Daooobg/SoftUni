export class User {
  constructor(
    public username: string,
    public email: string,
    public userId: string,
    public role: string,
    private AccessToken: string
  ) {}

  get token() {
    return this.AccessToken;
  }
}

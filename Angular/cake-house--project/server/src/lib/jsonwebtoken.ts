import util from 'util';
import jwtCallback, { VerifyOptions, Secret, SignOptions } from 'jsonwebtoken';

type SignPayload = {};
type SecretOrPrivateKey =
  | Secret
  | Buffer
  | { key: string; passphrase?: string };
type SecretOrPublicKey = Secret | Buffer;

const signAsync = util
  .promisify<string | object | Buffer, string>(jwtCallback.sign)
  .bind(jwtCallback) as (
  payload: SignPayload,
  secretOrPrivateKey: SecretOrPrivateKey,
  options?: SignOptions
) => Promise<void>;

const verifyAsync = util.promisify(jwtCallback.verify).bind(jwtCallback) as (
  token: string,
  secretOrPublicKey: SecretOrPublicKey,
  options?: VerifyOptions
) => Promise<object>;

const jwt = {
  sign: signAsync,
  verify: verifyAsync,
};

export default jwt;

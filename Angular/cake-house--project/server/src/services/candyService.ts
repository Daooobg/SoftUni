import * as factoryServices from './factoryService';
import Candy from '../models/candyModel';

export const createOne = factoryServices.createOne(Candy);

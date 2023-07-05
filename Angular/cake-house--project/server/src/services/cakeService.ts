import * as factoryServices from './factoryService';
import Cake from '../models/cakeModel';

export const createOne = factoryServices.createOne(Cake);
export const getAll = factoryServices.getAll(Cake);
export const updateOne = factoryServices.updateOne(Cake);
export const deleteOne = factoryServices.deleteOne(Cake);

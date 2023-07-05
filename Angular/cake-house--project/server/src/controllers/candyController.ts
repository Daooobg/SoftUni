import * as candyService from '../services/candyService';
import * as factoryController from './factoryController';

export const createOne = factoryController.createOne(candyService);
export const getAll = factoryController.getAll(candyService);

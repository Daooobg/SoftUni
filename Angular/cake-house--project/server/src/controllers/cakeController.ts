import * as cakeService from '../services/cakeService';
import * as factoryController from './factoryController';

export const createOne = factoryController.createOne(cakeService);
export const getAll = factoryController.getAll(cakeService);
export const updateOne = factoryController.updateOne(cakeService);
export const deleteOne = factoryController.deleteOne(cakeService);
export const createComment = factoryController.createComment(cakeService);

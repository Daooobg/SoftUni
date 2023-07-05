import { RequestHandler, Router } from 'express';

import * as candyController from '../controllers/candyController';
import { restrictTo } from '../middlewares/authMiddleware';

const restrict = restrictTo('admin', 'owner');

const router = Router();

router
  .route('/candies')
  .get(candyController.getAll)
  .post(candyController.createOne);

router
  .route('/candies/:slug')
  .put(
    restrictTo('admin', 'owner') as RequestHandler,
    candyController.updateOne
  );

export default router;

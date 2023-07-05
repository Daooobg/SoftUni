import { RequestHandler, Router } from 'express';

import * as candyController from '../controllers/candyController';
import * as cakeController from '../controllers/cakeController';
import { restrictTo } from '../middlewares/authMiddleware';

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
  )
  .delete(
    restrictTo('admin', 'owner') as RequestHandler,
    candyController.deleteOne
  );

router
  .route('/cakes')
  .get(cakeController.getAll)
  .post(cakeController.createOne);

router
  .route('/cakes/:slug')
  .put(restrictTo('admin', 'owner') as RequestHandler, cakeController.updateOne)
  .delete(
    restrictTo('admin', 'owner') as RequestHandler,
    cakeController.deleteOne
  );

export default router;

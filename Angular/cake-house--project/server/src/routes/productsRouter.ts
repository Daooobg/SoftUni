import { Router } from 'express';

import * as candyController from '../controllers/candyController';

const router = Router();

router
  .route('/candies')
  .get(candyController.getAll)
  .post(candyController.createOne);

export default router;

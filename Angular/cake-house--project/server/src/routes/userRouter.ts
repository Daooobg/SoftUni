import { Router } from 'express';
import * as authService from '../controllers/authController';

const router = Router();

router.route('/register').post(authService.register);

export default router;

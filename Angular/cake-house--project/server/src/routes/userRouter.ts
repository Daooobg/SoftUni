import { Router } from 'express';
import * as authService from '../controllers/authController';

const router = Router();

router.route('/register').post(authService.register);
router.route('/login').post(authService.login);

export default router;

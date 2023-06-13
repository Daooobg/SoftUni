DELETE FROM waiters AS w
WHERE (SELECT COUNT(*) FROM orders WHERE waiter_id = w.id) = 0;
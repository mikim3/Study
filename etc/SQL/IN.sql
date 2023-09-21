SELECT *
FROM orders
WHERE status IN ('Open', 'Pending', 'Approved');

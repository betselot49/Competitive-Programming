SELECT name AS Customers
FROM Customers
LEFT JOIN Orders ON orders.customerId = customers.id
WHERE Orders.id IS NULL;
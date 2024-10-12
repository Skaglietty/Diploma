SELECT c.login,
       COUNT (o.*) AS count_orders
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;
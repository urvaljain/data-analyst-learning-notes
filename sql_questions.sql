-- 1. Total sales amount
SELECT SUM(amount) AS total_sales FROM sales_dataset;

-- 2. Sales by city
SELECT city, SUM(amount) AS city_sales
FROM sales_dataset
GROUP BY city;

-- 3. Sales by product
SELECT product, SUM(amount) AS product_sales
FROM sales_dataset
GROUP BY product;

-- 4. Average order amount
SELECT AVG(amount) AS average_amount FROM sales_dataset;

-- 5. Highest order amount
SELECT MAX(amount) AS highest_order FROM sales_dataset;

-- 6. Group by product with average
SELECT product, AVG(amount) AS avg_product_amount
FROM sales_dataset
GROUP BY product;

-- 7. Filter sales greater than 800
SELECT * FROM sales_dataset
WHERE amount > 800;

-- 8. Count total orders
SELECT COUNT(order_id) AS total_orders FROM sales_dataset;

-- 9. Order sales by amount (descending)
SELECT * FROM sales_dataset
ORDER BY amount DESC;

-- 10. Show top 5 highest sales
SELECT * FROM sales_dataset
ORDER BY amount DESC
LIMIT 5;

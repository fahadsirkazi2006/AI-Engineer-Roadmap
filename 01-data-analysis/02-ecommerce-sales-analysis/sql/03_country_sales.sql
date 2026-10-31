SELECT
    Country,
    ROUND(SUM(Revenue),2) AS Total_revenue,
    COUNT(DISTINCT(InvoiceNo)) AS Unique_invoices
FROM product_sales
WHERE Country IS NOT NULL
GROUP BY Country
ORDER BY Total_revenue DESC
LIMIT 10;
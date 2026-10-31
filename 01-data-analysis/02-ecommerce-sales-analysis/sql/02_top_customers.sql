SELECT
    CustomerID,
     ROUND(SUM(Revenue),2) AS total_revenue,
     COUNT(DISTINCT(InvoiceNo)) AS unique_invoices
FROM product_sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY total_revenue DESC
LIMIT 10;
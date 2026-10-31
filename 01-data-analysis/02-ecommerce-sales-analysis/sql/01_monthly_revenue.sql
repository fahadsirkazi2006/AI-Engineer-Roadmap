SELECT
    strftime('%Y-%m',InvoiceDate) AS month,
    ROUND(SUM(Revenue),2) AS total_revenue,
    COUNT(DISTINCT(InvoiceNo)) AS unique_invoices,
    SUM(Quantity) AS total_quantity
FROM product_sales
GROUP BY strftime('%Y-%m',InvoiceDate)
ORDER BY month;



    
SELECT 
    t.*, 
    subtotal.amount_subtotal
FROM 
    your_table t
JOIN 
    (SELECT 
         country_risk, 
         client_name, 
         SUM(amount) AS amount_subtotal
     FROM 
         your_table
     GROUP BY 
         country_risk, client_name) subtotal
ON 
    t.country_risk = subtotal.country_risk 
    AND t.client_name = subtotal.client_name;
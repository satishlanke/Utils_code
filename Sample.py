hhSELECT 
    t.*, 
    grouped.total_client_earnings, 
    grouped.total_net_earnings
FROM 
    your_table t
JOIN 
    (SELECT 
        fund, 
        SUM(client_earnings) AS total_client_earnings,
        SUM(net_earnings) AS total_net_earnings
     FROM 
        your_table
     GROUP BY 
        fund) grouped
ON t.fund = grouped.fund;

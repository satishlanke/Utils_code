SELECT 
    t.*,
    aggregated."Client Earnings",
    aggregated."Net Earnings"
FROM 
    perfora_df_1 t
JOIN 
    (SELECT 
        "Client Name",
        SUM("Client Earnings") AS "Client Earnings",
        SUM("Net Earnings") AS "Net Earnings"
     FROM 
        perfora_df_1
     GROUP BY 
        "Client Name"
    ) aggregated
ON 
    t."Client Name" = aggregated."Client Name";
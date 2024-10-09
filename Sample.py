SELECT 
    t.identifiers,
    t.asset_correct,
    t.moody_rating,
    SUM(t.value) AS total_value
FROM 
    Sample_read t
JOIN 
    (SELECT 
         identifiers, 
         asset_correct, 
         moody_rating, 
         SUM(value) AS total_value
     FROM 
         Sample_read
     GROUP BY 
         identifiers, asset_correct, moody_rating
    ) AS subtotal 
ON 
    t.identifiers = subtotal.identifiers 
    AND t.asset_correct = subtotal.asset_correct
GROUP BY 
    t.identifiers, 
    t.asset_correct, 
    t.moody_rating;
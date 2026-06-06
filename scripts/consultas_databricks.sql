-- 1. Ver metadatos
DESCRIBE TABLE macroeconomic_gold_data;

SHOW CREATE TABLE macroeconomic_gold_data;

-- 2. Descripción de datos
SELECT 
    COUNT(*) as Total_Records, 
    AVG(Gold_Price) as Avg_Gold, 
    MAX(Inflation_Rate) as Max_Inflation 
FROM macroeconomic_gold_data;

-- 3. SELECT y GROUP BY comparativo
SELECT 
    Date, 
    AVG(Gold_Price) as Avg_Gold_Price
FROM macroeconomic_gold_data 
WHERE Gold_Price > 1200
GROUP BY Date;

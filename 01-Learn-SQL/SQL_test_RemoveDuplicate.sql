WITH duplicates AS (
    SELECT 
        id,
        ROW_NUMBER() OVER (
            PARTITION BY first_name, last_name, department
            ORDER BY id
        ) AS row_num
    FROM employees
)
DELETE FROM employees
WHERE id IN (
    SELECT id FROM duplicates WHERE row_num > 1
);


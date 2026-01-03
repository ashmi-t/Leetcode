# Write your MySQL query statement below
SELECT     
    
    Department ,
    Salary ,
    Employee
FROM 
(SELECT 

    E1.name AS Employee,
    E1.salary AS Salary,
    D1.name AS Department
    , DENSE_RANK() 
        OVER(PARTITION BY E1.departmentId ORDER BY E1.salary DESC ) 
        AS rnk
FROM 
    Employee E1
    INNER JOIN
        Department D1
    ON 
        D1.id = E1.departmentId

) AS T1
WHERE T1.rnk <=3
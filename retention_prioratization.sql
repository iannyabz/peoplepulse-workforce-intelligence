USE peoplePulsedb;
#4. Retention prioritization

#which department should HR investigate first
SELECT d.department, COUNT(*) as total_employees,
SUM(CASE WHEN a.attrition = 'Yes' THEN 1 ELSE 0 END) AS attrion_count,
ROUND(100.0 * SUM(CASE WHEN a.attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_rate_pct
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN attrition_outcomes a ON e.employee_id = a.employee_id
GROUP BY d.department
HAVING COUNT(*) >= 20
ORDER BY attrition_rate_pct DESC;


# which job roles have the most retention risk
SELECT jr.job_role, COUNT(*) as total_employees,
SUM(CASE WHEN a.attrition = 'Yes' THEN 1 ELSE 0 END) AS attrion_count,
ROUND(100.0 * SUM(CASE WHEN a.attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_rate_pct
FROM employees e
JOIN job_roles jr ON e.department_id = jr.job_id
JOIN attrition_outcomes a ON e.employee_id = a.employee_id
GROUP BY jr.job_role
HAVING COUNT(*) >= 20
ORDER BY attrition_rate_pct DESC;

#where will HR have the greatest impact
SELECT d.department,
       j.job_role,
       COUNT(*) AS total_employees,
       SUM(CASE WHEN a.attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
       ROUND(100.0 * SUM(CASE WHEN a.attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 1) AS attrition_rate_pct
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN job_roles j ON e.job_id = j.job_id
JOIN attrition_outcomes a ON e.employee_id = a.employee_id
GROUP BY d.department, j.job_role
ORDER BY attrition_count DESC 
LIMIT 10;
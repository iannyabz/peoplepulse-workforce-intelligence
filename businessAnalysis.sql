#Database Analysis
USE peoplePulsedb;

#1. workforceOverview
SELECT * from employees;

#getting size of each department
SELECT d.department, COUNT(*) as department_size from employees e
JOIN departments d ON d.department_id = e.department_id
GROUP BY department 
ORDER BY department_size DESC;

#getting size of job roles
SELECT j.job_role, COUNT(*) as job_role_size FROM employees e
JOIN job_roles j ON j.job_id = e.job_id
GROUP BY job_role
ORDER BY job_role_size DESC;

#workforce demographic
SELECT gender,COUNT(gender) as gender_size FROM employees
GROUP BY gender
ORDER BY gender_size DESC;

#experience of workforce
SELECT ROUND(AVG(years_at_company),2) as avg_exp_at_company FROM employees;

#education level;
SELECT educationCategory, COUNT(educationCategory) as total from employees
GROUP BY educationCategory
ORDER BY total DESC;

#Avegrage Income
SELECT ROUND(AVG(monthly_income),2) as avg_income FROM employees;

select * from attrition_outcomes;

#2. Attrition Analysis

#which department losses the mose employees
SELECT d.department, a.attrition, COUNT(*) AS attrition_total FROM attrition_outcomes a
JOIN employees e ON e.employee_id = a.employee_id
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department, a.attrition;


#understanding relation between overtime and attrition
SELECT e.overtime, a.attrition, COUNT(*) AS attrition_total FROM attrition_outcomes a
JOIN employees e ON e.employee_id = a.employee_id
GROUP BY e.overtime, a.attrition
ORDER BY e.overtime DESC, a.attrition;


#satisfaction rating related to attrition?
SELECT es.job_satisfaction, a.attrition, COUNT(*) as attrition_total FROM attrition_outcomes a
JOIN employees e ON e.employee_id = a.employee_id
JOIN employee_surveys es ON e.employee_id = es.employee_id
GROUP BY es.job_satisfaction, a.attrition
ORDER BY attrition_total DESC;


#effect of tenure on attrition
SELECT e.tenure_groups, a.attrition, COUNT(*) as attrition_total from attrition_outcomes a
JOIN employees e ON e.employee_id = a.employee_id
GROUP BY e.tenure_groups, a.attrition
ORDER BY attrition_total DESC; 



#3. Compensation Analysis
#avg pay per department

SELECT d.department, ROUND(AVG(e.monthly_income)) as avg_income FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id
ORDER BY avg_income DESC;


#relation between attrition and pay
SELECT a.attrition, ROUND(AVG(e.monthly_income),2) AS avg_income,
COUNT(*) as employee_count
FROM employees e
JOIN attrition_outcomes a ON e.employee_id = a.employee_id
GROUP BY a.attrition;

#relation between salary hike and perfomance
SELECT performance_rating, ROUND(AVG(percent_salary_hike),2) as avg_salary_hike 
FROM performance_records pr
GROUP BY pr.performance_rating;


#relation between education and salary
SELECT e.educationCategory, ROUND(AVG(monthly_income),2) as avg_income FROM employees e
GROUP BY e.educationCategory
ORDER BY avg_income DESC;


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
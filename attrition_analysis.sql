USE peoplePulsedb;
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

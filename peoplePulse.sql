#PeoplePulse_db

CREATE DATABASE IF NOT EXISTS peoplePulseDB;
USE peoplePulseDB;

#departments
CREATE TABLE IF NOT EXISTS departments (department_id INT AUTO_INCREMENT PRIMARY KEY,
department VARCHAR(100)
);

#job roles
CREATE TABLE IF NOT EXISTS job_roles(job_id INT AUTO_INCREMENT PRIMARY KEY,
job_role VARCHAR(100)
);


#Employee
CREATE TABLE IF NOT EXISTS employees(employee_id INT AUTO_INCREMENT PRIMARY KEY,
employee_number INT NOT NULL UNIQUE,
age INT,
gender VARCHAR(50),
educationCategory VARCHAR(100),
education_field VARCHAR(100),
department_id INT,
job_id INT,
job_level INT,
monthly_income INT,
monthly_rate INT,
stock_option_level INT,
overtime BOOLEAN,
distance_from_home INT,
marital_status VARCHAR(50),
years_at_company INT,
tenure_groups VARCHAR(50),
years_with_curr_manager INT,
num_companies_worked INT,
business_travel VARCHAR(50),

FOREIGN KEY(department_id)
REFERENCES departments(department_id),
FOREIGN KEY(job_id)
REFERENCES job_roles(job_id),

created_at TIMESTAMP
DEFAULT CURRENT_TIMESTAMP
);


#employee survey
CREATE TABLE IF NOT EXISTS employee_surveys (survey_id INT AUTO_INCREMENT PRIMARY KEY,
employee_id INT NOT NULL,
relationship_satisfaction TINYINT,
environment_satisfaction TINYINT,
work_life_balance TINYINT,
job_involvement INT,
job_satisfaction TINYINT,

FOREIGN KEY(employee_id)
REFERENCES employees(employee_id),

created_at TIMESTAMP
DEFAULT CURRENT_TIMESTAMP
);

#performance records
CREATE TABLE IF NOT EXISTS performance_records (record_id INT AUTO_INCREMENT PRIMARY KEY,
employee_id INT NOT NULL,
performance_rating TINYINT,
percent_salary_hike INT,
training_times_last_year INT,
promotion_recency VARCHAR(100),
years_in_current_role INT,
years_since_last_promotion INT,
long_current_role_tenure BOOLEAN,


FOREIGN KEY (employee_id)
REFERENCES employees(employee_id),

created_at TIMESTAMP
DEFAULT CURRENT_TIMESTAMP
);

#attrition outcomes
CREATE TABLE IF NOT EXISTS attrition_outcomes (attrition_id INT AUTO_INCREMENT PRIMARY KEY,
employee_id INT NOT NULL,
attrition BOOLEAN,

FOREIGN KEY (employee_id)
REFERENCES employees(employee_id),

created_at TIMESTAMP
DEFAULT CURRENT_TIMESTAMP
);


#ANALYTICAL TABLES


CREATE TABLE IF NOT EXISTS department_risk_summary (department_risk_id INT AUTO_INCREMENT PRIMARY KEY,
department VARCHAR(50),
total_employees INT,
avg_risk_score FLOAT,
high_risk_count INT,
medium_risk_count INT,
low_risk_count INT,
pct_high_risk FLOAT,

created_at TIMESTAMP
DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS model_predictions (model_id INT AUTO_INCREMENT PRIMARY KEY,
employee_number INT,
actual_attrition INT,
predicted_attrition INT,
risk_score FLOAT,
risk_category VARCHAR(20),

created_at TIMESTAMP
DEFAULT CURRENT_TIMESTAMP
);



CREATE INDEX idx_employee_department
ON employees(department_id);

CREATE INDEX idx_employee_job_role
ON employees(job_id);

CREATE INDEX idx_employee_employees
ON employees(employee_id);

SELECT * FROM departments;
SELECT * FROM job_roles;
SELECT * FROM employees;
SELECT * FROM employee_surveys;
SELECT * FROM performance_records;
SELECT * FROM attrition_outcomes;


USE peoplePulsedb;
SELECT * from employees
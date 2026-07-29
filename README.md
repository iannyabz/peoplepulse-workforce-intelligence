# PeoplePulse — Workforce Planning & Retention Intelligence Platform

**An end-to-end People Analytics decision-support platform that transforms workforce data into actionable insights for retention, workforce planning, and responsible HR decision-making.**


## Overview

PeoplePulse is an end-to-end People Analytics and Workforce Intelligence platform designed to help HR teams move beyond descriptive reporting and make more informed, evidence-based workforce decisions.

The project combines: Python, MySQL, Scikit-learn, SHAP and Power BI


Rather than treating attrition prediction as the end goal, PeoplePulse focuses on a broader question:
How can workforce data be transformed into useful intelligence that helps HR teams identify areas requiring attention, understand workforce patterns, and prioritize retention investigations?

The platform is designed as a decision-support system, not an automated employee decision-making tool.

# Business Problem

Organizations collect large amounts of employee data across areas such as:
* Demographics
* Compensation
* Job roles
* Departments
* Job satisfaction
* Work-life balance
* Overtime
* Performance
* Career progression
* Business travel
* Employee tenure


However, having workforce data does not automatically translate into actionable workforce intelligence.
HR teams may need to answer questions such as:
* Which departments have the highest observed attrition?
* Which workforce segments require further investigation?
* What factors are associated with employee turnover?
* Are certain employee groups experiencing different outcomes?
* Can statistical analysis and machine learning identify meaningful patterns?
* How reliable are predictive models across different groups?
* Which areas should HR prioritize for further investigation?
* How can analytical findings be communicated effectively to HR leadership?

PeoplePulse addresses these questions by combining data engineering, SQL, statistics, machine learning, explainability, responsible AI, and business intelligence into a single analytical workflow.

# Objectives

The project aims to:
1. Build a reproducible HR data pipeline using Python.
2. Store structured workforce data in a relational MySQL database.
3. Perform SQL based workforce and retention analysis.
4. Conduct exploratory and statistical analysis of workforce patterns.
5. Develop and evaluate employee attrition prediction models.
6. Explain model predictions using SHAP.
7. Evaluate potential differences in model performance across demographic groups.
8. Develop a workforce retention prioritization framework.
9. Build interactive Power BI dashboards for different HR audiences.
10. Translate analytical findings into practical business recommendations.
11. Demonstrate responsible and transparent use of predictive HR analytics.


# Dataset

This project uses the IBM HR Analytics Employee Attrition & Performance dataset.

**source:**
[IBM HR Analytics Employee Attrition & Performance — Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

The dataset contains fictional employee records with variables covering areas including:
* Employee demographics
* Department
* Job role
* Monthly income
* Job satisfaction
* Environment satisfaction
* Work-life balance
* Overtime
* Business travel
* Performance
* Career progression
* Tenure
* Attrition

# Key Business Questions

PeoplePulse is designed around the following analytical questions.

## Workforce Health
* What does the current workforce composition look like?
* How is headcount distributed across departments and job roles?
* What are the major workforce demographic patterns?
* How does employee tenure vary across the organization?

## Retention Intelligence
* What is the observed attrition rate?
* Which departments have the highest attrition?
* Which job roles have the highest attrition?
* How does attrition vary by tenure?
* How is attrition associated with overtime?
* How do satisfaction and work-life balance relate to attrition?
* Are compensation patterns associated with observed attrition?

## Predictive Analytics
* Can employee attrition be predicted using available workforce characteristics?
* Which machine learning model performs best?
* Which variables contribute most to model predictions?
* How should model performance be evaluated when classes are imbalanced?

## Explainability
* Why does the model make certain predictions?
* Which factors are most influential globally?
* How can technical model outputs be translated into HR-friendly insights?

## Responsible AI
* Does model performance differ across demographic groups?
* Are there differences in false-positive or false-negative rates?
* What limitations should be considered before using predictive HR analytics?

## Decision Support
* Which workforce segments should HR investigate first?
* How can risk, population size, and potential business impact be combined into a retention priority framework?
* How can analytical findings be communicated to HR leadership?



# MySQL Database Design

The project uses a relational database to separate workforce entities and analytical outputs.

### Core Tables
employees
departments
job_roles
employee_surveys
performance_records
attrition_outcomes

### Analytical Tables
employee_risk_scores
department_risk_summary
model_predictions
fairness_metrics


## 1. Exploratory Data Analysis

The project investigates workforce patterns across:
* Departments
* Job roles
* Tenure
* Compensation
* Overtime
* Satisfaction
* Work-life balance
* Business travel
* Demographic groups
Visualizations are used to identify patterns and generate hypotheses for further statistical investigation.


## 2. Statistical Analysis
Statistical methods are used to investigate relationships between workforce variables and attrition.
Potential methods include:
* Chi-square tests
* Two-group comparison tests
* Confidence intervals
* Logistic regression

The analysis distinguishes between:
Observed association and Causal conclusions
The project does not assume that a statistically significant relationship automatically implies causation.

## 3. Machine Learning

Several classification models are evaluated:
Logistic Regression, Decision Tree, Random Forest, Gradient Boosting

Models are evaluated using metrics including:
* Precision
* Recall
* F1-score
* ROC-AUC
* PR-AUC
* Confusion Matrix

Because attrition prediction can involve class imbalance, model performance is not evaluated using accuracy alone.
The final model is selected based on the analytical objective and appropriate evaluation metrics rather than simply choosing the model with the highest accuracy.

# Explainable AI

PeoplePulse uses SHAP-based explainability to understand model behavior.
The analysis examines:
* Global feature importance
* Feature contributions
* Individual prediction explanations
* Direction of feature influence
The goal is to translate model outputs into understandable insights for HR stakeholders.
Importantly, model explanations are treated as evidence of predictive relationships, not proof of causation.


The project does not recommend using the model to automatically:

* Reject job applicants
* Fire employees
* Deny promotions
* Make compensation decisions
* Make other automated employment decisions
Instead, the system is intended to support aggregate workforce analysis and HR investigation, with appropriate human oversight.


This project is intended for educational and portfolio purposes. Please refer to the original dataset source for applicable dataset licensing and usage terms.

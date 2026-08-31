#PeoplePulse Project

import pandas as pd
import numpy as np


data = pd.read_csv(r"C:\Users\ianny\OneDrive\Documents\Personal Coding Projects\HR project\ibm_hr_analytics\WA_Fn-UseC_-HR-Employee-Attrition.csv")

#data inspection
print(data.shape,'\n')
print(data.columns,'\n')
print(data.dtypes,'\n')
print(data.isna().sum()) #no nulls 
print(data.drop_duplicates())
print(data.nunique())

#renaming columns
dataCopy = data.copy()
dataCopy.rename(columns = {"Age":'age','Attrition':'attrition',
                'BusinessTravel':'business_travel','Education':'education',
                'DailyRate':'daily_rate','Department':'department',
                'DistanceFromHome':'distance_from_home','EducationField':'education_field',
                'EmployeeCount':'employee_count','EmployeeNumber':'employee_number',
                'EnvironmentSatisfaction':'environment_satisfaction','Gender':'gender',
                'HourlyRate':'hourly_rate', 'JobInvolvement':'job_involvement',
                'JobLevel':'job_level', 'JobRole':'job_role',
                'JobSatisfaction':'job_satisfaction', 'MaritalStatus':'marital_status',
                'MonthlyIncome':'monthly_income', 'MonthlyRate':'monthly_rate',
                'NumCompaniesWorked':'num_companies_worked', 'Over18':'over_18',
                'OverTime':'overtime','PercentSalaryHike':'percent_salary_hike',
                'PerformanceRating':'performance_rating','RelationshipSatisfaction':'relationship_satisfaction',
                'StandardHours':'standard_hours', 'StockOptionLevel':'stock_option_level',
                'TotalWorkingYears':'total_working_years', 'TrainingTimesLastYear':'training_times_last_year',
                'WorkLifeBalance':'work_life_balance','YearsAtCompany':'years_at_company',
                'YearsInCurrentRole':'years_in_current_role', 'YearsSinceLastPromotion':'years_since_last_promotion',
                'YearsWithCurrManager':'years_with_curr_manager'},inplace = True)

print(dataCopy.columns)

#COLUMN INSPECTION
#1. age INT
print(dataCopy['age'].value_counts())


#2. Attrition boolean
dataCopy['attrition'] = dataCopy['attrition'].map({'No':False, 'Yes':True})
print(dataCopy['attrition'].value_counts(dropna=False))

#3. business_travel varchar(100)
dataCopy['business_travel'] = dataCopy['business_travel'].map({'Travel_Rarely':'Travel Rarely',
                                                               'Travel_Frequently':'Travel Frequently',
                                                               'Non-Travel':'Non-Travel'})

#4. over_18 boolean
dataCopy['over_18'] = dataCopy['over_18'].map({'Y':True})


#5. overtime boolean
dataCopy['overtime'] = dataCopy['overtime'].map({'No': False,
                                                 'Yes':True})



#OMITTING NON-ESSENTIAL COLUMNS
dataCopy.drop(columns = ['employee_count','standard_hours','over_18'], inplace = True)
print(dataCopy.columns)


#IDENTIFYING OUTLIERS
numerical_columns = dataCopy.select_dtypes(include=['int64',
                                                    'float64']).columns


def check_outliers(df, columns):

    outlier_summary = []

    for column in columns:

        # Calculate Q1 and Q3
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        # Calculate IQR
        iqr = q3 - q1

        # Calculate bounds
        lowerB = q1 - 1.5 * iqr
        upperB = q3 + 1.5 * iqr

        # Identify outliers
        outliers = df[(df[column] < lowerB) |(df[column] > upperB)]

        # Store results
        outlier_summary.append({
            'column': column,
            'Q1': q1,
            'Q3': q3,
            'IQR': iqr,
            'Lower Bound': lowerB,
            'Upper Bound': upperB,
            'Outlier Count': len(outliers),
            'Outlier %': round((len(outliers) / len(df)) * 100,2)})

    return pd.DataFrame(outlier_summary)


outlier_summary = check_outliers(dataCopy,
                                 numerical_columns)

print(outlier_summary)

#VISUALIZING OUTLIERS
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style(style = 'whitegrid')

#1. monthly Income
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['monthly_income'].dropna())
plt.title('Monthly Income Distribution')
plt.ylabel('Monthly Income')
plt.show()


#2. num compaanies worked
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['num_companies_worked'].dropna())
plt.title('Number of Companies Worked Distribution')
plt.ylabel('Number of Companies Worked')
plt.show()

#3. performance_rating
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['performance_rating'].dropna())
plt.title('Performance Rating Distribution')
plt.ylabel('Performance Rating')
plt.show()

#4. stock_option_level
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['stock_option_level'].dropna())
plt.title('Stock Option Level Distribution')
plt.ylabel('Stock Option Level')
plt.show()

#5. total_working_years
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['total_working_years'].dropna())
plt.title('Total Working Years Distribution')
plt.ylabel('Total Working Years')
plt.show()

#6. training_times_last_year
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['training_times_last_year'].dropna())
plt.title('Training Times Last Year Distribution')
plt.ylabel('Training Times Last Year')
plt.show()

#7. years_at_company
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['years_at_company'].dropna())
plt.title('Years at Company Distribution')
plt.ylabel('Years at Company')
plt.show()

#8. years_in_current_role
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['years_in_current_role'].dropna())
plt.title('Years in Current Role Distribution')
plt.ylabel('Years in Current Role')
plt.show()

#9. years_since_last_promotion
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['years_since_last_promotion'].dropna())
plt.title('Years Since Last Promotion Distribution')
plt.ylabel('Years Since Last Promotion')
plt.show()

#10. years_with_curr_manager
plt.figure(figsize = (10,6))
sns.boxplot(dataCopy['years_with_curr_manager'].dropna())
plt.title('Years With Current Manager Distribution')
plt.ylabel('Years With Current Manager')
plt.show()
plt.close()

#income outliers deep dive
#we suspect high earners will be managers
Q1 = dataCopy['monthly_income'].quantile(0.25)
Q3 = dataCopy['monthly_income'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

income_outliers = dataCopy[
    (dataCopy['monthly_income'] < lower_bound) |
    (dataCopy['monthly_income'] > upper_bound)]



#CLEANED DATA
dataCleaned = dataCopy.copy()



#CATEGORY CONSISTENCY
#job_involvement_cat varchar(100)
dataCleaned['job_involvement_cat'] = dataCleaned['job_involvement'].map({1:'low',
                                                   2:'medium',
                                                   3:'high',
                                                   4:'very high'})


# environment_satisfaction_cat varchar(100)
dataCleaned['environment_satisfaction_cat'] = dataCleaned['environment_satisfaction'].map({1:'low',
                                                   2:'medium',
                                                   3:'high',
                                                   4:'very high'})


#educationCategory
dataCleaned['educationCategory'] = dataCleaned['education'].map({1:'Below College',
                                                   2:'College',
                                                   3:'Bachelors',
                                                   4:'Masters',
                                                   5:'Doctrate'})



# age_groups varchar(50)
bins = [18,35,60,np.inf]
labels = ['18-34','35-59','60+']
dataCleaned['age_group'] = pd.cut(dataCleaned['age'],bins = bins,
                               labels = labels, right = False)

#salary bands
minimum = dataCleaned['monthly_income'].min()
maximum = dataCleaned['monthly_income'].max()
avg = dataCleaned['monthly_income'].mean()
standard_dv = dataCleaned['monthly_income'].std()

bins = [999, 5000, 10000, 15000, 20000]
labels = ['1000-4999','5000-9999','10000-14999','15000-19999']
dataCleaned['salary_band'] = pd.cut(dataCleaned['monthly_income'],bins = bins,
                               labels = labels, right = False)

#tenure groups
minimumTenure = dataCleaned['total_working_years'].min()
maximumTenure = dataCleaned['total_working_years'].max()
avgTenure = dataCleaned['total_working_years'].mean()
standard_dvTenure = dataCleaned['total_working_years'].std()
#std is 7.78 years, so bands of 5 years i find appropriate

bins = [-1, 5, 10, 15, 20, 25, 30, 35, 40]
labels = ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-40']
dataCleaned['tenure_groups'] = pd.cut(dataCleaned['total_working_years'],bins = bins,
                               labels = labels, right = False)


#CAREER PROGRESSION INDICATORS
#not to be used to claim an employee should have been promoted or deserves promotion

#1. promotion recency
dataCleaned['promotion_recency'] = pd.cut(
    dataCleaned['years_since_last_promotion'],
    bins = [-1,1,3,np.inf],
    labels = ['Recently Promoted','Moderately Recent','Long Time Since Promotion'])
print(dataCopy[['promotion_recency','employee_number']])


#long stays in current position
dataCleaned['long_current_role_tenure'] = (
    dataCleaned['years_in_current_role'] >3)
#True = long tenure
#False = short tenure
print(dataCopy[['long_current_role_tenure','employee_number']])


#PROCESSED DATA
dataProcessed = dataCleaned.copy()

#VERYFYING processed data
print(dataProcessed.shape)
print(dataProcessed.dtypes)




#Populating SQL Tables
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:password@localhost/peoplePulseDB')

#1. departments
departments_df = dataProcessed['department'].copy()
departments_df.drop_duplicates(inplace = True)


departments_df.to_sql('departments', engine,
                  if_exists = 'append',
                  index = False)

dept_lookup = pd.read_sql('SELECT department, department_id FROM departments', engine)
dept_lookup = dept_lookup.sort_values('department_id').drop_duplicates(subset='department', keep='first')
dept_map = dept_lookup.set_index('department')['department_id'].to_dict()


#2. job roles
job_role_df = dataProcessed['job_role'].copy()
job_role_df.drop_duplicates(inplace = True)


job_role_df.to_sql('job_roles', engine,
                  if_exists = 'append',
                  index = False)

job_lookup = pd.read_sql('SELECT job_role,job_id FROM job_roles', engine)
job_lookup = job_lookup.sort_values('job_id').drop_duplicates(subset='job_role', keep='first')

job_map = job_lookup.set_index('job_role')['job_id'].to_dict()


#3. employees
employee_split = dataProcessed[['employee_number','age','gender',
                  'educationCategory','education_field',
                  'job_level','monthly_income','monthly_rate',
                  'stock_option_level','overtime',
                  'distance_from_home','marital_status',
                  'years_at_company','tenure_groups',
                  'years_with_curr_manager','num_companies_worked',
                  'business_travel']].copy()

employee_split['department_id'] = dataProcessed['department'].map(dept_map)
employee_split['job_id'] = dataProcessed['job_role'].map(job_map)

employee_split.to_sql('employees', engine,
                  if_exists = 'append',
                  index = False)


#4. employee_survey
survey_split = dataProcessed[['relationship_satisfaction',
                              'environment_satisfaction',
                              'work_life_balance','job_involvement',
                              'job_satisfaction']].copy()



emp_lookup = pd.read_sql('SELECT employee_id,employee_number FROM employees', engine)
emp_map = emp_lookup.set_index('employee_number')['employee_id'].to_dict()

survey_split['employee_id'] = dataProcessed['employee_number'].map(emp_map)

survey_split.to_sql('employee_surveys', engine,
                  if_exists = 'append',
                  index = False)



#5. perfomance records
performance_split = dataProcessed[['performance_rating','percent_salary_hike',
                                  'training_times_last_year','promotion_recency',
                                  'years_in_current_role','years_since_last_promotion',
                                  'long_current_role_tenure']].copy()

performance_split['employee_id'] = dataProcessed['employee_number'].map(emp_map)

performance_split.to_sql('performance_records', engine,
                  if_exists = 'append',
                  index = False)


#6. attrition outcomes
attrition_split = dataProcessed[['attrition']].copy()

attrition_split['employee_id'] = dataProcessed['employee_number'].map(emp_map)

attrition_split.to_sql('attrition_outcomes', engine,
                  if_exists = 'append',
                  index = False)





#EDA

#separating categorical and numerical columns
numColumns = []
catColumns = []

for column in dataProcessed:
    if dataProcessed[column].dtypes == 'int64':
        numColumns.append(column)
    else:
        catColumns.append(column)
       
#investigating distributions of numerical columns

basic insight
for col in numColumns:
    print(dataProcessed[col].describe())
    



#VISUALIZATIONS    
for column in numColumns:
    sns.kdeplot(data = dataProcessed[column], color = 'black', fill = 'black')
    plt.show()
    sns.histplot(dataProcessed[column])
    plt.show()



#categorical columns
#Visualizations

for column in catColumns:
    plt.figure(figsize = (10,6))
    sns.countplot(data = dataProcessed[column])
    plt.show()
    plt.figure(figsize = (10,6))
    sns.barplot(data = dataProcessed[column])
    plt.show()



targetVar = dataProcessed['attrition'].copy()


attMap = targetVar.map({True:'Left',False:'Stayed'})


#visualizing target variable

sns.countplot(data = attMap, color = 'black', fill = 'black')
plt.show()

sns.histplot(data = attMap, stat = 'percent', shrink = 0.8)
plt.show()


#Relationship Analysis

#1. correlation matrix
numerical_df = dataProcessed[numColumns]
numerical_df['attrition'] = dataProcessed['attrition']
corr_mat = numerical_df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(data = corr_mat,annot = True,
            cmap = 'coolwarm',
            fmt='.2f', linewidth = 0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


#salary analysis
for col in catColumns:
    sns.violinplot(data = dataProcessed, x = dataProcessed[col],
                   y = dataProcessed['monthly_income'])
    plt.tight_layout()
    plt.show()

    sns.barplot(data = dataProcessed, x = dataProcessed[col],
                y = dataProcessed['monthly_income'])
    plt.tight_layout()
    plt.show()

    sns.boxplot(data = dataProcessed, x = dataProcessed[col],
                y = dataProcessed['monthly_income'])
    plt.tight_layout()
    plt.show()
    plt.close()
#Attrition analysis

#1. Attrition vs Department

# Create a cross-tabulation of department and attrition
department_attrition = pd.crosstab(dataProcessed['department'],
                                   dataProcessed['attrition'],
                                   normalize='index') * 100

# Rename columns
department_attrition = department_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
department_attrition.plot(kind='bar',
                          stacked=True,
                          figsize=(10, 6))

plt.title('Attrition Rate by Department')
plt.xlabel('Department')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()
    
#2. Attrition vs job role
job_role_attrition = pd.crosstab(dataProcessed['job_role'],
                                 dataProcessed['attrition'],
                                 normalize = 'index')*100

# Renaming column
job_role_attrition = job_role_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
job_role_attrition.plot(kind='bar',
                        stacked=True,
                        figsize=(10, 6))

plt.title('Attrition Rate by Job Role')
plt.xlabel('Job Role')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=90)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()


#3. Attrition vs Job satisfaction
job_satisfaction_attrition = pd.crosstab(dataProcessed['job_satisfaction'],
                                 dataProcessed['attrition'],
                                 normalize = 'index')*100

# Renaming column
job_satisfaction_attrition = job_satisfaction_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
job_satisfaction_attrition.plot(kind='bar',
                                stacked=True,
                                figsize=(10, 6))

plt.title('Attrition Rate by Job Satisfaction')
plt.xlabel('Job Satisfaction')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()


#4. Attrition vs Environment Satisfaction
environment_satisfaction_attrition = pd.crosstab(
    dataProcessed['environment_satisfaction'],
    dataProcessed['attrition'],
    normalize = 'index')*100

# Renaming column
environment_satisfaction_attrition = job_satisfaction_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
environment_satisfaction_attrition.plot(kind='bar',
                                stacked=True,
                                figsize=(10, 6))

plt.title('Attrition Rate by Environment Satisfaction')
plt.xlabel('Environment Satisfaction')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()


#5. Attrition vs Work-Life Balance
work_life_attrition = pd.crosstab(
    dataProcessed['work_life_balance'],
    dataProcessed['attrition'],
    normalize = 'index')*100

# Renaming column
work_life_attrition = work_life_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
work_life_attrition.plot(kind='bar',
                         stacked=True,
                         figsize=(10, 6))

plt.title('Attrition Rate by Work-life Balance')
plt.xlabel('Work-Life Balance')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()



#6. Attrition vs Promotion Recency
promotion_attrition = pd.crosstab(
    dataProcessed['promotion_recency'],
    dataProcessed['attrition'],
    normalize = 'index')*100

# Renaming column
promotion_attrition = promotion_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
promotion_attrition.plot(kind='bar',
                         stacked=True,
                         figsize=(10, 6))

plt.title('Attrition Rate by Promotion Recency')
plt.xlabel('Promotion Recency')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()


#7. Attrition vs year in current role
curr_role_attrition = pd.crosstab(
    dataProcessed['years_in_current_role'],
    dataProcessed['attrition'],
    normalize = 'index')*100

# Renaming column
curr_role_attrition = curr_role_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
curr_role_attrition.plot(kind='bar',
                         stacked=True,
                         figsize=(10, 6))

plt.title('Attrition Rate by Years in Current Role')
plt.xlabel('Years in Current Role')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()


#8. Attrition vs Salary
monthly_income_attrition = pd.crosstab(
    dataProcessed['salary_band'],
    dataProcessed['attrition'],
    normalize = 'index')*100

# Renaming column
monthly_income_attrition = monthly_income_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
monthly_income_attrition.plot(kind='bar',
                         stacked=True,
                         figsize=(10, 6))

plt.title('Attrition Rate by Monthly Income')
plt.xlabel('Monthly Income')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()


#9. Attrition vs Overtime
overtime_attrition = pd.crosstab(
    dataProcessed['overtime'],
    dataProcessed['attrition'],
    normalize = 'index')*100

# Renaming column
overtime_attrition = overtime_attrition.rename(
    columns={False: 'Stayed', True: 'Left'})

# Plot
overtime_attrition.plot(kind='bar',

                         stacked=True,
                         figsize=(10, 6))

plt.title('Attrition Rate by Overtime')
plt.xlabel('Overtime')
plt.ylabel('Percentage of Employees')
plt.xticks(rotation=0)
plt.legend(title='Attrition')
plt.tight_layout()
plt.show()
plt.close()


#STATISTIC ANALYSIS
from scipy import stats

#1. Categorical
stat_analysis_df = dataProcessed[['overtime','job_role','department',
                                  'promotion_recency',
                                  'tenure_groups']].copy()

results = []
for col in stat_analysis_df:
    cont_table = pd.crosstab(dataProcessed[col],dataProcessed['attrition'])
    chi2_stat,p_val,dof,expected = stats.chi2_contingency(cont_table)
    cramer_v = stats.contingency.association(cont_table, method = 'cramer')
    results.append({'variable':col, 'chi2_stat':chi2_stat,
                   'p-value':p_val, 'dof':dof, 'effect_size': cramer_v})

    chi_results_df = pd.DataFrame(results).sort_values('p-value')


for col in chi_results_df['variable']:
    
    p_value = chi_results_df.loc[chi_results_df['variable'] == col,
                                 'p-value'].values[0]
    
    if p_value < 0.05:
        print(f'{col}:')
        print('Reject Null Hypothesis: Variables are strongly associated\n')
    else:
        print(f'{col}:')
        print('Failed to reject Null Hypothesis: Variables are independent\n')





        
#2. Numerical
from scipy.stats import mannwhitneyu
import pingouin as pg

stat_analysis_df = dataProcessed[['job_satisfaction', 'monthly_income',
                                   'work_life_balance', 'years_in_current_role',
                                   'environment_satisfaction', 'age']].copy()

result = []
for col in stat_analysis_df.columns:
    left = dataProcessed.loc[dataProcessed['attrition'] == True, col].dropna()
    stayed = dataProcessed.loc[dataProcessed['attrition'] == False, col].dropna()
    
    
    statistic, p_value = mannwhitneyu(left, stayed, alternative='two-sided')
    avgLeft = left.mean()
    avgRight = stayed.mean()

    medianLeft = left.median()
    medianRight = stayed.median()

    n1, n2 = len(left), len(stayed)
    rank_biserial = 1 - (2 * statistic) / (n1 * n2)
    
    
    result.append({'variable': col, 'Mann-Whitney Stat': statistic, 'p-value': p_value,
                   f'mean_stay':avgRight, 'mean_left':avgLeft,
                   'median_stay':medianRight,
                   'median_left':medianLeft,
                   'abs_RBC_value':rank_biserial})

mannWhitney_results = pd.DataFrame(result).sort_values('p-value')

for col in mannWhitney_results['variable']:
    p_value = mannWhitney_results.loc[mannWhitney_results['variable'] == col, 'p-value'].values[0]
    
    if p_value < 0.05:
        print(f'{col}:')
        print('Reject Null Hypothesis: Variables are strongly associated\n')
    else:
        print(f'{col}:')
        print('Failed to reject Null Hypothesis: Variables are independent\n')


# Multiple test corrections
from statsmodels.stats.multitest import multipletests

#1. Numerical
reject,p_adjusted,alpha_corrected,alpac_sidak = multipletests(
    pvals = mannWhitney_results['p-value'],
    alpha = 0.05,
    method = 'fdr_bh')

multi = pd.DataFrame({'rejected':reject,'Adjusted p-value':p_adjusted})


#2. Categorical
reject, p_adjusted,alpha_corrected, aphac_sidak = multipletests(
    pvals = chi_results_df['p-value'],
    alpha = 0.05,
    method = 'fdr_bh')

multi2 = pd.DataFrame({'rejected':reject,
                       'Adjusted p-value':p_adjusted})

print(multi2)
print(multi)


#Adding 95% confidence interval to Numerical data
import scipy.stats as st

result = []
for col in stat_analysis_df.columns:
    left = dataProcessed.loc[dataProcessed['attrition'] == True, col].dropna()
    stayed = dataProcessed.loc[dataProcessed['attrition'] == False, col].dropna()
    
    
    avgLeft = left.mean()
    avgStay = stayed.mean()

    semLeft = st.sem(left)
    semStay = st.sem(stayed)

    ci_lower_left,ci_upper_left = st.t.interval(0.95,len(left)-1,
                                                loc = avgLeft, scale = semLeft)
    ci_lower_stay,ci_upper_stay = st.t.interval(0.95,len(stayed)-1,
                                                loc = avgStay, scale = semStay)
    
    

    result.append({'variable': col,'ci_lower_stay':ci_lower_stay,
                   'ci_upper_stay':ci_upper_stay,'ci_lower_left':ci_lower_left,
                   'ci_upper_left':ci_upper_left})

ci_interval = pd.DataFrame(result).sort_values('variable')

print(ci_interval)








# MACHINE LEARNING
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.metrics import *

y = dataProcessed['attrition'].map({False:0, True:1})

X = dataProcessed.drop(columns = ['daily_rate', 'employee_number','monthly_rate',
                                                   'hourly_rate', 'performance_rating',
                                                   'total_working_years',
                                                   'years_since_last_promotion','attrition']) 


# Test/Train split
x_train,x_test,y_train,y_test = train_test_split(X,
                                                 y,
                                                 test_size = 0.2,
                                                 random_state = 42)


#Baseline Model
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report

# Majority Class
dummy_clf = DummyClassifier(strategy = 'most_frequent')
dummy_clf.fit(x_train,y_train)

y_pred = dummy_clf.predict(x_test)

print('Majority Class:')
print(classification_report(y_test,y_pred))



# Feature Preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier, XGBRegressor

numerical_cols = ['age','distance_from_home','education','environment_satisfaction',
                   'job_involvement','job_level','job_satisfaction','monthly_income',
                   'num_companies_worked','percent_salary_hike','relationship_satisfaction',
                   'stock_option_level','training_times_last_year','work_life_balance',
                   'years_at_company','years_in_current_role','years_with_curr_manager']

categorical_cols = ['business_travel','department','education_field',
                     'gender','job_role','marital_status','overtime',
                     'tenure_groups','promotion_recency','long_current_role_tenure']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_cols),
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'),
     categorical_cols)])

#Candidate Models
#1. Logistic Regression
pipeline_logistic = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression(max_iter=1000))])

pipeline_logistic.fit(x_train, y_train)
y_pred_log = pipeline_logistic.predict(x_test)

print('Logistic Regression:')
print(classification_report(y_test,y_pred_log))

#2. Decision Tree
pipeline_decision = Pipeline([
    ('preprocessor',preprocessor),
    ('model',DecisionTreeClassifier())])

pipeline_decision.fit(x_train,y_train)
y_pred_de= pipeline_decision.predict(x_test)

print('Decision Tree: ')
print(classification_report(y_test,y_pred_de))

#3. Random Forest
pipeline_rf = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(random_state=42))])

pipeline_rf.fit(x_train, y_train)
y_pred_rf = pipeline_rf.predict(x_test)

print("Random Forest:")
print(classification_report(y_test, y_pred_rf))

#4. XGBoost
pipeline_xgb = Pipeline([
    ('preprocessor', preprocessor),
    ('model', XGBClassifier(random_state=42))])

pipeline_xgb.fit(x_train, y_train)
y_pred_xgb = pipeline_xgb.predict(x_test)

print("XGBoost:")
print(classification_report(y_test, y_pred_xgb))

#5. Gradient Boosting
pipeline_gb = Pipeline([
    ('preprocessor', preprocessor),
    ('model', GradientBoostingClassifier(random_state=42))])

pipeline_gb.fit(x_train, y_train)
y_pred_gb = pipeline_gb.predict(x_test)

print("Gradient Boost:")
print(classification_report(y_test, y_pred_gb))


#performing Cross Validation
#1. Logistc Regression
from sklearn.model_selection import cross_val_score, KFold,StratifiedKFold

kf = StratifiedKFold(n_splits = 5, shuffle=True,random_state = 42)
scores_log = cross_val_score(pipeline_logistic,X,y,cv = kf, scoring = 'roc_auc')
print('Logistic Regression')
print(f'Scores Per Fold: {scores_log}')
print(f'Mean roc_auc: {round(scores_log.mean(),2)}')
print(f'Std: {round(scores_log.std(),2)}')

#2. Decision Tree
scores_de = cross_val_score(pipeline_decision,X,y,cv = kf,
                            scoring = 'roc_auc',error_score='raise')
print('Decision Tree:')
print(f'Scores Per Fold: {scores_de}')
print(f'Mean roc_auc: {round(scores_de.mean(),2)}')
print(f'Std: {round(scores_de.std(),2)}')

#3. Random Forest
scores_rf = cross_val_score(pipeline_rf,X,y,cv=kf,scoring = 'roc_auc')
print('Random Forest')
print(f'Scores Per Fold: {scores_rf}')
print(f'Mean roc_auc: {round(scores_rf.mean(),2)}')
print(f'Std: {round(scores_rf.std(),2)}')

#4. XGBoost
scores_xgb = cross_val_score(pipeline_xgb,X,y,cv=kf,scoring = 'roc_auc')
print('XGBoost')
print(f'Scores Per Fold: {scores_xgb}')
print(f'Mean roc_auc: {round(scores_xgb.mean(),2)}')
print(f'Std: {round(scores_xgb.std(),2)}')

#5. Gradient Boosting
scores_gb = cross_val_score(pipeline_gb,X,y,cv=kf,scoring = 'roc_auc')
print('Gradient Boosting')
print(f'Scores Per Fold: {scores_gb}')
print(f'Mean roc_auc: {round(scores_gb.mean(),2)}')
print(f'Std: {round(scores_gb.std(),2)}')



# Plotting ROC and Precision-Recall curve
from sklearn.metrics import RocCurveDisplay as roc
from sklearn.metrics import PrecisionRecallDisplay as pr

#1 logistic
roc.from_estimator(pipeline_logistic,x_test,y_test)
plt.title('Logistic Regression ROC Curve')
plt.show()

#2 Decision Tree
roc.from_estimator(pipeline_decision,x_test,y_test)
plt.title('Decision Tree ROC Curve')
plt.show()

#3 Random Forest
roc.from_estimator(pipeline_rf,x_test,y_test)
plt.title('Random Forest ROC Curve')
plt.show()

#4 XGBoost
roc.from_estimator(pipeline_xgb,x_test,y_test)
plt.title('XGBoost ROC Curve')
plt.show()

#5 Gradient Boosting
roc.from_estimator(pipeline_gb,x_test,y_test)
plt.title('Gradient Boosting Precision-Recall Curves')
plt.show()


#1 logistic
pr.from_estimator(pipeline_logistic,x_test,y_test)
plt.title('Logistic Regression ROC Curve')
plt.show()

#2 Decision Tree
pr.from_estimator(pipeline_decision,x_test,y_test)
plt.title('Decision Tree Precision-Recall Curve')
plt.show()

#3 Random Forest
pr.from_estimator(pipeline_rf,x_test,y_test)
plt.title('Random Forest Precision-Recall Curve')
plt.show()

#4 XGBoost
pr.from_estimator(pipeline_xgb,x_test,y_test)
plt.title('XGBoost Precision-Recall Curve')
plt.show()

#5 Gradient Boosting
pr.from_estimator(pipeline_gb,x_test,y_test)
plt.title('Gradient Boosting Precision-Recall Curves')
plt.show()


#Confusion Matrices
from sklearn.metrics import ConfusionMatrixDisplay

logistic_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred_log, labels=[False, True])
disp = ConfusionMatrixDisplay(confusion_matrix=logistic_matrix, display_labels=['Stayed', 'Left'])
disp.plot()
plt.title('Logistic Regression Confusion Matrix')
plt.show()

gb_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred_gb, labels=[False, True])
disp = ConfusionMatrixDisplay(confusion_matrix=gb_matrix, display_labels=['Stayed', 'Left'])
disp.plot()
plt.title('Gradient Boost Confusion Matrix')
plt.show()

xgb_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred_xgb, labels=[False, True])
disp = ConfusionMatrixDisplay(confusion_matrix=xgb_matrix, display_labels=['Stayed', 'Left'])
disp.plot()
plt.title('XGBoost Confusion Matrix')
plt.show()





#Attrition probabilities

y_pred_log = pipeline_logistic.predict(x_test)
proba = pipeline_logistic.predict_proba(x_test)

model_predictions = pd.DataFrame({
    'employee_number': dataProcessed.loc[x_test.index, 'employee_number'].values,
    'actual_attrition': y_test.values,
    'predicted_attrition': y_pred_log})


model_predictions['risk_score'] = (np.clip(proba[:, 1], 0, 1) * 100).round(1)
model_predictions['risk_category'] = pd.cut(
    model_predictions['risk_score'],
    bins=[-0.1, 40, 70, 100],
    labels=['Low Risk', 'Medium Risk', 'High Risk'])


model_predictions.to_sql('model_predictions', engine,
                  if_exists = 'append',
                  index = False)




#department risk Summary
model_predictions['department'] = dataProcessed.loc[x_test.index, 'department'].values

department_risk_summary = model_predictions.groupby('department').agg(
    total_employees=('employee_number', 'count'),
    avg_risk_score=('risk_score', 'mean'),
    high_risk_count=('risk_category', lambda x: (x == 'High Risk').sum()),
    medium_risk_count=('risk_category', lambda x: (x == 'Medium Risk').sum()),
    low_risk_count=('risk_category', lambda x: (x == 'Low Risk').sum()),).reset_index()

department_risk_summary['pct_high_risk'] = (
    department_risk_summary['high_risk_count'] / department_risk_summary['total_employees'] * 100).round(1)

department_risk_summary['avg_risk_score'] = department_risk_summary['avg_risk_score'].round(1)

department_risk_summary.to_sql('department_risk_summary', engine,
                  if_exists = 'append',
                  index = False)








#SHAP
import shap

X_train_transformed = pipeline_logistic.named_steps['preprocessor'].transform(x_train)
feature_names = pipeline_logistic.named_steps['preprocessor'].get_feature_names_out()
X_train_transformed_df = pd.DataFrame(X_train_transformed, columns=feature_names)


explainer = shap.Explainer(pipeline_logistic.named_steps['model'], X_train_transformed_df)
shap_values = explainer(X_train_transformed_df)

plt.figure(figsize=(10,6))
shap.plots.bar(shap_values)
plt.show()



plt.figure(figsize=(10,6))
shap.plots.beeswarm(shap_values)
plt.show()


#waterfall plot for top 5 high risk employees
train_prob = pipeline_logistic.predict_proba(x_train)[:, 1]
top5_idx = np.argsort(train_prob)[-5:][::-1]

for idx in top5_idx:
    plt.figure(figsize=(10, 6))
    shap.plots.waterfall(shap_values[idx])
    plt.show()

#waterfall plot for top 5 low risk employees
bottom5_idx = np.argsort(train_prob)[:5]

for idx in bottom5_idx:
    plt.figure(figsize=(10, 6))
    shap.plots.waterfall(shap_values[idx])
    plt.show()



#odds ratio
odds_ratio = np.exp(pipeline_logistic.named_steps['model'].coef_[0])

feature_names = pipeline_logistic.named_steps['preprocessor'].get_feature_names_out()

df_odds = pd.DataFrame({
    'feature': feature_names,
    'odds_ratio': odds_ratio})

df_odds = df_odds.sort_values('odds_ratio', ascending=False)
print(df_odds)



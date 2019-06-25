-- Geetha Venkataswamy Data Analysis Section 
-- Once you have a complete database, do the following:

-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT ee.emp_no, ee.last_name, ee.first_name, ee.gender, sa.salary
FROM employees ee, salaries sa
WHERE ee.emp_no = sa.emp_no;

-- 2. List employees who were hired in 1986.
SELECT * 
FROM EMPLOYEES
WHERE EXTRACT(YEAR FROM hire_date) = 1986

-- 3. List the manager of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name, and start and end employment dates.

--GEETHA NOTE: Assumption-- the end employment date will be pulled from the titles database as a manager 
--could have more than one position over the course of their time with the company AND not be a manager today 
--(the dept manager to_date would not reflect their employment end date)
-- According to the results below all the managers are still with the company as the latest to_date is the infinity number

SELECT DM.dept_no, D.dept_name, DM.emp_no, EE.last_name, EE.first_name, EE.hire_date, TI.to_date
FROM departments as D, dept_manager as DM, employees as EE
, titles as TI
WHERE DM.emp_no = EE.emp_no
AND DM.dept_no = D.dept_no
AND TI.emp_no = DM.emp_no
and TI.to_date =
(Select to_date from titles
where emp_no = DM.emp_no
order by to_date DESC
LIMIT 1)


-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT EE.emp_no, EE.last_name, EE.first_name, D.dept_name
FROM employees as EE, dept_emp as DE, departments as D
WHERE EE.emp_no = DE.emp_no
AND D.dept_no = DE.dept_no

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
--GEETHA NOTE: well that was a surprising number of results!
SELECT *
FROM employees
WHERE first_name = 'Hercules'
AND last_name like 'B%'

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT EE.emp_no, EE.last_name, EE.first_name, D.dept_name
FROM employees as EE, dept_emp as DE, departments as D
WHERE EE.emp_no = DE.emp_no
AND D.dept_no = DE.dept_no
AND D.dept_name = 'Sales'

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT EE.emp_no, EE.last_name, EE.first_name, D.dept_name
FROM employees as EE, dept_emp as DE, departments as D
WHERE EE.emp_no = DE.emp_no
AND D.dept_no = DE.dept_no
AND (D.dept_name = 'Sales' OR D.dept_name = 'Development')

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
--GEETHA NOTE: Is everyone at this company related???
SELECT last_name, count(last_name) as FREQ
FROM employees 
group by last_name
order by FREQ desc

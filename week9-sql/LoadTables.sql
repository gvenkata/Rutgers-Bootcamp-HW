--Geetha Venkataswamy Data Engineering Exercise
-- Copy and paste this into PSQL to load tables created

\COPY Employees FROM 'C:\Users\gvenkataswamy\Documents\GitHub\Rutgers-Bootcamp-HW\week9-sql\data\employees.csv' DELIMITER ',' CSV HEADER;

\COPY Salaries FROM 'C:\Users\gvenkataswamy\Documents\GitHub\Rutgers-Bootcamp-HW\week9-sql\data\salaries.csv' DELIMITER ',' CSV HEADER;

\COPY Departments FROM 'C:\Users\gvenkataswamy\Documents\GitHub\Rutgers-Bootcamp-HW\week9-sql\data\departments.csv' DELIMITER ',' CSV HEADER;

\COPY Dept_emp FROM 'C:\Users\gvenkataswamy\Documents\GitHub\Rutgers-Bootcamp-HW\week9-sql\data\dept_emp.csv' DELIMITER ',' CSV HEADER;

\COPY Dept_manager FROM 'C:\Users\gvenkataswamy\Documents\GitHub\Rutgers-Bootcamp-HW\week9-sql\data\dept_manager.csv' DELIMITER ',' CSV HEADER;

\COPY Titles FROM 'C:\Users\gvenkataswamy\Documents\GitHub\Rutgers-Bootcamp-HW\week9-sql\data\titles.csv' DELIMITER ',' CSV HEADER;

commit; 
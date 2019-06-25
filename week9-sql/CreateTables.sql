-- Geetha Venkataswamy Data EE section 

Drop table if exists Employees CASCADE; 
Drop table if exists Salaries CASCADE; 
Drop table if exists Departments CASCADE; 
Drop table if exists Dept_emp CASCADE; 
Drop table if exists Dept_manager CASCADE; 
Drop table if exists Titles CASCADE; 

CREATE TABLE Employees (
    emp_no int   NOT NULL,
    birth_date date   NOT NULL,
    first_name varchar(50)   NOT NULL,
    last_name varchar(50)   NOT NULL,
    gender varchar(5)   NOT NULL,
    hire_date date   NOT NULL,
    CONSTRAINT pk_Employees PRIMARY KEY (emp_no)
);

CREATE TABLE Salaries (
    emp_no int   NOT NULL,
    salary int   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL,
	CONSTRAINT fk_Salaries_emp_no FOREIGN KEY(emp_no) REFERENCES Employees(emp_no)
);

CREATE TABLE Departments (
    dept_no varchar(5)   NOT NULL,
    dept_name varchar(50) NOT NULL,
    CONSTRAINT pk_Departments PRIMARY KEY (dept_no)
);

CREATE TABLE Dept_emp (
    emp_no int   NOT NULL,
    dept_no varchar(5)   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL, 
	CONSTRAINT fk_Dept_emp_emp_no FOREIGN KEY(emp_no) REFERENCES Employees(emp_no), 
	CONSTRAINT fk_Dept_emp_dept_no FOREIGN KEY(dept_no) REFERENCES Departments(dept_no)
);

CREATE TABLE Dept_manager (
    dept_no varchar(5) NOT NULL,
    emp_no int NOT NULL,
    from_date date NOT NULL,
    to_date date NOT NULL,
	CONSTRAINT fk_Dept_manager_dept_no FOREIGN KEY(dept_no) REFERENCES Departments(dept_no),
	CONSTRAINT fk_Dept_manager_emp_no FOREIGN KEY(emp_no) REFERENCES Employees(emp_no)
);

CREATE TABLE Titles (
    emp_no int   NOT NULL,
    title varchar(50) NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL, 
	CONSTRAINT fk_Titles_emp_no FOREIGN KEY(emp_no) REFERENCES Employees(emp_no)
);



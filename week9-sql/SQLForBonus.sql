SELECT TI.title, round(avg(SA.salary), 2) as MONEY
FROM 
employees as EE, 
titles as TI, 
salaries as SA
WHERE
EE.emp_no = TI.emp_no
AND
SA.emp_no = EE.emp_no
group by TI.title
order by MONEY DESC

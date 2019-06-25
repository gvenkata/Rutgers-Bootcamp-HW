SELECT TI.title, round(avg(SA.salary), 2)
FROM 
employees as EE, 
titles as TI, 
salaries as SA
WHERE
EE.emp_no = TI.emp_no
AND
SA.emp_no = EE.emp_no
group by TI.title
order by round(avg(SA.salary), 2) DESC

--Task: find the candidates who have all three of these skills: Python, Tableau and PostgreSQL. Return candidate_id, sorted ascending.


SELECT candidate_id

FROM candidates

where skill in('Python','Tableau','PostgreSQL')

group by candidate_id 
HAVING count(*) = 3
order by candidate_id asc

limit 1
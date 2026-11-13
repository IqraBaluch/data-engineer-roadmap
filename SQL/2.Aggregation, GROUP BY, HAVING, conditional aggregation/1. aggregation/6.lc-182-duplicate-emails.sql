-- · emails that appear more than once
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
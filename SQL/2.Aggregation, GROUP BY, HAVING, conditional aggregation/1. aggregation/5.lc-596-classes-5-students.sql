-- lc-596-classes-5-students.sql · classes with at least five students

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;
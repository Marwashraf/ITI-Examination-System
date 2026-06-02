-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'Which SQL clause is used to retrieve data from a database?', 'SELECT', 'WHERE', 'FROM', 'JOIN', 'SELECT',12),
('MCQ', 'In SQL, which aggregate function is used to calculate the average value of a numeric column?', 'COUNT', 'SUM', 'AVG', 'MAX', 'AVG',12),
('MCQ', 'What is the purpose of the GROUP BY clause in SQL?', 'To filter rows based on a specified condition', 'To sort the result set in ascending or descending order', 'To perform calculations on numeric columns', 'To group rows that have the same values into summary rows', 'To group rows that have the same values into summary rows',12),
('MCQ', 'Which SQL statement is used to add new rows to a table?', 'INSERT INTO', 'UPDATE', 'DELETE', 'ALTER TABLE', 'INSERT INTO',12),
('MCQ', 'What is the purpose of the HAVING clause in SQL?', 'To specify a condition for filtering rows', 'To specify a condition for filtering groups', 'To sort the result set in ascending or descending order', 'To perform calculations on numeric columns', 'To specify a condition for filtering groups',12),
('MCQ', 'Which SQL JOIN type returns all records from both tables, joining records where available?', 'INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'FULL OUTER JOIN', 'FULL OUTER JOIN',12),
('MCQ', 'What is the purpose of the DISTINCT keyword in SQL?', 'To delete duplicate rows from a table', 'To update rows in a table', 'To select unique values from a column', 'To join two or more tables', 'To select unique values from a column',12),
('MCQ', 'Which SQL function is used to return the current date and time?', 'GETDATE()', 'CURRENT_TIMESTAMP', 'NOW()', 'SYSDATE', 'CURRENT_TIMESTAMP',12),
('MCQ', 'Which SQL statement is used to modify existing data in a table?', 'UPDATE', 'INSERT INTO', 'DELETE', 'ALTER TABLE', 'UPDATE',12),
('MCQ', 'What is the purpose of the ORDER BY clause in SQL?', 'To filter rows based on a specified condition', 'To specify a condition for filtering groups', 'To sort the result set in ascending or descending order', 'To perform calculations on numeric columns', 'To sort the result set in ascending or descending order',12);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2,Choice_3,Choice_4 ,correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'SQL stands for Structured Query Language.', 'True', 'False',Null,Null ,'True',12),
('TrueFalse', 'In SQL, the WHERE clause is used to filter rows based on a specified condition.', 'True', 'False', Null,Null,'True',12),
('TrueFalse', 'SQL can only be used to query data from relational databases.', 'True', 'False', Null,Null,'False',12),
('TrueFalse', 'The GROUP BY clause is used to filter rows based on a specified condition.', 'True', 'False',Null,Null ,'False',12),
('TrueFalse', 'The EXISTS operator in SQL is used to check whether a subquery returns any rows.', 'True','False', Null,Null,'True',12),
('TrueFalse', 'SQL views can be used to simplify complex queries and provide an additional layer of security.', 'True', 'False',Null,Null ,'True',12),
('TrueFalse', 'SQL allows users to perform mathematical calculations on numeric data using built-in functions.', 'True', 'False', Null,Null,'True',12),
('TrueFalse', 'The UNION operator in SQL is used to combine the results of two or more SELECT statements.', 'True', 'False', Null,Null,'True',12),
('TrueFalse', 'SQL transactions are used to ensure the integrity of data by grouping multiple SQL statements into a single unit of work.', 'True', 'False',Null,Null ,'True',12),
('TrueFalse', 'In SQL, the LIKE operator is used to search for a specified pattern in a column.', 'True', 'False', Null,Null,'True',12);

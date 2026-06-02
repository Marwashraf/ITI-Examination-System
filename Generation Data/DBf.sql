-- Insert MCQ Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice,Crs_ID)
VALUES 
('MCQ', 'What is the primary purpose of a database management system (DBMS)?', 'To create data models', 'To design user interfaces', 'To store, manage, and retrieve data', 'To optimize network performance', 'To store, manage, and retrieve data',7),
('MCQ', 'Which of the following is NOT a type of database model?', 'Hierarchical', 'Relational', 'Object-Oriented', 'Sequential', 'Sequential',7),
('MCQ', 'What does SQL stand for?', 'Structured Query Language', 'Simple Query Language', 'Standardized Query Language', 'Sequential Query Language', 'Structured Query Language',7),
('MCQ', 'Which SQL command is used to retrieve data from a database?', 'INSERT', 'UPDATE', 'SELECT', 'DELETE', 'SELECT',7),
('MCQ', 'What is a primary key in a relational database?', 'A unique identifier for each row in a table', 'A foreign key that references another table', 'An attribute that allows null values', 'A constraint that ensures data integrity', 'A unique identifier for each row in a table',7),
('MCQ', 'Which of the following data types is used to store whole numbers in SQL?', 'VARCHAR', 'DECIMAL', 'INTEGER', 'DATE', 'INTEGER',7),
('MCQ', 'What is the purpose of a foreign key in a relational database?', 'To enforce referential integrity between tables', 'To provide a unique identifier for each row in a table', 'To store text data', 'To create relationships between tables', 'To enforce referential integrity between tables',7),
('MCQ', 'Which SQL command is used to add new rows to a table?', 'INSERT', 'UPDATE', 'SELECT', 'DELETE', 'INSERT',7),
('MCQ', 'What does the term "ACID" stand for in database transactions?', 'Atomicity, Consistency, Isolation, Durability', 'Association, Cohesion, Inheritance, Dependency', 'Aggregation, Composition, Inheritance, Delegation', 'Atomicity, Consistency, Isolation, Dependency', 'Atomicity, Consistency, Isolation, Durability',7),
('MCQ', 'Which of the following is NOT a relational database management system?', 'MySQL', 'MongoDB', 'Oracle', 'PostgreSQL', 'MongoDB',7);

-- Insert True/False Questions
INSERT INTO Questions (QUESTION_TYPE, QUESTION, Choice_1,Choice_2,Choice_3,Choice_4,correct_choice,Crs_ID)
VALUES 
('TrueFalse', 'A database schema defines the structure of a database, including tables, columns, and relationships.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'Normalization is the process of organizing data in a database to minimize redundancy and dependency.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'A stored procedure is a precompiled set of one or more SQL statements that are stored in the database and can be called by applications.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'In a relational database, a view is a virtual table based on the result set of a SELECT query.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'In SQL, the ORDER BY clause is used to specify the order in which rows should be returned in a query result.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'A database transaction is a unit of work that must be executed as a single, indivisible operation.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'In a relational database, referential integrity ensures that relationships between tables remain consistent.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'SQL injection is a technique used to exploit vulnerabilities in a database by injecting malicious SQL code into an application''s input fields.', 'True','False',Null,Null,'True',7),
('TrueFalse', 'In a relational database, a foreign key is a field or combination of fields that uniquely identifies a record in a table.','True','False',Null,Null ,'False',7),
('TrueFalse', 'A database index is a data structure that improves the speed of data retrieval operations on a database table.', 'True','False',Null,Null,'True',7);

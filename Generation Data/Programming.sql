-- Insert questions for the DAX course into QUESTINS table
INSERT INTO Questions (QUESTION_TYPE, QUESTION, choice_1, choice_2, choice_3, choice_4, correct_choice, crs_ID)
VALUES 
('MCQ', 'Which of the following is NOT a fundamental programming concept?', ' Variables', 'Functions', 'Loops', 'Algorithms', 'Algorithms', 1),
('MCQ', 'What does the acronym "IDE" stand for in the context of programming?', 'Integrated Development Environment', 'Interactive Data Entry', ' Internet Development Environment', 'Integrated Design Environment', ' Integrated Development Environment',1),
('MCQ', 'In programming, what is the purpose of a conditional statement?', 'To execute a block of code repeatedly', ' To declare variables', ' To make decisions based on conditions ', 'To define functions', 'To make decisions based on conditions', 1),
('True/False', 'In programming, a variable can hold only one value throughout its lifetime.',' True', 'False', Null, Null,'False', 1),
('True/False', 'if-else" statement in programming allows for executing different blocks of code based on certain conditions', 'True', 'False', NULL, NULL, 'True', 1),
('True/False', 'A loop in programming allows for executing a block of code multiple times.', 'False', 'True', NULL, NULL, 'True', 1),
('MCQ', 'What is the purpose of a variable in programming?', ' To store and manipulate data', 'FunctioTo display text on the screenns', 'Loops', 'Algorithms', 'Algorithms', 1),
('MCQ', 'Which of the following is not a basic data type in most programming languages?', 'Integer','String','Float','Array', 'Array',1),
('MCQ', 'What is the result of 5 + 3 * 2 in most programming languages?','16','11','13','15' ,'11', 1),
('TrueFalse', 'In programming, a comment is a piece of code that is executed by the computer.', 'True','False',Null,Null,'False', 1),
('True/False', 'A loop in programming allows a set of instructions to be repeated multiple times based on a condition.', 'True', 'False', NULL, NULL, 'True', 1),
('True/False', ' Object-Oriented Programming (OOP) is a programming paradigm that focuses on breaking down a program into a collection of objects that interact with each other.', 'False', 'True', NULL, NULL, 'True', 1);




